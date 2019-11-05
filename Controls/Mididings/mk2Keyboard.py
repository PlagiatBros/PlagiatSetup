# coding=utf8
from mididings import *
from mididings.extra.osc import OSCInterface
from mididings.extra.inotify import AutoRestart
from mididings.extra.osc import SendOSC
from utils import OSCCustomInterface
from math import log10

from liblo import ServerThread
from liblo import send
from time import sleep


config(
	backend='jack',
	client_name='Mk2KeyBoardRoutes',
	out_ports=['Mk2OutBass', 'Mk2OutTreble', 'Mk2OutRhodes', 'Mk2OutTapeutape', 'Mk2OutWobble', 'PBseq24', 'PBTapeutape', 'PBguitarix'],
	in_ports=['Mk2In']
)

from ports import *
from aliases import *

hook(
    OSCInterface(mk2inport, mk2outport),
    AutoRestart()
)

gatecancel = Filter(CTRL) >> [
	CtrlFilter(41) >> [
	    SendOSC(vxjeannotpreport, '/strip/VxJeannotGars/Gate/Threshold%20(dB)/unscaled', lambda ev: -ev.value/127 * 54.0 - 24),
	    SendOSC(vxjeannotpreport, '/strip/VxJeannotMeuf/Gate/Threshold%20(dB)/unscaled', lambda ev: -ev.value/127 * 54.0 - 24),
    ],
        CtrlFilter(42) >> [
	    SendOSC(monitorsjeannotport, '/strip/Klick/Gain/Mute', lambda ev: ev.value/127.),
	    SendOSC(monitorsjeannotport, '/strip/Klick/Gain/Mute', lambda ev: ev.value/127.),
    ]
] >> Discard()


bassfilter = CtrlFilter(18) >> [
    # SendOSC(bassmainport, '/strip/BassMain/Calf%20Filter/Frequency/unscaled', lambda ev: 20000. * pow(10,((-log10(71/20000.))*ev.value) / 127. + log10(71/20000.))),
    # SendOSC(bassmainport, '/strip/BassDry/Calf%20Filter/Frequency/unscaled', lambda ev: 20000. * pow(10,((-log10(71/20000.))*ev.value) / 127. + log10(71/20000.)))
]

looperctl = CtrlFilter(range(109,117)) >> CtrlValueFilter(127) >> [

	CtrlFilter(109) >> SendOSC(slport, '/sl/4/hit', 'record'), #pre
	CtrlFilter(110) >> SendOSC(slport, '/sl/4/hit', 'overdub'),
	CtrlFilter(111) >> SendOSC(slport, '/sl/4/hit', 'pause_on'),
	CtrlFilter(112) >> SendOSC(slport, '/sl/5/hit', 'record'), #post
	CtrlFilter(113) >> SendOSC(slport, '/sl/5/hit', 'overdub'),
	CtrlFilter(114) >> SendOSC(slport, '/sl/5/hit', 'pause_on'),
	CtrlFilter(116) >> SendOSC(slport, '/sl/-1/hit', 'reverse'), #reverse

]

def pitchwheel_cb(ev):
	return 1.0 - (abs(ev.value) / (8192.0)) * 0.75


def pitchwheel_cb_vx(offset):
	def fn(ev):
		ratio = abs(ev.value) / 8192.0
		xoffset = offset + 0 -  24. * ratio
		print(xoffset)
		return xoffset
	return fn

last_pitch = 0
def dedupe(ev):
	global last_pitch
	if ev.value != last_pitch:
		last_pitch = ev.value
		return ev
	else:
		return None


