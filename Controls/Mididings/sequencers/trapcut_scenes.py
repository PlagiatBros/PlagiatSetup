from ports import *

_ip = '127.0.0.1:'

def _open(send):
    send(samplesmainport, '/strip/SamplesMain/Gain/Mute', 0.0)
    send(samplesmainport, '/strip/Keyboards/Gain/Mute', 0.0)
    send(bassmainport, '/strip/BassMain/Gain/Mute', 0.0)
    # send(slport, '/sl/1/set', 'wet', 1)
    # send(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0)
    # send(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0)
    # send(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0)
    # send(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0)
    # send(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0)
    # send('1111', '/trapcut/open')

def _close(send):
    send(samplesmainport, '/strip/SamplesMain/Gain/Mute', 1.0)
    send(samplesmainport, '/strip/Keyboards/Gain/Mute', 1.0)
    send(bassmainport, '/strip/BassMain/Gain/Mute', 1.0)
    # send(slport, '/sl/1/set', 'wet', 0)
    # send(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 1.0)
    # send(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 1.0)
    # send(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 1.0)
    # send(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0)
    # send(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0)
    # send('1111', '/trapcut/close')

def _cutXtimes(x, sequencer, timer):
    for i in range(x):
        _open(sequencer.send)
        timer.wait(1, 'beat')
        _close(sequencer.send)
        timer.wait(1, 'beat')
    _open(sequencer.send)

def I(sequencer, timer):
    _cutXtimes(1, sequencer, timer)

def II(sequencer, timer):
    _cutXtimes(2, sequencer, timer)

def III(sequencer, timer):
    _cutXtimes(3, sequencer, timer)

def IIII(sequencer, timer):
    _cutXtimes(4, sequencer, timer)
