from utils import osc2MidiRouter
from ports import *

router = osc2MidiRouter('osc2Tapeutape', port=surfaceorltomidiport, target=surfaceorlport)
router.start()
