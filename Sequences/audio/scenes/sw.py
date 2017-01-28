def fifty_refrain_auto(sequencer, timer):
    timer.wait(7.5, 'bites')
    sequencer.send(56418, '/pedalBoard/button', 1)
    timer.wait(0.5, 'bites')
    sequencer.send(56418, '/pedalBoard/button', 4)
