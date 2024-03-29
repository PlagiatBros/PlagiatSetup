from inspect import getmembers
from seqzero import Sequencer

import scenes
import sequences

import sys
sys.path.append("../Controls/Mididings/")

from ports import *


lightseq = Sequencer(name='/Lightseq', port=8003, target=rpijardinport + ' ' + rpicourport, bpm=120, scenes=scenes)

for name, sequence in getmembers(sequences):
    if name[0] != '_' and type(sequence) == list:
        lightseq.sequence_add(name, sequence)
