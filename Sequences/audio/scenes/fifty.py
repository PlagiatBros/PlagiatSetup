import sys
sys.path.append("../Controls/Mididings/")

from ports import *

def fifty_intro(sequencer, timer):
    timer.wait(11, 'bites')
    sequencer.send(slport, '/sl/1/hit', 'record')
    timer.wait(12, 'bite')
    sequencer.send(56418, '/pedalBoard/button', 3)


def fifty_refrain_auto(sequencer, timer):
    timer.wait(12, 'bites')
    sequencer.send(56418, '/pedalBoard/button', 6)
