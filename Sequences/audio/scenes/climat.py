import sys
sys.path.append("../Controls/Mididings/")

from ports import *


def climat_couplet1b(sequencer, timer):
    timer.wait(19.5, 'b')
    sequencer.send(56418, '/pedalBoard/button', 93)



def climat_couplet2b(sequencer, timer):

    sequencer.send(samplesmainport, '/strip/Keyboards/Calf%20Filter/Frequency/unscaled', 20.)

    timer.wait(37, 'b')

    sequencer.animate([samplesmainport, '/strip/Keyboards/Calf%20Filter/Frequency/unscaled'], 20., 20000., 18, 'b', framerate=50)

    pass



def climat_couplet2c(sequencer, timer):

    pass

def climat_outro_filter(sequencer, timer):

    timer.wait(20, 's')

    sequencer.animate([samplesmainport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled'], 20., 20000., 300, 'sec', framerate=50)
    sequencer.animate([samplesmainport, '/strip/Keyboards/Calf%20Filter/Frequency/unscaled'], 20., 20000., 300, 'sec', framerate=50)
    sequencer.animate([surfaceorlport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled'], 20., 20000., 300, 'sec', framerate=5)
    sequencer.animate([surfaceorlport, '/strip/Keyboards/Calf%20Filter/Frequency/unscaled'], 20., 20000., 300, 'sec', framerate=5)
