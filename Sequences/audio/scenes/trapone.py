import sys
sys.path.append("../Controls/Mididings/")

from ports import *

def trapone_intro(sequencer, timer):
    timer.wait(2.5, 'bites')
    sequencer.animate([vxmainport, '/strip/VxJeannotMain/AM%20pitchshifter/Pitch%20shift/unscaled'], 1, .25, 0.45, 'beat', framerate=50)
    sequencer.animate([vxmainport, '/strip/VxORLMain/AM%20pitchshifter/Pitch%20shift/unscaled'], 1, .25, 0.45, 'beat', framerate=50)
    timer.wait(1.5, 'bites')
    sequencer.send(vxmainport, '/strip/VxJeannotMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)
    sequencer.send(vxmainport, '/strip/VxORLMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)
    sequencer.send(56418, '/pedalBoard/button', 4)

def trapone_altern_couplet(sequencer, timer):
    timer.wait(8, 'bites')
    sequencer.send(56418, '/pedalBoard/button', 4)

def trapone_altern_refrain(sequencer, timer):
    timer.wait(8, 'bites')
    sequencer.send(56418, '/pedalBoard/button', 5)

def trapone_altern_final(sequencer, timer):
    timer.wait(8, 'bites')
    sequencer.send(56418, '/pedalBoard/button', 7)
