# coding=utf8
from mididings import *
from mididings.extra.inotify import AutoRestart
from mididings.extra.osc import SendOSC
from utils import SLTempoServer
from ports import *
from math import log10


config(
	backend='jack',
	client_name='BassWobbleCtrl',
	in_ports=['BassWobbleCtrlIn'],
	out_ports=['WobbleCtrlOut'],
)

sltemposerver = SLTempoServer(18000, '127.0.0.1:' + str(slport))

hook(
    AutoRestart(),
    sltemposerver
)


def wobbleRythm(denom):
    def wobble(ev):
        param = (log10((sltemposerver.tempo/60.)*denom) + 1.5) / 3
        sltemposerver.send('osc.udp://127.0.0.1:%i' % bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/LFO%20Rate/unscaled', param)
        sltemposerver.send('osc.udp://127.0.0.1:%i' % bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/Max%20Freq/unscaled', 1.0)
        # sltemposerver.send('osc.udp://127.0.0.1:%i' % samplesmainport, '/strip/Keyboards/Gain/Mute', 1.0)
        # print 'hi'
    return wobble

run([

    Filter(PITCHBEND) >> [
        SendOSC(bassmainport, '/strip/BassWobblePost/AM%20pitchshifter/Pitch%20shift/unscaled', lambda ev: max(ev.value, 0) / (8191.0/3) + 1) >> Discard(),
        SendOSC(bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/Freq/unscaled', lambda ev: abs(ev.value) / (8191.0) / 10 + 0.25)  >> Discard(),
        SendOSC(bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/Freq/unscaled', lambda ev: abs(ev.value) / (8191.0) / 10 + 0.25)  >> Discard(),
    ],

    Filter(NOTEON) >> [
        KeyFilter('f2') >> [[
            Call(wobbleRythm(1)),
            SendOSC(bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/Freq/unscaled', 0.35),
        ] >> Discard(), Ctrl(1, 1) >> Output('WobbleCtrlOut', 1)],

		KeyFilter('c3') >>  [[
            Call(wobbleRythm(3/2.)),
            SendOSC(bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/Freq/unscaled', 0.35),
        ] >> Discard(), Ctrl(1, 32) >> Output('WobbleCtrlOut', 1)],

		KeyFilter('a3') >>  [[
            Call(wobbleRythm(3)),
            SendOSC(bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/Freq/unscaled', 0.35),
        ] >> Discard(), Ctrl(1, 3) >> Output('WobbleCtrlOut', 1)],

		KeyFilter('f3') >> [[
            Call(wobbleRythm(4)),
            SendOSC(bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/Freq/unscaled', 0.35),
        ] >> Discard(), Ctrl(1, 4) >> Output('WobbleCtrlOut', 1)],

		KeyFilter('c4') >>  [[
            Call(wobbleRythm(4)),
            SendOSC(bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/Freq/unscaled', 0.35),
        ] >> Discard(), Ctrl(4, 127) >> Output('WobbleCtrlOut', 1)],

		KeyFilter('a4') >>  [[
            Call(wobbleRythm(6)),
            SendOSC(bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/Freq/unscaled', 0.35),
        ] >> Discard(), Ctrl(1, 6) >> Output('WobbleCtrlOut', 1)],
    ],

    Filter(NOTEOFF) >> KeyFilter(notes=['f2', 'c3', 'a3', 'f3', 'c4', 'a4']) >> [[
        SendOSC(bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/Max%20Freq/unscaled', 0.0),
        SendOSC(bassmainport, '/strip/BassWobblePost/AM%20pitchshifter/Pitch%20shift/unscaled', 1.0),
        SendOSC(bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/Freq/unscaled', 0.25),
        # SendOSC(samplesmainport, '/strip/Keyboards/Gain/Mute', 0.0),
    ] >> Discard(), Ctrl(1, 0) >> Output('WobbleCtrlOut', 1)]

])
