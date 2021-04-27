from mididings import Call
import mididings.engine as _engine
import mididings.setup as _setup
import mididings.misc as _misc
import mididings.event as _event
import mididings.util as _util

import mididings.extra.panic as _panic

import liblo as _liblo

from time import time, sleep

class OSCCustomInterface(object):
    def __init__(self, port=56418):
        self.port = port
        self.timestamp = 0
        self.timeout = 80

    def on_start(self):
        if self.port is not None:
            self.server = _liblo.ServerThread(self.port)
            self.server.register_methods(self)
            self.server.start()

    def on_exit(self):
        if self.port is not None:
            self.server.stop()
            del self.server


    @_liblo.make_method('/pedalBoard/button', 'if')
    @_liblo.make_method('/pedalBoard/button', 'i')
    def button_cb(self, path, args):
        # Anti-rebond
        diff = time() * 1000 - self.timestamp
        if diff < self.timeout and args[0] < 25:
            return
        self.timestamp = time() * 1000

        if len(args) > 1:
            sleep(args[1])

        if _engine.current_subscene() == 9 and args[0] < 12:
         _engine.switch_scene(args[0])
         _engine.switch_subscene(1)
	else:
            if args[0] == 12:
             _engine.switch_subscene(9)
   	    if args[0] < 12 or args[0] > 24:
	     _engine.output_event(_event.ProgramEvent('PBCtrlOut', _util.NoDataOffset(1), args[0]))
            # if _engine.current_subscene() == 8 and args[0] > 17:
            #  _engine.switch_subscene(args[0]-17)

	    else:
                if args[0] == 24:
                    _engine.switch_subscene(8)
                else:
                    _engine.output_event(_event.ProgramEvent('PBCtrlOut', _util.NoDataOffset(1), args[0]))
                 
                # if (args[0] < 15 and args[0] > 12) or (args[0] < 24 and args[0] > 21):
                #     _engine.output_event(_event.ProgramEvent('PBCtrlOut', _util.NoDataOffset(1), args[0]))
                # elif args[0] == 15:
                #     _engine.output_event(_event.NoteOnEvent('WobbleCtrlOut', 1, 'f2', 127))
                # elif args[0] == 16:
                #     _engine.output_event(_event.NoteOnEvent('WobbleCtrlOut', 1, 'c3', 127))
                # elif args[0] == 17:
                #     _engine.output_event(_event.NoteOnEvent('WobbleCtrlOut', 1, 'g3', 127))
                # elif args[0] == 19:
                #     _engine.output_event(_event.NoteOnEvent('WobbleCtrlOut', 1, 'f3', 127))
                # elif args[0] == 20:
                #     _engine.output_event(_event.NoteOnEvent('WobbleCtrlOut', 1, 'c4', 127))
                # elif args[0] == 21:
                #     _engine.output_event(_event.NoteOnEvent('WobbleCtrlOut', 1, 'g4', 127))


    @_liblo.make_method('/pedalBoard/buttonRelease', 'i')
    def buttonRelease_cb(self, path, args):
        if args[0] == 15:
            _engine.output_event(_event.NoteOffEvent('WobbleCtrlOut', 1, 'f2', 0))
        elif args[0] == 16:
            _engine.output_event(_event.NoteOffEvent('WobbleCtrlOut', 1, 'c3', 0))
        elif args[0] == 17:
            _engine.output_event(_event.NoteOffEvent('WobbleCtrlOut', 1, 'g3', 0))
        elif args[0] == 19:
            _engine.output_event(_event.NoteOffEvent('WobbleCtrlOut', 1, 'f3', 0))
        elif args[0] == 20:
            _engine.output_event(_event.NoteOffEvent('WobbleCtrlOut', 1, 'c4', 0))
        elif args[0] == 21:
            _engine.output_event(_event.NoteOffEvent('WobbleCtrlOut', 1, 'g4', 0))
