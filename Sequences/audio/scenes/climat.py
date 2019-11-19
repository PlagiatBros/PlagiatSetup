import sys
sys.path.append("../Controls/Mididings/")

from ports import *


#def _log(start, end, frame, n_frame):
#    lin:
#    return (end - start) / n_frames * frame + start


def climat_outro_filter(sequencer, timer):

    timer.wait(20, 'sex')

    sequencer.animate([samplesmainport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled'], 20., 20000., 300, 'sec', framerate=50)
    sequencer.animate([samplesmainport, '/strip/Keyboards/Calf%20Filter/Frequency/unscaled'], 20., 20000., 300, 'sec', framerate=50)
    sequencer.animate([surfaceorlport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled'], 20., 20000., 300, 'sec', framerate=5)
    sequencer.animate([surfaceorlport, '/strip/Keyboards/Calf%20Filter/Frequency/unscaled'], 20., 20000., 300, 'sec', framerate=5)
