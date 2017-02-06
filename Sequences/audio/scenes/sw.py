import sys
sys.path.append("../Controls/Mididings/")

import ports as _ports


def sw_couplet_auto(sequencer, timer):
    timer.wait(7.5, 'bites')
#    sequencer.send(56418, '/pedalBoard/button', 1)
    sequencer.send(_ports.samplesmainport, '/strip/SamplesMain/Gain/Mute', 1.0)
    timer.wait(0.5, 'bites')
    sequencer.send(_ports.samplesmainport, '/strip/SamplesMain/Gain/Mute', 0.0)
    sequencer.send(56418, '/pedalBoard/button', 3)

def sw_couplet_auto2(sequencer, timer):
    timer.wait(7.5, 'bites')
#    sequencer.send(56418, '/pedalBoard/button', 1)
    sequencer.send(_ports.samplesmainport, '/strip/SamplesMain/Gain/Mute', 1.0)
    timer.wait(0.5, 'bites')
    sequencer.send(_ports.samplesmainport, '/strip/SamplesMain/Gain/Mute', 0.0)
    sequencer.send(56418, '/pedalBoard/button', 6)


def sw_shit_going(sequencer, timer):
    timer.wait(5.8, 'bites')
    sequencer.send(_ports.vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 0.0)
    sequencer.send(_ports.vxjeannotpreport, '/strip/VxJeannotDelayPre/Gain/Mute', 0.0)
