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
	out_ports=['Mk2OutBass', 'Mk2OutTreble', 'Mk2OutRhodes', 'Mk2OutTapeutape'],
	in_ports=['Mk2In']
)


hook(
    OSCInterface(mk2inport, mk2outport), # "osc.udp://CtrlOrl:56423"),
    AutoRestart()
)


server = ServerThread(18000)
server.start()
# server.send('osc.udp://127.0.0.1:' + slport)
ping = False
tempo = 120

def tempo(path, *args):
    global tempo, ping
    if ping is False:
        ping = True
    tempo = args[0][2]

server.add_method('/tempo', None, tempo)

while ping is False:
    server.send('osc.udp://127.0.0.1:%i' % slport, '/get', 'tempo', 'osc.udp://127.0.0.1:18000', '/tempo')
    sleep(0.1)

server.send('osc.udp://127.0.0.1:%i' % slport, '/register_update', 'tempo', 'osc.udp://127.0.0.1:18000', '/tempo')


def wobbleRythm(denom):
    global tempo
    def wobble(ev):
        param = (log10((tempo/60.)*denom) + 1.5) / 3
        server.send('osc.udp://127.0.0.1:%i' % bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/LFO%20Rate/unscaled', param)
        server.send('osc.udp://127.0.0.1:%i' % bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/Max%20Freq/unscaled', 1.0)
        server.send('osc.udp://127.0.0.1:%i' % samplesmainport, '/strip/Keyboards/Gain/Mute', 1.0)

    return wobble


basswobblectrl = [
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
    ]


run(
    scenes = {
        1: 	Scene("BassWobbleCtrl", basswobblectrl),
    },
    control = Filter(PROGRAM) >> SceneSwitch(),
    pre = ~Filter(PROGRAM)
)
