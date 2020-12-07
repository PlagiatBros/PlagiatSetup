# coding=utf8
from mididings import *
from mididings.extra.inotify import AutoRestart
from liblo import ServerThread

config(
	backend='jack',
	client_name='MonoSynthMicroTonal',
	out_ports=['SynthOut1', 'SynthOut2', 'SynthOut3'],
	in_ports=['SynthIn1', 'SynthIn2', 'SynthIn3']
)

from ports import *
from aliases import *

hook(
    AutoRestart()
)

def set_microtonal(path, args):
    monosynth_pitch = [8192. * t / 2 for t in args]
    print('monosynth pitch: %s' % monosynth_pitch)


server = ServerThread(monosynthpitcherport)
server.add_method('/monosynth/pitch', None, set_microtonal)
server.start()

def applyPitch(ev):

    return ev >> Pitchbend(monosynth_pitch[ev.note % 12])

run(
    Filter(NOTEON) >> Process(applyPitch) >> [
        PortFilter('SynthIn1') >> Output('SynthOut1', 1),
        PortFilter('SynthIn2') >> Output('SynthOut2', 1),
        PortFilter('SynthIn3') >> Output('SynthOut3', 1),
    ]
)
