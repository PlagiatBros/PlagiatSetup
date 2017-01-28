def fifty_refrain_auto(sequencer, timer):
    timer.wait(12, 'bites')
    sequencer.send(56418, '/pedalBoard/button', 6)
