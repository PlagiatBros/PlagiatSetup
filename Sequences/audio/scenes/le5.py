import sys
sys.path.append("../Controls/Mididings/")

from ports import *


def le5_refrain_cutdown_close(sequencer, timer):
    t = timer.time()

    sequencer.animate([samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled'], 1, .25, 1, 'beat', framerate=50, timestamp=t)
    sequencer.animate([samplesmainport, '/strip/Keyboards/AM%20pitchshifter/Pitch%20shift/unscaled'], 1, .25, 1, 'beat', framerate=50, timestamp=t)
    sequencer.animate([bassmainport, '/strip/BassMain/AM%20pitchshifter/Pitch%20shift/unscaled'], 1, .25, 1, 'beat', framerate=50, timestamp=t)
    sequencer.animate([vxpitchshifterport, '/x42/pitch'], 1, .25, 1, 'beat', framerate=50, timestamp=t)

    timer.wait(3, 'bites')

    sequencer.send(samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)
    sequencer.send(samplesmainport, '/strip/Keyboards/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)
    sequencer.send(bassmainport, '/strip/BassMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)
    sequencer.send(vxpitchshifterport, '/x42/pitch', 1.)

def le5_fartingart(sequencer, timer):

    sequencer.animate([samplesmainport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled'], 20000., 280., .5, 'sec', framerate=50)
    sequencer.animate([surfaceorlport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled'], 20000., 280., .5, 'sec', framerate=5)

def le5_louboutin_close(sequencer, timer):
    t = timer.time()

    # vxorldelay_off
    sequencer.send(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 1.0)
    sequencer.send(vxorlpostport, '/strip/VxORLDelayPost/Gain/Mute', 1.0)
    sequencer.send(surfaceorlport, '/vxorl', 'delay', 0)

    # mute  SAMPLES
    sequencer.animate([samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled'], 1., .25, 1, 'beat', framerate=50, timestamp=t)
    sequencer.animate([samplesmainport, '/strip/Keyboards/AM%20pitchshifter/Pitch%20shift/unscaled'], 1., .25, 1, 'beat', framerate=50, timestamp=t)

    timer.wait(3.25, 'bites')
    t = timer.time()

    # vxorldelay_on
    sequencer.send(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 0.0)
    sequencer.send(vxorlpostport, '/strip/VxORLDelayPost/Gain/Mute', 0.0)
    sequencer.send(surfaceorlport, '/vxorl', 'delay', 1)

    # unmute  SAMPLES
    sequencer.animate([samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled'], 0.25, 1., 0.75, 'beat', framerate=50, timestamp=t)
    sequencer.animate([samplesmainport, '/strip/Keyboards/AM%20pitchshifter/Pitch%20shift/unscaled'], 0.25, 1., 0.75, 'beat', framerate=50, timestamp=t)
