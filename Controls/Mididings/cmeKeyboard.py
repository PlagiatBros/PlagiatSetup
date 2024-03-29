# coding=utf8
from mididings import *
from mididings.extra.osc import OSCInterface
from mididings.extra.inotify import AutoRestart
from mididings.extra.osc import SendOSC
from utils import OSCCustomInterface
from utils import OSCCurentScene
from ports import *
from math import log10
from liblo import send


config(
	backend='jack',
	client_name='CMEKeyBoardRoutes',
	out_ports=['CMEOutBass', 'CMEOutTreble', 'CMEOutRhodes', 'CMEOutTapeutape', 'CMEOutMonoSynth1', 'CMEOutMonoSynth2', 'CMEOutMonoSynth3'],
	in_ports=['CMEIn']
)



hook(
    OSCInterface(cmeinport, cmeoutport), # "osc.udp://CtrlOrl:56423"),
    OSCCurentScene('osc.udp://127.0.0.1:' + str(surfaceorlport), '/cmescene'),
    AutoRestart()
)


active_channel = []

def zyn_enable_filter(*channel):
	global active_channel

	for c in active_channel:
		if c == 21:
			# calf monosynth
			send(keyboardsport, '/strip/DubstepHorn/Calf%20Filter/Frequency/unscaled', 20000.0)
		elif c == 22:
			# calf monosynth
			send(keyboardsport, '/strip/TrapHigh/Calf%20Filter/Frequency/unscaled', 20000.0)
		else:
			# zyn
			send(zyntrebleport, '/part%i/Pefxbypass1' % (c - 1), True)

	active_channel = list(channel)

	for c in active_channel:
		if c < 20:
			# zyn
			send(zyntrebleport, '/part%i/Pefxbypass1' % (c - 1), False)


def zyn_enable_filter_1(e):
	zyn_enable_filter(1)
def zyn_enable_filter_2(e):
	zyn_enable_filter(2)
def zyn_enable_filter_3(e):
	zyn_enable_filter(3,4)
def zyn_enable_filter_5(e):
	zyn_enable_filter(5)
def zyn_enable_filter_6(e):
	zyn_enable_filter(6)
def zyn_enable_filter_11(e):
	zyn_enable_filter(11)
def zyn_enable_filter_21(e):
	zyn_enable_filter(21)
def zyn_enable_filter_22(e):
	zyn_enable_filter(12)


def zyn_set_filter(ev):
	for c in active_channel:
		if c == 21:
			# calf monosynth
			send(keyboardsport, '/strip/DubstepHorn/Calf%20Filter/Frequency/unscaled',  20000. * pow(10, ((-log10(71/20000.))*ev.value) / 127. + log10(71/20000.)))
		elif c == 22:
			# calf monosynth
			send(keyboardsport, '/strip/TrapHigh/Calf%20Filter/Frequency/unscaled',  20000. * pow(10, ((-log10(71/20000.))*ev.value) / 127. + log10(71/20000.)))
		else:
			#zyn
			send(zyntrebleport, '/part%i/partefx1/parameter11' % (c - 1), ev.value) # EQ/filter0/Pfreq

cmeevents = ~Filter(CTRL)


zynbass1 = Transpose(-12) >> ~Filter(CTRL) >> Output('CMEOutBass', 1)
zynbass2 = Transpose(-12) >> ~Filter(CTRL) >> Output('CMEOutBass', 2)
zynbass3 = Transpose(-12) >> ~Filter(CTRL) >> Output('CMEOutBass', 3)
zynbass4 = Transpose(-12) >> ~Filter(CTRL) >> Output('CMEOutBass', 4)
zynbass5 = Transpose(-12) >> ~Filter(CTRL) >>[
    Output('CMEOutBass', 5),
    Output('CMEOutBass', 1),
    ]
zynbass6 = Transpose(-12) >> ~Filter(CTRL) >> Output('CMEOutBass', 6)
zynbass7 = Transpose(-12) >> ~Filter(CTRL) >> Output('CMEOutBass', 7)

zyntreble1 = [
    Init([
	Call(zyn_enable_filter_1)
    ]),
	Transpose(-12) >> [
	    [
	        ~Filter(CTRL),
	        CtrlFilter(1),
	        CtrlFilter(64)
	        ] >> Output('CMEOutTreble', 1),

	]
]

zyntreble1b = [
    Init([
	Call(zyn_enable_filter_5)
    ]),
	Transpose(-12) >> [
	    [
	        ~Filter(CTRL),
	        CtrlFilter(1),
	        CtrlFilter(64)
	        ] >> Output('CMEOutTreble', 5),

	]
]


