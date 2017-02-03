from inspect import getmembers
from seqzero import Sequencer
import scenes
import sequences

audioseq = Sequencer(name='/Audioseq', port=8002, bpm=120, scenes=scenes)

for name, sequence in getmembers(sequences):
    if name[0] != '_' and type(sequence) == list:
        audioseq.sequence_add(name, sequence)
