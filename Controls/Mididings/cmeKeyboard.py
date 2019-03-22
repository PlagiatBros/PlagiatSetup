# coding=utf8
from mididings import *
from mididings.extra.osc import OSCInterface
from mididings.extra.inotify import AutoRestart
from mididings.extra.osc import SendOSC
from utils import OSCCustomInterface
from ports import *
from math import log10
from liblo import send


config(
	backend='jack',
	client_name='CMEKeyBoardRoutes',
	out_ports=['CMEOutBass', 'CMEOutTreble', 'CMEOutRhodes', 'CMEOutTapeutape'],
	in_ports=['CMEIn']
)


hook(
    OSCInterface(cmeinport, cmeoutport), # "osc.udp://CtrlOrl:56423"),
    AutoRestart()
)

cmeevents = ~Filter(CTRL)


zynbass1 = Output('CMEOutBass', 1)
zynbass2 = Output('CMEOutBass', 2)
zynbass3 = Output('CMEOutBass', 3)
zynbass4 = Output('CMEOutBass', 4)
zynbass5 = [
    Output('CMEOutBass', 5),
    Output('CMEOutBass', 1),
    ]
zynbass6 = Output('CMEOutBass', 6)
zynbass7 = Output('CMEOutBass', 7)

zyntreble1 = [
    [
        ~Filter(CTRL),
        CtrlFilter(1),
        CtrlFilter(64)
        ] >> Output('CMEOutTreble', 1),

]

zyntreble2 = [
    [
        ~Filter(CTRL),
        CtrlFilter(1),
        CtrlFilter(64)
        ] >> Output('CMEOutTreble', 2)
]

zyntreble3 = [
    [
        ~Filter(CTRL),
        CtrlFilter(1),
        CtrlFilter(64)
        ] >> Output('CMEOutTreble', 3)
]

zyntrebleGMandela = ~Filter(CTRL) >> [
    KeyFilter(notes=['g2','g#2','a#2','g3','g#3','a#3','g3','g#3','a#3','g4','g#4','a#4']),
    ~KeyFilter(notes=['g2','g#2','a#2','g3','g#3','a#3','g3','g#3','a#3','g4','g#4','a#4']) >> [
        KeyFilter('c2','b2') >> Key('g2'),
        KeyFilter('c3','b3') >> Key('g3'),
        KeyFilter('c4','b4') >> Key('g4'),
        KeyFilter('c5','b5') >> Key('g5'),
    ],
] >> Output('CMEOutTreble', 1)

zynrhodes1 = Output('CMEOutRhodes', 1)

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
    },
    control = [
        Filter(CTRL) >> [
            CtrlFilter(110) >>  SendOSC(samplesmainport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled', lambda ev: 20000. * pow(10, ((-log10(71/20000.))*ev.value) / 127. + log10(71/20000.))),
            CtrlFilter(75) >> gatecancel,
            CtrlFilter(1) >> Call(glitch),
        ] >> Discard(),
        Filter(CTRL) >> [
            CtrlFilter(107) >> CtrlValueSplit(64, NoteOff(60), [NoteOff(60), NoteOn(60, 127)]) >> tapeutape16,
            CtrlFilter(108) >> CtrlValueSplit(64, NoteOff(61), [NoteOff(61), NoteOn(61, 127)]) >> tapeutape16,
            CtrlFilter(109) >> CtrlValueSplit(64, NoteOff(62), [NoteOff(62), NoteOn(62, 127)]) >> tapeutape16,
            CtrlFilter(80) >> CtrlValueSplit(64, NoteOff(63), [NoteOff(63), NoteOn(63, 127)]) >> tapeutape16,
            CtrlFilter(16) >> CtrlValueSplit(64, NoteOff(59), [NoteOff(59), NoteOn(59, 127), SendOSC(lightseqport, "/lightseq/scene/play", "intro_respect")]) >> tapeutape1,
            # CtrlFilter(18) >> CtrlValueSplit(64, NoteOff(58), [NoteOff(58), NoteOn(58, 127)]) >> tapeutape1,
            CtrlFilter(18) >> CtrlValueSplit(64, NoteOff(57), [NoteOff(57), NoteOn(57, 127)]) >> tapeutape1,
        ],
        Filter(PROGRAM) >> SceneSwitch(),
        ],
    pre = ~Filter(PROGRAM)
)
