import sys
sys.path.append("../Controls/Mididings/")

from ports import *

def dafist_outro_filter_close(sequencer, timer):

    sequencer.animate([samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled'], 1, .25, 0.75, 'beat', framerate=50)
    sequencer.animate([samplesmainport, '/strip/Keyboards/AM%20pitchshifter/Pitch%20shift/unscaled'], 1, .25, 0.75, 'beat', framerate=50)
    sequencer.send(slport, '/sl/7/hit', 'mute_on')
    timer.wait( 1, 'bites')

    timer.wait(  1, 'bites')

    timer.wait(.25, 'bites')
    sequencer.send(slport, '/sl/7/hit', 'mute_off')
    sequencer.animate([samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled'], .25, 1, 0.75, 'beat', framerate=50)
    sequencer.animate([samplesmainport, '/strip/Keyboards/AM%20pitchshifter/Pitch%20shift/unscaled'], .25, 1, 0.75, 'beat', framerate=50)

def dafist_filter_reset(sequencer, timer):
    sequencer.send(slport, '/sl/7/hit', 'mute_off')
    sequencer.send(samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)
    sequencer.send(samplesmainport, '/strip/Keyboards/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)
