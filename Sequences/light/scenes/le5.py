#encoding: utf-8
import sys
sys.path.append("../Controls/Mididings/")

from ports import *

def le5_niggahdontyou(seq, timer):
    seq.send('/pyta/text', 2, "Niggah, 
don't you know it ain't no heavy duty
for Mi$$y $chneck One Two?")
    seq.send('/pyta/text/visible', 2, 1)
    timer.wait(1, 's')
    seq.send('/pyta/text', 2, "Nigrid, 
don't you know it ain't no heavy duty
for Mi$$y $chneck One Two?")
    timer.wait(0.3, 's')
    seq.send('/pyta/text', 2, "iNgrid, 
don't you know it ain't no heavy duty
for Mi$$y $chneck One Two?")
    timer.wait(0.3, 's')
    seq.send('/pyta/text', 2, "Nigroo, 
don't you know it ain't no heavy duty
for Mi$$y $chneck One Two?")
    timer.wait(1, 's')
    seq.send('/pyta/text', 2, "Nicole 
don't you know it ain't no heavy duty
for Mi$$y $chneck One Two?")
    timer.wait(0.3, 's')
    seq.send('/pyta/text', 2, "Niggah, 
don't you know it ain't no heavy duty
for Mi$$y $chneck One Two?")
