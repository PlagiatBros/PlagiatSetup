# coding=utf8
from mididings import *
from mididings.extra.osc import OSCInterface
from mididings.extra.inotify import AutoRestart
from utils import OSCCustomInterface
from ports import *


config(
	backend='jack',
	client_name='CMEKeyBoardRoutes',
	out_ports=['CMEOutBass', 'CMEOutTreble', 'CMEOutRhodes'],
	in_ports=['CMEIn']
)


hook(
    OSCInterface(cmeinport, cmeoutport), # "osc.udp://CtrlOrl:56423"),
    AutoRestart()
)

cmeevents = ~Filter(CTRL)


zynbass1 = ~Filter(CTRL) >> Output('CMEOutBass', 1)
zynbass2 = ~Filter(CTRL) >> Output('CMEOutBass', 2)
zynbass3 = ~Filter(CTRL) >> Output('CMEOutBass', 3)
zynbass4 = ~Filter(CTRL) >> Output('CMEOutBass', 4)
zynbass5 = ~Filter(CTRL) >> Output('CMEOutBass', 5)
zynbass6 = ~Filter(CTRL) >> Output('CMEOutBass', 6)
zynbass7 = ~Filter(CTRL) >> Output('CMEOutBass', 7)

zyntreble1 = [
    ~Filter(CTRL) >> Output('CMEOutTreble', 1),

]

zyntreble2 = ~Filter(CTRL) >> Output('CMEOutTreble', 2)

zynrhodes1 = ~Filter(CTRL) >> Output('CMEOutRhodes', 1)

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
    },
    control = Filter(PROGRAM) >> SceneSwitch(),
    pre = ~Filter(PROGRAM)
)
