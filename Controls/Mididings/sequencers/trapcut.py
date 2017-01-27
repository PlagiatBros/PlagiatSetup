from seqzero import Sequencer
from ports import *

from seqzero import Sequencer

import trapcut_scenes

trapcut = Sequencer(name='Trapcut',bpm=240, port=trapcutport, scenes=trapcut_scenes)

trapcut.start_threaded()

# set tempo : send /Trapcut/Bpm x (x = 2 or 3 times the actual tempo)
# launch cut: send /Trapcut/Scene/Play I (or II, III, IIII)
