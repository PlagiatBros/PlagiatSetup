#encoding: utf-8
import sys
sys.path.append("../Controls/Mididings/")

from ports import *

def hc_notheft(seq, timer):
    seq.send(rpijardinport, '/pyta/text', 1, "                 Theft")
    seq.send(rpicourport, '/pyta/text', 1, "            ain't no Rap ")
    seq.send(rpijardinport, '/pyta/text/visible', 1, 1)
    seq.send(rpicourport, '/pyta/text/visible', 1, 1)
    timer.wait(3, 's')
    seq.send('/pyta/text/strobe', 1, 1, 4, 0.5)
    SendOSC(rpijardinport, '/pyta/text', 1, "Copying ain't no Theft"),
    SendOSC(rpicourport, '/pyta/text', 1, "Copulefting ain't no Rape"),
    timer.wait(1, 's')
    seq.send('/pyta/text/strobe', 1, 0)
    timer.wait(2, 's')
    seq.send('/pyta/text/animate', 1, 'alpha', 1, 0, 8)
