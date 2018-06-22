# coding=utf8
from mididings import *
from mididings.extra.osc import OSCInterface
from mididings.extra.inotify import AutoRestart
from mididings.extra.osc import SendOSC
from utils import OSCCustomInterface
from math import log10

from liblo import ServerThread
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
    SendOSC(bassmainport, '/strip/BassMain/Calf%20Filter/Frequency/unscaled', lambda ev: 20000. * pow(10,((-log10(71/20000.))*ev.value) / 127. + log10(71/20000.))),
    SendOSC(bassmainport, '/strip/BassDry/Calf%20Filter/Frequency/unscaled', lambda ev: 20000. * pow(10,((-log10(71/20000.))*ev.value) / 127. + log10(71/20000.)))
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

pitch = Filter(PITCHBEND) >> [
    SendOSC(samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled', lambda ev: 1 - (abs(ev.value) / (8191.0)) * 0.75),
    SendOSC(vxmainport, '/strip/VxORLMain/AM%20pitchshifter/Pitch%20shift/unscaled', 		lambda ev: 1 - (abs(ev.value) / (8191.0)) * 0.75),
    SendOSC(vxmainport, '/strip/VxJeannotMain/AM%20pitchshifter/Pitch%20shift/unscaled',  	lambda ev: 1 - (abs(ev.value) / (8191.0)) * 0.75),
    SendOSC(bassmainport, '/strip/BassMain/AM%20pitchshifter/Pitch%20shift/unscaled',  	 	lambda ev: 1 - (abs(ev.value) / (8191.0)) * 0.75),
    SendOSC(bassmainport, '/strip/BassSynth/AM%20pitchshifter/Pitch%20shift/unscaled',  	lambda ev: 1 - (abs(ev.value) / (8191.0)) * 0.75),
]  >> Discard()

samples_mute = Filter(NOTE) >> [
    KeyFilter(notes=['f2','c3','g3']) >> Filter(NOTEON) >> [
        SendOSC(samplesmainport, '/strip/SamplesMain/Gain/Mute', 1.0)
    ],
    KeyFilter(notes=['f2','c3','g3']) >> Filter(NOTEOFF) >> [
        SendOSC(samplesmainport, '/strip/SamplesMain/Gain/Mute', 0.0)
    ],
]

bass_and_samples_mute = Filter(NOTE) >> [
    KeyFilter(notes=['f2','c3','g3']) >> Filter(NOTEON) >> [
        SendOSC(samplesmainport, '/strip/SamplesMain/Gain/Mute', 1.0)
        SendOSC(bassmainport, '/strip/BassMain/Gain/Mute', 1.0)
    ],
    KeyFilter(notes=['f2','c3','g3']) >> Filter(NOTEOFF) >> [
        SendOSC(samplesmainport, '/strip/SamplesMain/Gain/Mute', 0.0)
        SendOSC(bassmainport, '/strip/BassMain/Gain/Mute', 0.0)
    ],
]

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
    },
    control = Filter(PROGRAM) >> SceneSwitch(),
    pre = ~Filter(PROGRAM)
)
