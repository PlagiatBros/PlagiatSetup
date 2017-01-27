from seqzero import Sequencer
from ports import *

from seqzero import Sequencer

import trapcut_scenes

seq = Sequencer(bpm=120, port=trapbreakerport, scenes=trapcut_scenes)
seq.start()
