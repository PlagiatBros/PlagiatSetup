# coding=utf8
from mididings import *
from mididings.extra.osc import OSCInterface
from mididings.extra.inotify import AutoRestart
from utils import OSCCustomInterface

config(
	backend='jack',
	client_name='DrumKlitRoutes',
	out_ports=['DKTapeutape'],
	in_ports=['DKJeannotIn']
)

hook(
    AutoRestart()
)

from ports import *

#### Slicing ####
slicing = PortFilter('DKJeannotIn') >> [
    Filter(NOTEON) >>
    [
        KeyFilter(64) >> NoteOn(64, 127),
        ~KeyFilter(64) >> Pass(),
        ]
    ]


#### RUN ###################################################

run(
    scenes = {
            1: SceneGroup("Slicing", [
          		Scene("Slicing",
                    [
                        slicing,
                    ]
        		),
	    ]),

    },
)
