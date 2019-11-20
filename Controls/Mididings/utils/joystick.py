#encoding: utf-8

import os, struct, array, signal, select
from fcntl import ioctl
from time import sleep
from threading import Thread

axis_names = {
    0x00 : 'x',
    0x01 : 'y',
    0x02 : 'z',
    0x03 : 'rx',
    0x04 : 'ry',
    0x05 : 'rz',
    0x06 : 'trottle',
    0x07 : 'rudder',
    0x08 : 'wheel',
    0x09 : 'gas',
    0x0a : 'brake',
    0x10 : 'hat0x',
    0x11 : 'hat0y',
    0x12 : 'hat1x',
    0x13 : 'hat1y',
    0x14 : 'hat2x',
    0x15 : 'hat2y',
    0x16 : 'hat3x',
    0x17 : 'hat3y',
    0x18 : 'pressure',
    0x19 : 'distance',
    0x1a : 'tilt_x',
    0x1b : 'tilt_y',
    0x1c : 'tool_width',
    0x20 : 'volume',
    0x28 : 'misc',
}

button_names = {
    0x120 : 'trigger',
    0x121 : 'thumb',
    0x122 : 'thumb2',
    0x123 : 'top',
    0x124 : 'top2',
    0x125 : 'pinkie',
    0x126 : 'base',
    0x127 : 'base2',
    0x128 : 'base3',
    0x129 : 'base4',
    0x12a : 'base5',
    0x12b : 'base6',
    0x12f : 'dead',
    0x130 : 'a',
    0x131 : 'b',
    0x132 : 'c',
    0x133 : 'x',
    0x134 : 'y',
    0x135 : 'z',
    0x136 : 'tl',
    0x137 : 'tr',
    0x138 : 'tl2',
    0x139 : 'tr2',
    0x13a : 'select',
    0x13b : 'start',
    0x13c : 'mode',
    0x13d : 'thumbl',
    0x13e : 'thumbr',

    0x220 : 'dpad_up',
    0x221 : 'dpad_down',
    0x222 : 'dpad_left',
    0x223 : 'dpad_right',

    # XBox 360 controller uses these codes.
    0x2c0 : 'dpad_left',
    0x2c1 : 'dpad_right',
    0x2c2 : 'dpad_up',
    0x2c3 : 'dpad_down',
}

class Joystick():

    def __init__(self, dev=0, callback=None):

        self.path = '/dev/input/js' + str(dev)
        self.axis_map = []
        self.button_map = []
        self.callback = callback
        self.error = False
        self.quit = False
        self.dev = None
        self.name = ''
        self.state = {
            'button': {},
            'axis': {}
        }

        try:
            self.connect()
        except IOError as e:
            print('ERROR: Joystick device %s not found.' % (self.path))
            self.connected = False

    def set_callback(self, callback):

        self.callback = callback

    def stop(self):

        self.quit = True

    def connect(self):

        self.dev = open(self.path, 'rb')

        self.axis_map = []
        self.button_map = []

        # Get the device name.
        buf = array.array('B', [0] * 64)
        ioctl(self.dev, 0x80006a13 + (0x10000 * len(buf)), buf) # JSIOCGNAME(len)
        self.name = buf.tostring().rstrip(b'\x00').decode('utf-8')

        # Get number of axes and buttons.
        buf = array.array('B', [0])
        ioctl(self.dev, 0x80016a11, buf) # JSIOCGAXES
        num_axes = buf[0]

        buf = array.array('B', [0])
        ioctl(self.dev, 0x80016a12, buf) # JSIOCGBUTTONS
        num_buttons = buf[0]

        # Get the axis map.
        buf = array.array('B', [0] * 0x40)
        ioctl(self.dev, 0x80406a32, buf) # JSIOCGAXMAP
        for axis in buf[:num_axes]:
            axis_name = axis_names.get(axis, 'unknown(0x%02x)' % axis)
            self.axis_map.append(axis_name)

        # Get the button map.
        buf = array.array('H', [0] * 200)
        ioctl(self.dev, 0x80406a34, buf) # JSIOCGBTNMAP
        for btn in buf[:num_buttons]:
            btn_name = button_names.get(btn, 'unknown(0x%03x)' % btn)
            self.button_map.append(btn_name)

        print('INFO: Joystick device %s (%s) connected.' % (self.path, self.name))
        self.connected = True

        if self.callback:
            self.callback('status', 'connected', 1)

    def disconnect(self):

        print('ERROR: Joystick device %s (%s) disconnected.' % (self.path, self.name))
        self.connected = False

        if self.callback:
            self.callback('status', 'connected', 0)


    def run(self):

        while not self.quit:

            if self.connected:
                r, w, e = select.select([self.dev], [], [], 0)
                if not self.dev in r:
                    sleep(0.001)
                    continue
            else:
                sleep(0.001)


            try:
                if not self.connected:
                    self.connect()
                evbuf = self.dev.read(8)
            except IOError as e:
                evbuf = None
                if self.connected:
                    self.disconnect()

            if evbuf:

                time, value, evtype, number = struct.unpack('IhBB', evbuf)

                type = None
                name = None

                if evtype & 0x01:
                    type = 'button'
                    name = self.button_map[number]
                elif evtype & 0x02:
                    type = 'axis'
                    name = self.axis_map[number]
                    value = value / 32767.0

                if type and name:

                    state = self.state[type]

                    if not name in state or state[name] != value:

                        state[name] = value

                        if self.callback:
                            self.callback(type, name, value)

    # mididings hook
    def on_start(self):
        t = Thread(target=self.run, args=[])
        t.start()

    def on_exit(self):
        self.stop()