pitch = Filter(PITCHBEND) >> Process(dedupe) >> [

    SendOSC(samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled', pitchwheel_cb),
    SendOSC(samplesmainport, '/strip/Keyboards/AM%20pitchshifter/Pitch%20shift/unscaled',   pitchwheel_cb),


    SendOSC(vocoderjeannotport, '/x42/parameter', 6, pitchwheel_cb_vx(0)),
    SendOSC(vocoderorlport, '/x42/parameter', 6, pitchwheel_cb_vx(0)),
    SendOSC(vocoderjeannotportgars, '/x42/parameter', 6, pitchwheel_cb_vx(-4)),
    SendOSC(vocoderorlportgars, '/x42/parameter', 6, pitchwheel_cb_vx(-4)),
    SendOSC(vocoderjeannotportmeuf, '/x42/parameter', 6, pitchwheel_cb_vx(4)),
    SendOSC(vocoderorlportmeuf, '/x42/parameter', 6, pitchwheel_cb_vx(4)),

    # SendOSC(vxmainport, '/strip/VxORLMain/AM%20pitchshifter/Pitch%20shift/unscaled', 		pitchwheel_cb),
    # SendOSC(vxmainport, '/strip/VxJeannotMain/AM%20pitchshifter/Pitch%20shift/unscaled',  	pitchwheel_cb),

    SendOSC(bassmainport, '/strip/BassMain/AM%20pitchshifter/Pitch%20shift/unscaled',  	 	pitchwheel_cb),
    SendOSC(bassmainport, '/strip/BassSynth/AM%20pitchshifter/Pitch%20shift/unscaled',  	pitchwheel_cb),

]  >> Discard()


glitch_state = [
	0.0, # active
	0.0, # strength
	0.0, # noise
	0.0, # hue
	1.0, # saturation
	1.0, # value
	1.0, # alpha
	0.0, # invert
]

def send_glitch_state(ev):
	cc  = ev.ctrl
	val = 1.0 * ev.value

	if   cc == 1:
		glitch_state[0] =  float(val>0)
		glitch_state[1] =  val / 127
	elif cc == 12:
		glitch_state[1] =  5 * val / 127
	elif cc == 13:
		glitch_state[2] =  5 * val / 127
	elif cc == 14:
		glitch_state[3] =  5 * val / 127
	elif cc == 15:
		glitch_state[4] =  1.0 - (val / 127)
	elif cc == 16:
		glitch_state[5] =  1 + val
	elif cc == 17:
		glitch_state[7] =  val % 2
	elif cc == 18:
		# glitch_state[6] = 1.0 - (val / 127)
		pass

	send(lightseqport, '/Lightseq/Scene/Play', 'glitch_timeout')
	for port in [rpijardinport, rpicourport]:
		send(port, '/pyta/post_process/set_all', *glitch_state)


video = Filter(CTRL) >> CtrlFilter([1] + range(12,19)) >> Call(send_glitch_state) >> Discard()



samples_mute = Filter(NOTE) >> [
    KeyFilter(notes=['f2','c3','g3']) >> Filter(NOTEON) >> [
        SendOSC(samplesmainport, '/strip/SamplesMain/Gain/Mute', 1.0)
    ],
    KeyFilter(notes=['f2','c3','g3']) >> Filter(NOTEOFF) >> [
        SendOSC(samplesmainport, '/strip/SamplesMain/Gain/Mute', 0.0)
    ],
]

bass_mute = Filter(NOTE) >> [
    KeyFilter(notes=['f2','c3','g3']) >> Filter(NOTEON) >> [
        SendOSC(bassmainport, '/strip/BassMain/Gain/Mute', 1.0)
    ],
    KeyFilter(notes=['f2','c3','g3']) >> Filter(NOTEOFF) >> [
        SendOSC(bassmainport, '/strip/BassMain/Gain/Mute', 0.0)
    ],
]

bass_and_samples_mute = Filter(NOTE) >> [bass_mute, samples_mute]

run(
    scenes = {
        1: 	Scene("BassWobbleCtrl",
                [
                [Filter(NOTE), Filter(PITCHBEND)] >> Output('Mk2OutWobble', 1),
                bassfilter,
                gatecancel,
				looperctl,
				pitch
                ]
          ),
        2: 	Scene("VxDelayCtrl",
                [
                KeyFilter(notes=['f2','c3','g3']) >> [
                    Filter(NOTEON) >> SendOSC(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 0.0),
                    Filter(NOTEOFF) >> SendOSC(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 1.0),
                    ] >> Discard(),
                bassfilter,
                gatecancel,
				looperctl,
				pitch
                ]
              ),
        3: Scene("Connasses SACEM samples",
                [
                Filter(NOTEON) >> Output('Mk2OutTapeutape', 1),
                bassfilter,
                gatecancel,
				looperctl,
				pitch
                ]
              ),
        4: Scene("Samples cut",
                [
                    samples_mute,
                    bassfilter,
                    gatecancel,
					looperctl,
					pitch
                ] >> Discard()
              ),
        5: Scene("HorroCore Couplet 1",
                [
                    KeyFilter(notes=['f2','c3','g3']) >> Filter(NOTEON) >> [

	                    vxorlmeuf_on,
			            vxorlgars_off,
			            vxorldisint_off,
			            vxorldelay_off,
			            vxorlvocode_on,

			            vxjeannotdelay_off,
			            vxjeannotgars_off,
			            vxjeannotmeuf_on,
			            vxjeannotdisint_off,
			            vxjeannotvocode_off,

                    ],
                    KeyFilter(notes=['f2','c3','g3']) >> Filter(NOTEOFF) >> [

	                    vxorlmeuf_on,
			            vxorlgars_off,
			            vxorldisint_off,
			            vxorldelay_off,
			            vxorlvocode_off,

			            vxjeannotdelay_off,
			            vxjeannotgars_on,
			            vxjeannotmeuf_off,
			            vxjeannotdisint_off,
			            vxjeannotvocode_off,

                    ],
					samples_mute,
                    bassfilter,
                    gatecancel,
					looperctl,
					pitch
                ] >> Discard()
              ),
		  6: Scene("HorroCore Couplet 2",
                  [
					KeyFilter(notes=['f2','c3','g3']) >> Filter(NOTEOFF) >> [

					    Program(3) >> cseqtrigger,

					],
				  	[
                      KeyFilter(notes=['f2','c3','g3']) >> Filter(NOTEON) >> [

  	                    vxorlmeuf_off,
  			            vxorlgars_on,
  			            vxorldisint_off,
  			            vxorldelay_off,
  			            vxorlvocode_off,

                      ],
                      KeyFilter(notes=['f2','c3','g3']) >> Filter(NOTEOFF) >> [

  	                    vxorlmeuf_on,
  			            vxorlgars_off,
  			            vxorldisint_off,
  			            vxorldelay_off,
  			            vxorlvocode_on,

				        Program(3) >> cseqtrigger,

                      ],
  					samples_mute,
                    bassfilter,
                    gatecancel,
  					looperctl,
  					pitch
                  ] >> Discard()],
                ),
          7: 	Scene("Clap",
                  [
                  KeyFilter(notes=['f2','c3','g3']) >> Filter(NOTEON) >> NoteOn(64,127) >> Output('Mk2OutTapeutape', 1),
                  bassfilter,
                  gatecancel,
				  looperctl,
					pitch
                  ]
                ),
        8: Scene("Bass & Samples cut",
                [
                    bass_and_samples_mute,
                    bassfilter,
                    gatecancel,
					looperctl,
					pitch
                ] >> Discard()
              ),
      9: Scene("Bass cut",
              [
                  bass_mute,
                  bassfilter,
                  gatecancel,
					looperctl,
					pitch
              ] >> Discard()
            ),
    },
    control = [
		video,
		Filter(PROGRAM) >> SceneSwitch()
	],
    pre = ~Filter(PROGRAM)
)
