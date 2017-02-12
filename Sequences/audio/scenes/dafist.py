import sys
sys.path.append("../Controls/Mididings/")

from ports import *

def dafist_outro_filter_close(sequencer, timer):
    timer.wait(.25, 'bites')
    sequencer.animate([samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled'], 1, .25, 0.5, 'beat', framerate=50)
    sequencer.send(slport, '/sl/7/hit', 'mute_on')

def dafist_outro_filter_open(sequencer, timer):
    timer.wait(.25, 'bites')
    sequencer.send(slport, '/sl/7/hit', 'mute_off')
    sequencer.animate([samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled'], .25, 1, 0.75, 'beat', framerate=50)
