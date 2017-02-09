from inspect import getmembers
from seqzero import Sequencer

import scenes
import sequences

import sys
sys.path.append("../Controls/Mididings/")

from ports import *


lightseq = Sequencer(name='/Lightseq', port=8003, target='127.0.0.1:3333 127.0.0.1:'+str(qlcport), bpm=120, scenes=scenes)

for name, sequence in getmembers(sequences):
    if name[0] != '_' and type(sequence) == list:
        lightseq.sequence_add(name, sequence)
