from ports import *

def _close(send):
    send(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0)
    send(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0)
    send(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0)
    send(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0)
    send(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0)

def _open(send):
    send(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 1.0)
    send(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 1.0)
    send(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 1.0)
    send(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0)
    send(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0)

def _cutXtimes(x, sequencer, timer):
    for i in range(x):
        _open(sequencer.send)
        timer.wait(0.5, 'beat')
        _close(sequencer.send)

def I(sequencer, timer):
    _cutXtimes(1, sequencer, timer)

def II(sequencer, timer):
    _cutXtimes(2, sequencer, timer)

def III(sequencer, timer):
    _cutXtimes(3, sequencer, timer)

def IIII(sequencer, timer):
    _cutXtimes(4, sequencer, timer)
