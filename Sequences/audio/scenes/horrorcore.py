import sys
sys.path.append("../Controls/Mididings/")

from ports import *


def horrorcore_mooncup_maison_pitchdown(sequencer, timer, wait=0):

    timer.wait(10 if wait == 1 else 2, 'bites')

    t = timer.time()
    sequencer.animate([samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled'], 1, .25, 2, 'beat', framerate=50, timestamp=t)
    sequencer.animate([samplesmainport, '/strip/Keyboards/AM%20pitchshifter/Pitch%20shift/unscaled'], 1, .25, 2, 'beat', framerate=50, timestamp=t)
    sequencer.animate([bassmainport, '/strip/BassMain/AM%20pitchshifter/Pitch%20shift/unscaled'], 1, .25, 2, 'beat', framerate=50, timestamp=t)

    timer.wait(1.5, 'bites')

    sequencer.send(samplesmainport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled',20.)
    sequencer.send(samplesmainport, '/strip/Keyboards/Calf%20Filter/Frequency/unscaled',20.)
    sequencer.send(surfaceorlport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled',20.)
    sequencer.send(surfaceorlport, '/strip/Keyboards/Calf%20Filter/Frequency/unscaled',20.)

    timer.wait(0.5, 'bites')

    sequencer.send(samplesmainport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled',20000.)
    sequencer.send(samplesmainport, '/strip/Keyboards/Calf%20Filter/Frequency/unscaled',20000.)
    sequencer.send(surfaceorlport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled',20000.)
    sequencer.send(surfaceorlport, '/strip/Keyboards/Calf%20Filter/Frequency/unscaled',20000.)

    sequencer.send(samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)
    sequencer.send(samplesmainport, '/strip/Keyboards/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)
    sequencer.send(bassmainport, '/strip/BassMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)

    # secu
    timer.wait(1, 'bites')

    sequencer.send(samplesmainport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled',20000.)
    sequencer.send(samplesmainport, '/strip/Keyboards/Calf%20Filter/Frequency/unscaled',20000.)
    sequencer.send(surfaceorlport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled',20000.)
    sequencer.send(surfaceorlport, '/strip/Keyboards/Calf%20Filter/Frequency/unscaled',20000.)

    sequencer.send(samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)
    sequencer.send(samplesmainport, '/strip/Keyboards/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)
    sequencer.send(bassmainport, '/strip/BassMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.)

def horrorcore_mooncup_maison_mesh(sequencer, timer):
    timer.wait(4, 'bites')
    sequencer.send(56418, '/pedalBoard/button', 99)