zyntreble2 = [
    Init([
	Call(zyn_enable_filter_2)
    ]),
	Transpose(-12) >> [
	    [
	        ~Filter(CTRL),
	        CtrlFilter(1),
	        CtrlFilter(64)
	        ] >> Output('CMEOutTreble', 2)
	]
]

zyntreble3 = [
    Init([
	Call(zyn_enable_filter_3)
    ]),
	Transpose(-12) >> [
	    [
	        ~Filter(CTRL),
	        CtrlFilter(1),
	        CtrlFilter(64)
	        ] >> Output('CMEOutTreble', 3)
	]
]

zyntrebleGMandela = Transpose(-12) >> ~Filter(CTRL) >> [
    KeyFilter(notes=['g2','g#2','a#2','g3','g#3','a#3','g3','g#3','a#3','g4','g#4','a#4']),
    ~KeyFilter(notes=['g2','g#2','a#2','g3','g#3','a#3','g3','g#3','a#3','g4','g#4','a#4']) >> [
        KeyFilter('c2','b2') >> Key('g2'),
        KeyFilter('c3','b3') >> Key('g3'),
        KeyFilter('c4','b4') >> Key('g4'),
        KeyFilter('c5','b5') >> Key('g5'),
    ],
] >> Output('CMEOutTreble', 1)

zyntreble4 = [ #bombarde
    Init([
	Call(zyn_enable_filter_6)
    ]),

	Transpose(-12) >> [
	    [
	        ~Filter(CTRL),
	        CtrlFilter(1),
	        CtrlFilter(64)
	        ] >> Output('CMEOutTreble', 6)
	]
]

zyndre = [ #bombarde
    Init([
	Call(zyn_enable_filter_11)
    ]),

	Transpose(-12) >> [
	    [
	        ~Filter(CTRL),
	        CtrlFilter(1),
	        CtrlFilter(64)
	        ] >> Output('CMEOutTreble', 9)
	]
]

monosynth1 = [ # trap bass

	Transpose(-12) >> [
	    [
	        ~Filter(CTRL),
	        CtrlFilter(1),
	        CtrlFilter(64)
	        ] >> Output('CMEOutMonoSynth1', 1)
	]
]

monosynth2 = [ # horny horn
    Init([
	Call(zyn_enable_filter_21)
    ]),

	~Filter(PITCHBEND) >> Transpose(-12) >> [
	    [
	        ~Filter(CTRL),
	        CtrlFilter(1),
	        CtrlFilter(64),
	        ] >> Output('CMEOutMonoSynth2', 1),
	],
        Filter(PITCHBEND) >> [
            ChannelFilter(1) >> Output('CMEOutMonoSynth2', 1),
            ChannelFilter(2) >> Output('CMEOutMonoSynth2', 2)
            ]
]

monosynth3 = [ # trap so high
    Init([
	Call(zyn_enable_filter_22)
    ]),

	Transpose(-12) >> [
	    [
	        ~Filter(CTRL),
	        CtrlFilter(1),
	        CtrlFilter(64),
	        ] >> Output('CMEOutMonoSynth3', 1),
	]
]


zynrhodes1 = Transpose(-12) >> Output('CMEOutRhodes', 1)


tapeutape1 = ~Filter(CTRL) >> Output('CMEOutTapeutape', 1)
tapeutape16 = ~Filter(CTRL) >> Output('CMEOutTapeutape', 16)

gatecancel = [
    SendOSC(vxorlpreport, '/strip/VxORLGars/Gate/Threshold%20(dB)/unscaled', lambda ev: -ev.value/127. * 54.0 - 48),
    SendOSC(vxorlpreport, '/strip/VxORLMeuf/Gate/Threshold%20(dB)/unscaled', lambda ev: -ev.value/127. * 54.0 - 48),
    ] >> Discard()



def glitch(ev):
		cc  = ev.ctrl
		val = 1.0 * ev.value

		glitch_state = [
			float(val > 0), # active
			val / 127, # strength
			val / 127, # noise
			0.0, # hue
			1.0, # saturation
			1.0, # value
			1.0, # alpha
			0.0, # invert
		]

		send(lightseqport, '/Lightseq/Scene/Play', 'glitch_timeout')
		for port in [rpijardinport, rpicourport]:
			send(port, '/pyta/post_process/set_all', *glitch_state)

