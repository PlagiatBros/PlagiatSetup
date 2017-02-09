# coding=utf8
from mididings import *
from mididings.extra.osc import OSCInterface
from mididings.extra.inotify import AutoRestart
from utils import OSCCustomInterface
from ports import *


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
zynbass5 = Output('CMEOutBass', 5)
zynbass6 = Output('CMEOutBass', 6)
zynbass7 = Output('CMEOutBass', 7)

zyntreble1 = [
    ~Filter(CTRL) >> Output('CMEOutTreble', 1),

]

zyntreble2 = ~Filter(CTRL) >> Output('CMEOutTreble', 2)

zyntreble3 = ~Filter(CTRL) >> Output('CMEOutTreble', 3)

zynrhodes1 = Output('CMEOutRhodes', 1)

tapeutape1 = ~Filter(CTRL) >> Output('CMEOutTapeutape', 1)

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
    },
    control = Filter(PROGRAM) >> SceneSwitch(),
    pre = ~Filter(PROGRAM)
)
