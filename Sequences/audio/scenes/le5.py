import sys
sys.path.append("../Controls/Mididings/")

from ports import *


def le5_refrain_cutdown_close(sequencer, timer):
#    timer.wait(.75, 'bites')
    sequencer.animate([samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled'], 1, .25, 0.5, 'beat', framerate=50)
    sequencer.animate([vxmainport, '/strip/VxORLMain/AM%20pitchshifter/Pitch%20shift/unscaled'], 1, .25, 0.5, 'beat', framerate=50)
    sequencer.animate([vxmainport, '/strip/VxJeannotMain/AM%20pitchshifter/Pitch%20shift/unscaled'], 1, .25, 0.5, 'beat', framerate=50)
    sequencer.animate([bassmainport, '/strip/BassMain/AM%20pitchshifter/Pitch%20shift/unscaled'], 1, .25, 0.5, 'beat', framerate=50)
    timer.wait(.1, 'bites')
    sequencer.send(samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)
    sequencer.send(vxmainport, '/strip/VxJeannotMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)
    sequencer.send(vxmainport, '/strip/VxORLMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)
    sequencer.send(bassmainport, '/strip/BassMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)
