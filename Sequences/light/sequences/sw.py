#encoding: utf-8
import sys
sys.path.append("../Controls/Mididings/")

import random

from ports import *

sw_leboncoin = [
    [[rpijardinport, '/pyta/slide/visible', 'PlagiatAnniv', 1], [rpicourport, '/pyta/text', 0, 'PLAGIAT'], [rpicourport, '/pyta/text/visible', 0, 1]], None, None, [['/pyta/slide/visible', -1, 0], ['/pyta/text/visible', -1, 0]],
    [[rpicourport, '/pyta/slide/visible', 'PlagiatAnniv', 1], [rpijardinport, '/pyta/text', 0, 'PLAGIAT'], [rpijardinport, '/pyta/text/visible', 0, 1]], None, None, [['/pyta/slide/visible', -1, 0], ['/pyta/text/visible', -1, 0]]
]


ones = ['1', 'One', '0ne', 'ONE', 'won']
twos = ['2', 'Cinq', 'Two', 'Toux', 'tu:']

sw_onetwo_jardin = []
for i in range(0,len(ones)):
    j=random.randint(1,3)
    sw_onetwo_jardin.append([[rpijardinport, '/pyta/text/visible', -1, 0], [rpijardinport, '/pyta/text', j, ones[i]], [rpijardinport, '/pyta/text/visible', j, 1]])
for i in range(0,len(twos)):
    j=random.randint(1,3)
    sw_onetwo_jardin.append([[rpijardinport, '/pyta/text/visible', -1, 0], [rpijardinport, '/pyta/text', j, twos[i]], [rpijardinport, '/pyta/text/visible', j, 1]])

sw_onetwo_cour = []
for i in range(0,len(ones)):
    j=random.randint(1,3)
    sw_onetwo_cour.append([[rpicourport, '/pyta/text/visible', -1, 0], [rpicourport, '/pyta/text', j, ones[i]], [rpicourport, '/pyta/text/visible', j, 1]])
for i in range(0,len(twos)):
    j=random.randint(1,3)
    sw_onetwo_cour.append([[rpicourport, '/pyta/text/visible', -1, 0], [rpicourport, '/pyta/text', j, twos[i]], [rpicourport, '/pyta/text/visible', j, 1]])

