import sys
sys.path.append("../Controls/Mididings/")

from ports import *

def sw_couplet_auto(sequencer, timer):
    timer.wait(7.5, 'bites')
#    sequencer.send(56418, '/pedalBoard/button', 1)
    sequencer.send(samplesmainport, '/strip/SamplesMain/Gain/Mute', 1.0)
    timer.wait(0.5, 'bites')
    sequencer.send(samplesmainport, '/strip/SamplesMain/Gain/Mute', 0.0)
    sequencer.send(56418, '/pedalBoard/button', 3)

def sw_couplet_auto2(sequencer, timer):
    timer.wait(7.5, 'bites')
#    sequencer.send(56418, '/pedalBoard/button', 1)
    sequencer.send(samplesmainport, '/strip/SamplesMain/Gain/Mute', 1.0)
    timer.wait(0.5, 'bites')
    sequencer.send(samplesmainport, '/strip/SamplesMain/Gain/Mute', 0.0)
    sequencer.send(56418, '/pedalBoard/button', 81)

def sw_couplet_break1(sequencer, timer):
    pass

def sw_couplet_break2(sequencer, timer):
    timer.wait(2, 'bites')
    sequencer.send(vxorlpreport, '/strip/VxORLGars/Gain/Mute', 1.0)
    sequencer.send(vxorlpostport, '/strip/VxORLGarsPost/Gain/Mute', 1.0)
    sequencer.send(surfaceorlport, '/vxorl', 'gars', 0)
    sequencer.send(vxorlpreport, '/strip/VxORLMeuf/Gain/Mute', 0.0)
    sequencer.send(vxorlpostport, '/strip/VxORLMeufPost/Gain/Mute', 1.0)
    sequencer.send(surfaceorlport, '/vxorl', 'meuf', 0)
    sequencer.send(vxorlpreport, '/strip/VxORLVocode/Gain/Mute', 0.0)
    sequencer.send(vxorlpostport, '/strip/VxORLVocodePost/Gain/Mute', 0.0)
    sequencer.send(surfaceorlport, '/vxorl', 'vocode', 0)


def sw_shit_going(sequencer, timer):
    timer.wait(5.8, 'bites')
    sequencer.send(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 0.0)
    sequencer.send(vxjeannotpreport, '/strip/VxJeannotDelayPre/Gain/Mute', 0.0)
