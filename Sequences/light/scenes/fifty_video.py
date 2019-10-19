#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from random import randint, choice

_butters = ['baaaaaââ', 'Butter', 'BuTtEr', 'butter', 'BUTTER', 'bUtTeR', 'BuRgEr' , 'BeTTeR']
_shits = ['Shit', 'jeeeeez', '$hIt', '$HIT', 'chips', 'Chipo ?' '$hit', '$hibre', '$HiT', 'ChIt', 'ChIbrr']

def fifty_butter(seq, timer):
  seq.send('/pyta/text/{0,2}/reset')
  for port in [rpicourport, rpijardinport]:
      i = choice([0,2])
      seq.send(port, '/pyta/text/%i/set' % i, 'visible', 1)
      seq.send(port, '/pyta/text/%i/set' % i, 'text', _butters[randint(0,len(_butters)-1)], 0.2)
  timer.wait(2, 'beat')
  seq.send('/pyta/text/{0,2}/set', 'visible', 0)

def fifty_shit(seq, timer):
  seq.send('/pyta/text/{0,2}/reset')
  for port in [rpicourport, rpijardinport]:
      i = choice([0,2])
      seq.send(port, '/pyta/text/%i/set' % i, 'visible', 1)
      seq.send(port, '/pyta/text/%i/set' % i, 'text', _shits[randint(0,len(_butters)-1)], 0.2)
  timer.wait(2, 'beat')
  seq.send('/pyta/text/{0,2}/set', 'visible', 0)



_words = ['I dro', 'DOSE', 'KarTiN', 'MaCH!nZ']
_i = 0
def fifty_trapcup(seq, timer):
    global _i
    seq.send('/pyta/slide/white/reset')
    seq.send('/pyta/slide/white/set', 'visible', 1)
    seq.send('/pyta/slide/white/strobe', 'color', 1,1,1, 0,0,0, 0.08, 0.5)
    seq.send('/pyta/slide/white/set', 'position_z', -10)
    seq.send('/pyta/text/0/reset')
    seq.send('/pyta/text/0/set', 'visible', 1)
    seq.send('/pyta/text/0/strobe', 'color', 0,0,0, 1,1,1, 0.08, 0.5)
    seq.send('/pyta/text/0/set', 'text', _words[_i%len(_words)])
    _i += 1
    timer.wait(0.5, 'b')
    seq.send('/pyta/slide/white/set', 'visible', 0)
    seq.send('/pyta/text/0/set', 'visible', 0)
