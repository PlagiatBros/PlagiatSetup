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

hook(
    AutoRestart()
)

monosynth_pitch = [0 for i in range(12)]
manual_pitch = [0, 0, 0]


def set_microtonal(path, args):
    monosynth_pitch = [8192. * t / 2 for t in args]
    print('monosynth pitch: %s' % monosynth_pitch)


server = ServerThread(monosynthpitcherport)
server.add_method('/monosynth/pitch', None, set_microtonal)
server.start()

def applyMicrotonal(ev, input):
    note = ev.note % 12
    port = ev.port
    return [ev, Pitchbend(monosynth_pitch[note] + manual_pitch[port])]

def storePitchwheel(ev, input):
    port = ev.port
    manual_pitch[port] = ev.value
    return Discard()

run(
    Filter(NOTEON) >> Process(applyMicrotonal),
    Filter(PITCHBEND) >> Process(storePitchwheel)
)
