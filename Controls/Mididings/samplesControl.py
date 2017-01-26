# coding=utf8
from mididings import *
from mididings.extra.osc import OSCInterface
from mididings.extra.inotify import AutoRestart
from utils import OSCCustomInterface



config(
	backend='jack',
	client_name='SamplesControlRoutes',
	out_ports=['SCTapeutape', 'SCCtrlOut'],
	in_ports=['SCCtrlIn']
)

hook(
    OSCInterface(57422, 57423), # "osc.udp://CtrlOrl:56423"),
    OSCCustomInterface(57418),
    AutoRestart()
)

from ports import *

#### Slicing ####
slicing = PortFilter('SCCtrlIn') >> [
#    ProgramFilter(1) >> stop, # !!!STOP!!! #
    Filter(NOTE) >> [
        KeyFilter(60) >> [ # Gestion Volume Sample 1
            Filter(NOTEON) >> SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 1.0) >> Discard(),
            Filter(NOTEOFF) >> SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0) >> Discard()
            ],
        KeyFilter(61) >> [ # Gestion Volume Sample 2
            Filter(NOTEON) >> SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 1.0) >> Discard(),
            Filter(NOTEOFF) >> SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0) >> Discard()
            ],
        KeyFilter(62) >> [ # Gestion Volume Sample 3
            Filter(NOTEON) >> SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 1.0) >> Discard(),
            Filter(NOTEOFF) >> SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0) >> Discard()
            ],
        KeyFilter(63) >> [ # Gestion Volume Sample 4
            Filter(NOTEON) >> SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0) >> Discard(),
            Filter(NOTEOFF) >> SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0) >> Discard()
            ],
        KeyFilter(64) >> [ # Gestion Volume Sample 5
            Filter(NOTEON) >> SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0) >> Discard(),
            Filter(NOTEOFF) >> SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0) >> Discard()
            ],
        ],
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
