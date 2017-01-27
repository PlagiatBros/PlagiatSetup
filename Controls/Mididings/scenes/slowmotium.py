#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################

#### SlowMotium ####
slowmotium = [
    [orl, jeannot] >> Filter(PROGRAM) >> Ctrl(0, 8) >> tapeutapecontrol,
    orl >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    orl >> ProgramFilter(2) >> [ # Couplet - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 4),
            SendOSC(slport, '/set', 'tempo', 75),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 75),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'xxxx'),
            SendOSC(klickport, '/klick/metro/start'),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],

            ]),


            vxorlgars_off,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_on,

            vxjeannotdelay_on,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            ] >> Discard()
        ],
    orl >> ProgramFilter(3) >> [ # Couplet - Bouton 3
            vxorlgars_off,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_on,

            vxjeannotdelay_on,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
        ],

    orl >> ProgramFilter(4) >> [ # Couplet - Bouton 4
            vxorlgars_off,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_on,

            vxjeannotdelay_on,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
        ],


    ]
