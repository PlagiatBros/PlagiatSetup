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
	in_ports=['BassWobbleCtrlIn']
)

sltemposerver = SLTempoServer(18000, '127.0.0.1:' + str(slport))

hook(
    AutoRestart(),
    sltemposerver
)


def wobbleRythm(denom):
    global tempo
    def wobble(ev):
        param = (log10((tempo/60.)*denom) + 1.5) / 3
        sltemposerver.send('osc.udp://127.0.0.1:%i' % bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/LFO%20Rate/unscaled', param)
        sltemposerver.send('osc.udp://127.0.0.1:%i' % bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/Max%20Freq/unscaled', 1.0)
        sltemposerver.send('osc.udp://127.0.0.1:%i' % samplesmainport, '/strip/Keyboards/Gain/Mute', 1.0)

    return wobble

run([

    Filter(PITCHBEND) >> [
        SendOSC(bassmainport, '/strip/BassWobblePost/AM%20pitchshifter/Pitch%20shift/unscaled', lambda ev: max(ev.value, 0) / (8191.0/3) + 1) >> Discard(),
        SendOSC(bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/Freq/unscaled', lambda ev: abs(ev.value) / (8191.0) / 10 + 0.25)  >> Discard(),
        SendOSC(bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/Freq/unscaled', lambda ev: abs(ev.value) / (8191.0) / 10 + 0.25)  >> Discard(),
    ],

    Filter(NOTEON) >> [
        KeyFilter('f2') >> [
            Call(wobbleRythm(1)),
            SendOSC(bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/Freq/unscaled', 0.35),
        ] >> Discard(),
        KeyFilter('c3') >>  [
            Call(wobbleRythm(3/2.)),
            SendOSC(bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/Freq/unscaled', 0.35),
        ] >> Discard(),
        KeyFilter('g3') >>  [
            Call(wobbleRythm(3)),
            SendOSC(bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/Freq/unscaled', 0.35),
        ] >> Discard(),
    ],

    Filter(NOTEOFF) >> KeyFilter(notes=['f2', 'c3', 'g3']) >> [
        SendOSC(bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/Max%20Freq/unscaled', 0.0),
        SendOSC(bassmainport, '/strip/BassWobblePost/AM%20pitchshifter/Pitch%20shift/unscaled', 1.0),
        SendOSC(bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/Freq/unscaled', 0.25),
        SendOSC(samplesmainport, '/strip/Keyboards/Gain/Mute', 0.0),
    ] >> Discard()

])
