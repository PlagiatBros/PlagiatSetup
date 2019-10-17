#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *

from random import normalvariate, random, randint


def fifty_offre_emploi_strobe(seq, timer):
    while True:
        for port in [rpicourport, rpijardinport]:
            for t in [0, 1, 2, 3]:

            deviation = normalvariate(0, 0.5)
            if deviation > 0.8:
                seq.send(port, '/pyta/text/'+t+'/strobe', 'alpha', 1, 0, random(), 0.4 + random()/5)
            else:
                seq.send(port, '/pyta/text/'+t+'/strobe_stop', 'alpha')

        timer.wait(4, 's')


butters = ['baaaaaââ', 'Butter', 'BuTtEr', 'butter', 'BUTTER', 'bUtTeR', 'BuRgEr' , 'BeTTeR']
shits = ['Shit', 'jeeeeez', '$hIt', '$HIT', 'chips', 'Chipo ?' '$hit', '$hibre', '$HiT', 'ChIt', 'ChIbrr']

def fifty_butter(seq, timer):
  seq.send('/pyta/text/{1,2}/set', 'text', '')
  i = random.randint(1,2)
  j = random.randint(0,7)
  seq.send('/pyta/text/'+i+'/set', 'text', butters[j], 0.2),
  timer.wait(2, 'beat')
  seq.send('/pyta/text/'+i+'/set', 'text', ''),

def fifty_shit(seq, timer):
  seq.send('/pyta/text/{1,2}/set', 'text', '')
  i = random.randint(1,2)
  j = random.randint(0,7)
  seq.send('/pyta/text/'+i+'/set', 'text', shits[j], 0.2),
  timer.wait(2, 'beat')
  seq.send('/pyta/text/'+i+'/set', 'text', ''),


  _words = ['I drop', 'DOSE', 'KaRtiN', 'mÀchinZ']
  _i = 0
  def fifty_trapcup(seq, timer):
      global _i
      word = _words[_i%len(_words)]
      _i += 1
      seq.send('/pyta/slide/white/reset')
      seq.send('/pyta/slide/white/set', 'visible', 1)
      seq.send('/pyta/slide/white/set', 'position_z', -1)
      seq.send('/pyta/slide/white/set', 'noise', -10)
      seq.send('/pyta/text/0/reset')
      seq.send('/pyta/text/0/set', 'visible', 1)
      seq.send('/pyta/text/0/set', 'text', word)
      seq.send('/pyta/text/0/set', 'color', 0, 0, 0)
      seq.send('/pyta/text/0/set', 'noise', 1)
      timer.wait(0.5, 'b')
      seq.send('/pyta/text/0/set', 'visible', 0)
      seq.send('/pyta/slide/white/set', 'visible', 0)
