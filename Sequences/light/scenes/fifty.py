import sys
sys.path.append("../Controls/Mididings/")
import random

from ports import *

colos=""
for i in range(1,47):
colos.append('Colo_'+str(i)+' ')

colos=""
for i in range(1,9):
colos.append('Colo_'+str(i)+' ')

def fifty_tea(seq, timer):
  seq.send('/pyta/slide/alpha', colos, 0.01)
  for i in range(1, 9):
      seq.send('/pyta/slide/visible', coffees, 0)
      seq.send('/pyta/slide/visible', 'Coffee_'+str(i), 1)
      timer.wait(0.25, 'beat')
  seq.send('/pyta/slide/alpha', colos, 0.1)

  
def fifty_butter(seq, timer):
  i = random.randomint(0,2)
  seq.send('/pyta/text', i, "BuTtEr"),
  seq.send('/pyta/text/visible', i, 1)
  timer.wait(2, 'beat)
  seq.send('/pyta/text/visible', i, 0)
             
def fifty_shit(seq, timer):
  i = random.randomint(0,2)
  seq.send('/pyta/text', i, "$hIt"),
  seq.send('/pyta/text/visible', i, 1)
  timer.wait(2, 'beat)
  seq.send('/pyta/text/visible', i, 0)        
