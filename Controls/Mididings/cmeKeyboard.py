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

from scenes import *

zynbass1 = Output('CMEOutBass', 1)
zynbass2 = Output('CMEOutBass', 2)
zynbass3 = Output('CMEOutBass', 3)
zynbass4 = Output('CMEOutBass', 4)
zynbass5 = Output('CMEOutBass', 5)

zyntreble1 = Output('CMEOutTreble', 1)
zyntreble2 = Output('CMEOutTreble', 2)

zynrhodes1 = Output('CMEOutRhodes', 1)

hook(
    OSCInterface(cmeinport, cmeoutport), # "osc.udp://CtrlOrl:56423"),
    AutoRestart()
)

run(
    scenes = {
        1: 	Scene("ZynBass 1", Filter(NOTE) >> zynbass1),
        2: 	Scene("ZynBass 2", Filter(NOTE) >> zynbass2),
        3: 	Scene("ZynBass 3", Filter(NOTE) >> zynbass3),
        4: 	Scene("ZynBass 4", Filter(NOTE) >> zynbass4),
        5: 	Scene("ZynBass 5", Filter(NOTE) >> zynbass5),
        6: 	Scene("ZynTreble 1", Filter(NOTE) >> zyntreble1),
        7: 	Scene("ZynTreble 2", Filter(NOTE) >> zyntreble2),
        8: 	Scene("ZynRhodes 1", Filter(NOTE) >> zynrhodes1),
    },
    control = Filter(PROGRAM) >> SceneSwitch(),
    pre = ~Filter(PROGRAM)
)
