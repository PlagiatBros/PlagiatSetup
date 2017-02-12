import sys
sys.path.append("../Controls/Mididings/")

from ports import *


def connassesacem_1(seq, timer):
    seq.send('/CC/White/Segment/1', 100)
    seq.send('/CC/White/Segment/2', 75)
    seq.send('/CC/White/Segment/3', 50)
    seq.send('/CC/White/Segment/4', 25)
    seq.send('/CJ/White/Segment/8', 100)
    seq.send('/CJ/White/Segment/7', 75)
    seq.send('/CJ/White/Segment/6', 50)
    seq.send('/CJ/White/Segment/5', 25)

    seq.send(vporlport,'/pyta/slide/rotate_z', 98, -90)
    seq.send(vporlport,'/pyta/slide/rgb', 98, 0.7, 0, 0)
    seq.send(vporlport,'/pyta/slide/visible', 98, 1)

    seq.send(vpjeannotport,'/pyta/slide/rotate_z', 98, 90)
    seq.send(vpjeannotport,'/pyta/slide/rgb', 98, 0.7, 0, 0)
    seq.send(vpjeannotport,'/pyta/slide/visible', 98, 1)

def connassesacem_2(seq, timer):
    seq.send(vpjeannotport, '/pyta/slide/alpha', 99, 0)
    seq.send(vpjeannotport, '/pyta/slide/rgb', 99, 1, 0, 0)
    seq.send(vpjeannotport, '/pyta/slide/visible', 99, 1)
    seq.animate([vpjeannotport, '/pyta/slide/alpha', 99], 0., 1., 120, 'sex', framerate=50)

    seq.send(vporlport, '/pyta/slide/alpha', 99, 0)
    seq.send(vporlport, '/pyta/slide/rgb', 99, 1, 0, 0)
    seq.send(vporlport, '/pyta/slide/visible', 99, 1)
    seq.animate([vporlport, '/pyta/slide/alpha', 99], 0., 1., 120, 'sex', framerate=50)
