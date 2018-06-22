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
	client_name='CMEAdapter',
	out_ports=['AdapterOut'],
	in_ports=['AdapterIn']
)


hook(
    AutoRestart()
)

out = Output('AdapterOut', 1)

run([
    Filter(NOTEON) >> [
		KeyFilter(44) >> Program(5),
		KeyFilter(45) >> Program(7),
		KeyFilter(46) >> [Ctrl(16, 127), Ctrl(18, 127)],
		KeyFilter(47) >> [Ctrl(16, 0), Ctrl(18, 0)],
		KeyFilter(48) >> Program(8),
		KeyFilter(49) >> Program(9),
		KeyFilter(50) >> Program(10),
		KeyFilter(51) >> Program(11),

    ],
	Filter(PITCHBEND),
	Filter(CTRL) >> CtrlFilter(4) >> Ctrl(75, EVENT_VALUE),
	Filter(CTRL) >> CtrlFilter(8) >> Ctrl(110, EVENT_VALUE),

] >> out)
