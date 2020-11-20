import sys
sys.path.append("../Controls/Mididings/")

from ports import *

def dafist_blast_delayed(sequencer, timer):
    timer.wait( 2 * 16, 'bites')
    sequencer.send(56418, '/pedalBoard/button', 97)

def dafist_blast_phase(sequencer, timer):
    timer.wait(4 * 16, 'bites')
    sequencer.send(samplesmainport, '/strip/Keyboards/Gain/Mute', 1.0)


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

def dafist_gate_cancel_orl(seq, timer):
    seq.send(vxorlpreport, '/strip/VxORLGars/Gate/Threshold%20(dB)/unscaled', -70.0)
    seq.send(vxorlpreport, '/strip/VxORLMeuf/Gate/Threshold%20(dB)/unscaled', -70.0)
    seq.wait(3, 'bites')
    seq.send(vxorlpreport, '/strip/VxORLGars/Gate/Threshold%20(dB)/unscaled', -48.0) 
    seq.send(vxorlpreport, '/strip/VxORLMeuf/Gate/Threshold%20(dB)/unscaled', -48.0)
