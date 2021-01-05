# coding=utf8
from mididings import *
from mididings.event import PitchbendEvent
from mididings.extra.inotify import AutoRestart
from liblo import ServerThread
from mididings.extra.osc import SendOSC

config(
	backend='jack',
	client_name='MonoSynthMicroTonal',
	out_ports=['SynthOut1', 'SynthOut2', 'SynthOut3'],
	in_ports=['SynthIn1', 'SynthIn2', 'SynthIn3']
)

from ports import *

# hook(
#     AutoRestart()
# )

monosynth_pitch =  [0 for i in range(12)]
manual_pitch = [0, 0, 0]
pb_factor = [1/12., 1/12., 1]
note = 0

def set_microtonal(path, args):
    global monosynth_pitch
    monosynth_pitch = [8192. * t / 2 for t in args]
    print('monosynth pitch: %s' % monosynth_pitch)


server = ServerThread(monosynthpitcherport)
server.add_method('/monosynth/pitch', None, set_microtonal)
server.start()

def applyMicrotonal(ev):
    global note

    note = ev.note % 12
    port = ev.port - 1
    #print(int(monosynth_pitch[note] + manual_pitch[port]))
    return [PitchbendEvent(ev.port, ev.channel, int(monosynth_pitch[note] * pb_factor[port] + manual_pitch[port])), ev]

def storePitchwheel(ev):
    port = ev.port - 1
    manual_pitch[port] = ev.value * pb_factor[port]
    if ev.channel != 1:
	ev.value =  int( ev.value * pb_factor[port])
    ev.value +=  int(monosynth_pitch[note] * pb_factor[port])
    return ev

run([
    Filter(NOTEON) >> Process(applyMicrotonal),
    Filter(NOTEOFF),
    Filter(PITCHBEND) >> [
	Process(storePitchwheel),
	ChannelFilter(1) >> SendOSC(5678, '/channel', 1)
	]
])
