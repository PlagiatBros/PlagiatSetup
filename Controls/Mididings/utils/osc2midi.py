#!/usr/bin/env python
#encoding: utf-8

"""
Midi <> OSC generic router
"""

import mididings as midiServer
from mididings.engine import output_event
from mididings.event import *
from liblo import ServerThread, make_method


class osc2MidiRouter(ServerThread):

    def __init__(self, name='osc2midi', midi='jack', port=9999, target=None):

        ServerThread.__init__(self, port)

        self.events = {
            'CTRL': CtrlEvent,
            'NOTEON': NoteOnEvent,
            'NOTEOFF': NoteOffEvent,
            'PROGRAM': ProgramEvent,
            'PITCHBEND': PitchbendEvent,
            'AFTERTOUCH': AftertouchEvent,
            'SYSEX': SysExEvent
        }
        self.eventTypes = []

        self.name = name
        self.midi = midi
        self.midiPorts = {
            'in' : [name + '_in'],
            'out': [name + '_out']
        }

        if type(target) == int:
            self.target = '127.0.0.1:' + str(target)
        elif type(target) == str:
            self.target = target
        else:
            self.target = None

        midiServer.config(
            backend = self.midi,
            client_name = self.name,
            in_ports = self.midiPorts['in'],
            out_ports = self.midiPorts['out']
        )

    def start(self):

        ServerThread.start(self)

        midiServer.run(midiServer.Call(self.processMIDI))

    def stop(self):

        ServerThread.stop(self)

        midiServer.quit()


    @make_method(None, None)
    def processOSC(self, path, *args):

        s = path.upper().split('/')
        if s[1] == 'MIDI':

            mtype = s[2]

            if self.events.has_key(mtype):
                output_event(self.events[mtype](self.midiPorts['out'][0], *args[0]))

    def processMIDI(self, event):
        mtype = str(event.type)
        if self.events.has_key(mtype):

            args = []

            if mtype == 'CTRL':
                args.append(event.channel)
                args.append(event.ctrl)
                args.append(event.value)
            elif mtype == 'NOTEON' or mtype == 'NOTEOFF':
                args.append(event.channel)
                args.append(event.note)
                args.append(event.velocity)
            elif mtype == 'PROGRAM':
                args.append(event.channel)
                args.append(event.program)
            elif mtype == 'PITCHBEND':
                args.append(event.channel)
                args.append(event.value)
            elif mtype == 'AFTERTOUCH':
                args.append(event.channel)
                args.append(event.value)
            elif mtype == 'SYSEX':
                args.append(event.sysex)

            self.send('osc.upd://' + target, '/midi/' + mtype.lower(), *args)
