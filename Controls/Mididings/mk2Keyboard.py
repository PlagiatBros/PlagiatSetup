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
        1: 	Scene("BassWobbleCtrl",
                [
                [Filter(NOTE), Filter(PITCHBEND)] >> Output('Mk2OutWobble', 1),
                CtrlFilter(18) >> SendOSC(bassmainport, '/strip/BassMain/Calf%20Filter/Frequency/unscaled', lambda ev: 20000. * pow(10,((-log10(71/20000.))*ev.value) / 127. + log10(71/20000.))) >> Discard(),
                ]
                      ),
        2: 	Scene("VxDelayCtrl",
                [
                [
                    Filter(NOTEON) >> SendOSC(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 0.0),
                    Filter(NOTEOFF) >> SendOSC(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 1.0),
                    ] >> Discard(),
                CtrlFilter(18) >> SendOSC(bassmainport, '/strip/BassMain/Calf%20Filter/Frequency/unscaled', lambda ev: 20000. * pow(10,((-log10(71/20000.))*ev.value) / 127. + log10(71/20000.))) >> Discard(),
                ]
              ),
        3: Scene("Connasses SACEM samples",
                [
                Filter(NOTEON) >> Output('Mk2OutTapeutape', 1),
                CtrlFilter(18) >> SendOSC(bassmainport, '/strip/BassMain/Calf%20Filter/Frequency/unscaled', lambda ev: 20000. * pow(10,((-log10(71/20000.))*ev.value) / 127. + log10(71/20000.))) >> Discard(),
                ]
              ),

    },
    control = Filter(PROGRAM) >> SceneSwitch(),
    pre = ~Filter(PROGRAM)
)
