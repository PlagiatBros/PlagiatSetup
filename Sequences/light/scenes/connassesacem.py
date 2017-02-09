import sys
sys.path.append("../Controls/Mididings/")

from ports import *

def connassesacem_1(seq, timer):
    seq.send('192.168.0.2:4444', '/la'
    seq.send(qlcstopport, 'stop')
    seq.send('/BC/White/Segment/1', 100)
    seq.send('/BJ/White/Segment/1', 100)