run(
    scenes = {
        1: 	Scene("ZynBass 1", zynbass1),
        2: 	Scene("ZynBass 2", zynbass2),
        3: 	Scene("ZynBass 3", zynbass3),
        4: 	Scene("ZynBass 4", zynbass4),
        5: 	Scene("ZynBass 5", zynbass5),
        6: 	Scene("ZynBass 6", zynbass6),
        7: 	Scene("ZynBass 7", zynbass7),
        8: 	Scene("ZynTreble 1", zyntreble1),
        9: 	Scene("ZynTreble 2", zyntreble2),
        10:	Scene("ZynRhodes 1", zynrhodes1),
        11:	Scene("Tapeutape 1", tapeutape1),
        12: Scene("ZynTreble 3", zyntreble3),
        13: Scene("zyntrebleGMandela", zyntrebleGMandela),
		14: Scene("ZynTreble 1b", zyntreble1b),
		15: Scene("BOMBARDE", zyntreble4),
		16: Scene("Trap Bass mono", monosynth1),
		17: Scene("Dubstep Horn mono", monosynth2),
		18: Scene("Trap High mono", monosynth3),
		19: Scene("DRE", zyndre),
    },
    control = [
        Filter(CTRL) >> [
            CtrlFilter(2, 7) >>  [
				Call(zyn_set_filter),
				# SendOSC(samplesmainport, '/strip/Keyboards/Calf%20Filter/Frequency/unscaled', lambda ev: 20000. * pow(10, ((-log10(71/20000.))*ev.value) / 127. + log10(71/20000.))),
				SendOSC(surfaceorlport, '/zyn/filter', lambda ev: ev.value),
				],
            CtrlFilter(3) >>  [
				SendOSC(samplesmainport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled', lambda ev: 20000. * pow(10, ((-log10(71/20000.))*ev.value) / 127. + log10(71/20000.))),
				SendOSC(surfaceorlport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled', lambda ev: 20000. * pow(10, ((-log10(71/20000.))*ev.value) / 127. + log10(71/20000.))),
				],
            CtrlFilter(4) >>  [
				SendOSC(samplesmainport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled', lambda ev: 20000. * pow(10, ((-log10(71/20000.))*ev.value) / 127. + log10(71/20000.))),
				SendOSC(samplesmainport, '/strip/Keyboards/Calf%20Filter/Frequency/unscaled', lambda ev: 20000. * pow(10, ((-log10(71/20000.))*ev.value) / 127. + log10(71/20000.))),
				SendOSC(surfaceorlport, '/strip/Keyboards/Calf%20Filter/Frequency/unscaled', lambda ev: 20000. * pow(10, ((-log10(71/20000.))*ev.value) / 127. + log10(71/20000.))),
				SendOSC(surfaceorlport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled', lambda ev: 20000. * pow(10, ((-log10(71/20000.))*ev.value) / 127. + log10(71/20000.))),
				],
            # CtrlFilter(75) >> gatecancel,
            CtrlFilter(1) >> Call(glitch),
        ] >> Discard(),
        Filter(CTRL) >> [
            CtrlFilter(107) >> CtrlValueSplit(64, NoteOff(60), [NoteOff(60), NoteOn(60, 127)]) >> tapeutape16,
            CtrlFilter(108) >> CtrlValueSplit(64, NoteOff(61), [NoteOff(61), NoteOn(61, 127)]) >> tapeutape16,
            CtrlFilter(109) >> CtrlValueSplit(64, NoteOff(62), [NoteOff(62), NoteOn(62, 127)]) >> tapeutape16,
            CtrlFilter(80) >> CtrlValueSplit(64, NoteOff(63), [NoteOff(63), NoteOn(63, 127)]) >> tapeutape16,
            CtrlFilter(16) >> CtrlValueSplit(64, NoteOff(59), [NoteOff(59), NoteOn(59, 127)]) >> tapeutape1,
            # CtrlFilter(18) >> CtrlValueSplit(64, NoteOff(58), [NoteOff(58), NoteOn(58, 127)]) >> tapeutape1,
            CtrlFilter(18) >> [
				CtrlValueSplit(64, NoteOff(57), [NoteOff(57), NoteOn(57, 127)]) >> tapeutape1,
				CtrlValueFilter(127) >> [
					SendOSC(lightseqport, "/Lightseq/Scene/Play", "wholeworld_intro_respect"),
				] >> Discard()
			]
        ],
        Filter(PROGRAM) >> SceneSwitch(),
        ],
    pre = ~Filter(PROGRAM)
)
