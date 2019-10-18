#encoding: utf-8
import sys
sys.path.append("../Controls/Mididings/")
import random

from ports import *

colos = " ".join(['Colo_'+str(i) for i in range(1,47)])
twerks = " ".join(['Twerk_'+str(i) for i in range(1,33)])
coffees =  " ".join(['Tea_'+str(i) for i in range(1,9)])

def fifty_tea(seq, timer):
  seq.send('/pyta/slide/alpha', colos, 0.01)
  for i in range(1, 9):
      seq.send('/pyta/slide/visible', coffees, 0)
      seq.send('/pyta/slide/visible', 'Tea_'+str(i), 1)
      timer.wait(0.25, 'beat')
  seq.send('/pyta/slide/visible', coffees, 0)
  seq.send('/pyta/slide/alpha', colos, 0.1)


def fifty_twerk_1(seq, timer):
    prev = ''
    for i in range(1,11):
        frame = 'Twerk_' + str(i)
        if prev:
            seq.send('/pyta/slide/visible', prev, 0)
        seq.send('/pyta/slide/visible', frame, 1)
        prev = frame
        timer.wait(1/15., 's')
    seq.send('/pyta/slide/visible', frame, 0)


def fifty_twerk_2(seq, timer):
    prev = ''
    for i in range(11,26):
        frame = 'Twerk_' + str(i)
        if prev:
            seq.send('/pyta/slide/visible', prev, 0)
        seq.send('/pyta/slide/visible', frame, 1)
        prev = frame
        timer.wait(1/35., 's')
    seq.send('/pyta/slide/visible', frame, 0)


def fifty_twerk_3(seq, timer):
    prev = ''
    for i in range(26,33):
        frame = 'Twerk_' + str(i)
        if prev:
            seq.send('/pyta/slide/visible', prev, 0)
        seq.send('/pyta/slide/visible', frame, 1)
        prev = frame
        timer.wait(1/15., 's')
    seq.send('/pyta/slide/visible', frame, 0)





butters = ['baaaaaââ', 'Butter', 'BuTtEr', 'butter', 'BUTTER', 'bUtTeR', 'BuRgEr' , 'BeTTeR']
shits = ['Shit', 'jeeeeez', '$hIt', '$HIT', 'chips', 'Chipo ?' '$hit', '$hibre', '$HiT', 'ChIt', 'ChIbrr']

def fifty_butter(seq, timer):
  seq.send('/pyta/text/visible', -1, 0)
  i = random.randint(0,2)
  j = random.randint(0,7)
  seq.send('/pyta/text', i, butters[j]),
  seq.send('/pyta/text/visible', i, 1)
  timer.wait(2, 'beat')
  seq.send('/pyta/text/visible', i, 0)

def fifty_shit(seq, timer):
  seq.send('/pyta/text/visible', -1, 0)
  i = random.randint(0,2)
  j = random.randint(0,8)
  seq.send('/pyta/text', i, shits[j]),
  seq.send('/pyta/text/visible', i, 1)
  timer.wait(2, 'beat')
  seq.send('/pyta/text/visible', i, 0)




_words = ['I dra', 'dose', 'kartin', 'machinz']
_i = 0
def fifty_trapcup(seq, timer):
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
