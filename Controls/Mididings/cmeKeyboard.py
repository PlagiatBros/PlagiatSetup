# coding=utf8
from mididings import *
from mididings.extra.osc import OSCInterface
from mididings.extra.inotify import AutoRestart
from mididings.extra.osc import SendOSC
from utils import OSCCustomInterface
from ports import *
from math import log10


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

gatecancel = [
    SendOSC(vxorlpreport, '/strip/VxORLGars/Gate/Threshold%20(dB)/unscaled', lambda ev: -ev.value/127. * 54.0 - 48),
    SendOSC(vxorlpreport, '/strip/VxORLMeuf/Gate/Threshold%20(dB)/unscaled', lambda ev: -ev.value/127. * 54.0 - 48),
    ] >> Discard()



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
            CtrlFilter(75) >> gatecancel
        ] >> Discard(),
        Filter(PROGRAM) >> SceneSwitch(),
        ],
    pre = ~Filter(PROGRAM)
)
