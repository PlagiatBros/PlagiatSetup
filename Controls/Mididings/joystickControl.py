# coding=utf8
from utils import Joystick
from ports import *

import mididings
from mididings.engine import output_event
from mididings.event import PitchbendEvent, NoteOnEvent, CtrlEvent
from mididings.extra.inotify import AutoRestart
from liblo import send
import subprocess



mididings.config(
    backend = 'jack',
    client_name = 'Joystick2Pitchbend',
    out_ports = ['out']
)

def process(type, name, value):
    print('%s/%s: %s' % (type, name, value))
    if type == 'button' and value == 1:
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
        elif name == 'tr':
            subprocess.call(['i3-msg', 'scratchpad', 'show'])
        elif name == 'tr2':
            subprocess.call(['i3-msg', 'focus', 'right'])
        elif name == 'tl2':
            subprocess.call(['i3-msg', 'focus', 'left'])



    elif type == 'axis':
        if name == 'x':
            output_event(PitchbendEvent('out', 2, int(value * 8192)))
        elif name == 'rx':
            output_event(CtrlEvent('out', 1, 1, int(100 * abs(value))))

    elif type == 'status':
        if name == 'connected' and value == 0:
            process('axis', 'x', 0)
            process('axis', 'rx', 0)

mididings.hook(
    Joystick(dev=0, callback=process),
    AutoRestart()
)

mididings.run(mididings.Pass())
