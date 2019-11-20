# coding=utf8
from utils import Joystick

import mididings
from mididings.engine import output_event, active, quit
from mididings.event import PitchbendEvent, NoteOnEvent, CtrlEvent
from mididings.extra.osc import SendOSC

from liblo import send
from ports import *

mididings.config(
    backend = 'jack',
    client_name = 'Joystick2Pitchbend',
    out_ports = ['out']
)

def process(type, name, value):
    # print('%s/%s: %s' % (type, name, value))
    if type == 'button':
        if name == 'a': # X
            send(cmeinport, '/mididings/switch_scene', 8)
        elif name == 'b': # O
            send(cmeinport, '/mididings/switch_scene', 9)
        elif name == 'y': # CARRÉ
            send(cmeinport, '/mididings/switch_scene', 10)
        elif name == 'x': # TRIANGLE
            send(cmeinport, '/mididings/switch_scene', 12)
        elif name == 'dpad_up':
            send(cmeinport, '/mididings/switch_scene', 6)
        elif name == 'dpad_down':
            pass
        elif name == 'dpad_left':
            send(cmeinport, '/mididings/switch_scene', 5)
        elif name == 'dpad_right':
            send(cmeinport, '/mididings/switch_scene', 7)
    elif type == 'axis':
        if name == 'x':
            output_event(PitchbendEvent('out', 1, int(value * 8192)))
        elif name == 'rx':
            output_event(CtrlEvent('out', 1, 1, int(100 * abs(value))))


mididings.hook(
    Joystick(dev=0, callback=process)
)

mididings.run(mididings.Pass())
