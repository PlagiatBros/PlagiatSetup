from mididings import Call
import mididings.engine as _engine
import mididings.setup as _setup
import mididings.misc as _misc
import mididings.event as _event
import mididings.util as _util

import mididings.extra.panic as _panic

import liblo as _liblo

from time import time

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

    # @_liblo.make_method('/Sequencer/Intro', 'i')
    # def intro_cb(self, path, args):
    #     _engine.output_event(_event.NoteOnEvent('PBTapeutape', _util.NoDataOffset(9), 0, int(args[0])))
    #     _engine.output_event(_event.NoteOnEvent('PBTapeutape', _util.NoDataOffset(9), 39, int(args[0])))
    #     _engine.output_event(_event.NoteOnEvent('PBTapeutape', _util.NoDataOffset(9), 38, int(args[0])))
    #     _engine.output_event(_event.NoteOnEvent('PBTapeutape', _util.NoDataOffset(9), 40, int(args[0])))
    #     _engine.output_event(_event.ProgramEvent('PBCtrlOut', _util.NoDataOffset(1), 127))

    # @_liblo.make_method('/Sequencer/Sabra', 'i')
    # def sabra_cb(self, path, args):
    #     _engine.output_event(_event.NoteOnEvent('PBTapeutape', _util.NoDataOffset(9), 23, int(args[0])))
    #     _engine.output_event(_event.NoteOnEvent('PBTapeutape', _util.NoDataOffset(9), 39, int(args[0])))
    #     _engine.output_event(_event.NoteOnEvent('PBTapeutape', _util.NoDataOffset(9), 38, int(args[0])))
    #     _engine.output_event(_event.NoteOnEvent('PBTapeutape', _util.NoDataOffset(9), 40, int(args[0])))
    #     _engine.output_event(_event.NoteOnEvent('PBTapeutape', _util.NoDataOffset(9), 22, int(args[0])))
    #     _engine.output_event(_event.NoteOnEvent('PBTapeutape', _util.NoDataOffset(9), 65, int(args[0])))



    @_liblo.make_method('/pedalBoard/button', 'i')
    def button_cb(self, path, args):
        # Anti-rebond
        diff = time() * 1000 - self.timestamp
        if diff < self.timeout:
            return
        self.timestamp = time() * 1000

        if _engine.current_subscene() == 9 and args[0] < 12:
         _engine.switch_scene(args[0])
         _engine.switch_subscene(1)
         # if args[0] == 1: # Rustine car acte 0 sur screen 14 !!!
         #     _engine.output_event(_event.ProgramEvent('PBseq24', _util.NoDataOffset(1), 127))
         # else:
        #  _engine.output_event(_event.ProgramEvent('PBseq24', _util.NoDataOffset(1), seq24PageMap[args[0]]))
#         _engine.output_event(_event.CtrlEvent('PBTapeutape', _util.NoDataOffset(0), 0, args[0]-1))
	else:
            if args[0] == 12:
             _engine.switch_subscene(9)
   	    if args[0] < 12:
	     _engine.output_event(_event.ProgramEvent('PBCtrlOut', _util.NoDataOffset(1), args[0]))
            if _engine.current_subscene() == 8 and args[0] > 17:
             _engine.switch_subscene(args[0]-17)

	    else:
                if args[0] == 24:
                 _engine.switch_subscene(8)
   	        if args[0] < 24 and args[0] > 12:
                    _engine.output_event(_event.ProgramEvent('PBCtrlOut', _util.NoDataOffset(1), args[0]))
