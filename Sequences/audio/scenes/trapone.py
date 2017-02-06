import sys
sys.path.append("../Controls/Mididings/")

from ports import *

def trapone_intro(sequencer, timer):
    timer.wait(2, 'bites')
    sequencer.animate([vxmainport, '/strip/VxJeannotMain/AM%20pitchshifter/Pitch%20shift/unscaled'], 1, .25, 0.5, 'beat', framerate=50, blocking=True)
    sequencer.animate([vxmainport, '/strip/VxORLMain/AM%20pitchshifter/Pitch%20shift/unscaled'], 1, .25, 0.5, 'beat', framerate=50, blocking=True)
    timer.wait(2, 'bites')
    sequencer.send(vxmainport, '/strip/VxJeannotMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)
    sequencer.send(vxmainport, '/strip/VxORLMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)
    sequencer.send(56418, '/pedalBoard/button', 4)




