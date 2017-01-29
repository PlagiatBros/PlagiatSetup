from seqzero import Sequencer
import scenes
import sequences

audioseq = Sequencer(name='/Audioseq', port=8002, bpm=120, scenes=scenes)

audioseq.sequence_add('dafist_outro_filter', sequences.dafist_outro_filter)
