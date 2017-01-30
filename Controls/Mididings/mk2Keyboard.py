# coding=utf8
from mididings import *
from mididings.extra.osc import OSCInterface
from mididings.extra.inotify import AutoRestart
from mididings.extra.osc import SendOSC
from utils import OSCCustomInterface
from ports import *
from math import log10

from liblo import ServerThread
from time import sleep


config(
	backend='jack',
	client_name='Mk2KeyBoardRoutes',
	out_ports=['Mk2OutBass', 'Mk2OutTreble', 'Mk2OutRhodes', 'Mk2OutTapeutape', 'Mk2OutWobble'],
	in_ports=['Mk2In']
)


hook(
    OSCInterface(mk2inport, mk2outport),
    AutoRestart()
)

run(
    scenes = {
        1: 	Scene("BassWobbleCtrl", Output('Mk2OutWobble', 1)),
    },
    control = Filter(PROGRAM) >> SceneSwitch(),
    pre = ~Filter(PROGRAM)
)
