import sys
sys.path.append("../Controls/Mididings/")

from ports import *




def connassesacem_anim(seq, timer):

    while True:
        r = range(1,9)
        for i in range(1,9):

            seq.animate(['/CC/Segment/%i' % r[(i-2)%8], '$', '$', '$'], 50, 0, 0.5, "beat", mode="integer")
            seq.animate(['/CC/Segment/%i' % r[(i-1)%8], '$', '$', '$'], 150, 50, 0.5, "beat", mode="integer")
            seq.animate(['/CC/Segment/%i' % r[( i )%8], '$', '$', '$'], 50, 150, 0.5, "beat", mode="integer")
            seq.animate(['/CC/Segment/%i' % r[(i+1)%8], '$', '$', '$'], 0, 50, 0.5, "beat", mode="integer")

            seq.animate(['/CJ/Segment/%i' % (9-r[(i-2)%8]), '$', '$', '$'], 50, 0, 0.5, "beat", mode="integer")
            seq.animate(['/CJ/Segment/%i' % (9-r[(i-1)%8]), '$', '$', '$'], 150, 50, 0.5, "beat", mode="integer")
            seq.animate(['/CJ/Segment/%i' % (9-r[( i )%8]), '$', '$', '$'], 50, 150, 0.5, "beat", mode="integer")
            seq.animate(['/CJ/Segment/%i' % (9-r[(i+1)%8]), '$', '$', '$'], 0, 50, 0.5, "beat", mode="integer")

            timer.wait(.5, "beat")



def connassesacem_1(seq, timer):
    seq.send('/CC/Segment/1', 100, 100, 100)
    seq.send('/CC/Segment/2', 75, 75, 75)
    seq.send('/CC/Segment/3', 50, 50, 50)
    seq.send('/CC/Segment/4', 25, 25, 25)
    seq.send('/CJ/Segment/8', 100, 100, 100)
    seq.send('/CJ/Segment/7', 75, 75, 75)
    seq.send('/CJ/Segment/6', 50, 50, 50)
    seq.send('/CJ/Segment/5', 25, 25, 25)

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
