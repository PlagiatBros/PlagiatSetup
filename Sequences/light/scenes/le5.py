#encoding: utf-8
import sys
sys.path.append("../Controls/Mididings/")

from ports import *

def le5_niggahdontyou(seq, timer):
    text = '\ndon\'t you know it ain\'t\n\
no heavy duty too heavy\n\
for Mi$$y $chneck One Two?'

    seq.send('/pyta/text', 2, 'Niggah,\n' + text)
    seq.send('/pyta/text/visible', 2, 1)
    timer.wait(1, 's')
    seq.send('/pyta/text', 2, 'Nigrid,\n' + text)
    timer.wait(0.3, 's')
    seq.send('/pyta/text', 2, 'iNgrid,\n' + text)
    timer.wait(0.3, 's')
    seq.send('/pyta/text', 2, 'Nigroo,\n' + text)
    timer.wait(1, 's')
    seq.send('/pyta/text', 2, 'Nicole,\n' + text)
    timer.wait(0.3, 's')
    seq.send('/pyta/text', 2, 'Niggah,\n' + text)


_words = ['DO YOU', 'USE', 'CRUISE', 'CONTROL?']
_i = 0
def le5_trapcup(seq, timer):
    global _i
    word = _words[_i%len(_words)]
    size = 2.5 / len(word)
    _i += 1
    seq.send('/pyta/slide/lock', 'White', 1)
    seq.send('/pyta/slide/strobe', 'White', 1, 2, 0.5)
    seq.send('/pyta/text/rgb', 0, 0, 0, 0)
    seq.send('/pyta/text', 0, word)
    seq.send('/pyta/text/size', 0, size)

    seq.send('/pyta/slide/visible', 'White', 1)
    seq.send('/pyta/text/visible', 0, 1)
    timer.wait(0.5, 'b')
    seq.send('/pyta/text/visible', 0, 0)
    seq.send('/pyta/slide/visible', 'White', 0)
    seq.send('/pyta/slide/lock', 'White', 0)




def le5_instouboulouboutin(seq, timer):
    seq.send('/pyta/text', 0, 'Instouboul')
    timer.wait(0.1, 's')
    seq.send('/pyta/text', 0, 'Instoubolu')
    timer.wait(0.1, 's')
    seq.send('/pyta/text', 0, 'Instoublou')
    timer.wait(0.1, 's')
    seq.send('/pyta/text', 0, 'Instoulbou')
    timer.wait(0.1, 's')
    seq.send('/pyta/text', 0, 'Instolubuo')
    timer.wait(0.1, 's')
    seq.send('/pyta/text', 0, 'Instlouubo')
    timer.wait(0.1, 's')
    seq.send('/pyta/text', 0, 'Insltouubo')
    timer.wait(0.1, 's')
    seq.send('/pyta/text', 0, 'Inlstuouob')
    timer.wait(0.1, 's')
    seq.send('/pyta/text', 0, 'Ilnsutooub')
    timer.wait(0.1, 's')
    seq.send('/pyta/text', 0, 'Linustoubo')
    timer.wait(0.1, 's')
    seq.send('/pyta/text', 0, 'Lunistobou')
    timer.wait(0.1, 's')
    seq.send('/pyta/text', 0, 'Loutsoubou')
    timer.wait(0.1, 's')
    seq.send('/pyta/text', 0, 'Loubinstou')
    timer.wait(0.1, 's')
    seq.send('/pyta/text', 0, 'Loubisnotu')
    timer.wait(0.1, 's')
    seq.send('/pyta/text', 0, 'Loubsiontu')
    timer.wait(0.1, 's')
    seq.send('/pyta/text', 0, 'Loubointon')
    timer.wait(0.1, 's')
    seq.send('/pyta/text', 0, 'Louboutsoin')
    timer.wait(0.1, 's')
    seq.send('/pyta/text', 0, 'Loubotchoin')
    timer.wait(0.1, 's')
    seq.send('/pyta/text', 0, 'Louboutin')
    timer.wait(0.1, 's')
