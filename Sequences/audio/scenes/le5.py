import sys
sys.path.append("../Controls/Mididings/")

from ports import *


def le5_refrain_cutdown_close(sequencer, timer):
    t = timer.time()

    sequencer.animate([samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled'], 1, .25, 1, 'beat', framerate=50, timestamp=t)
    sequencer.animate([vxmainport, '/strip/VxORLMain/AM%20pitchshifter/Pitch%20shift/unscaled'], 1, .25, 1, 'beat', framerate=50, timestamp=t)
    sequencer.animate([vxmainport, '/strip/VxJeannotMain/AM%20pitchshifter/Pitch%20shift/unscaled'], 1, .25, 1, 'beat', framerate=50, timestamp=t)
    sequencer.animate([bassmainport, '/strip/BassMain/AM%20pitchshifter/Pitch%20shift/unscaled'], 1, .25, 1, 'beat', framerate=50, timestamp=t)

    timer.wait(3, 'bites')

    sequencer.send(samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)
    sequencer.send(vxmainport, '/strip/VxJeannotMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)
    sequencer.send(vxmainport, '/strip/VxORLMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)
    sequencer.send(bassmainport, '/strip/BassMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)
