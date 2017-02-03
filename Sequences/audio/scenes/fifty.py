import sys
sys.path.append("../Controls/Mididings/")

from ports import *

def fifty_intro(sequencer, timer):
    timer.wait(11, 'bites')
    sequencer.send(slport, '/sl/1/hit', 'record')
    timer.wait(1, 'bite')
    sequencer.send(56418, '/pedalBoard/button', 3)


def fifty_refrain_auto(sequencer, timer):
    timer.wait(12, 'bites')
    sequencer.send(56418, '/pedalBoard/button', 7)


def fifty_refrain_cutdown_close(sequencer, timer):
    timer.wait(.75, 'bites')
    sequencer.animate([samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled'], 1, .25, 0.5, 'beat', framerate=50, blocking=True)
    timer.wait(.5, 'bites')
    sequencer.send(samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)
