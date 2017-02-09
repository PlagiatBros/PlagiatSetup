#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################

#### Get Ur Freak On ####
geturfreakon = [
    Init([
        Program(seq24PageMap[8]) >> seq24once,
        Ctrl(0, 7) >> tapeutapecontrol,
        zynmicrotonal_off,
    ]),
    [orl, jeannot] >> Filter(PROGRAM) >> [
        SendOSC(audioseqport, '/Audioseq/Sequences/Disable', '*')
    ] >> Discard(),
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    orl >> ProgramFilter(2) >> [ # SlowMotium (bouclage bass) - Bouton 2
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
            vxjeannotvocode_off,

            bassdry,
            bassscape,

            ] >> Discard(),
        [
            bassdetunest_off,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,
            ]
        ],
    jeannot >> ProgramFilter(2) >> [ # SlowMotium (vxdelay off) - Bouton 2
            vxorlgars_off,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_on,

            vxjeannotdelay_on,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotvocode_off,
        ],

    jeannot >> ProgramFilter(3) >> [ # SlowMotium (vxdelay on) - Bouton 3
            vxorlgars_off,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_on,

            vxjeannotdelay_on,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotvocode_off,
        ],
    orl >> ProgramFilter(3) >> [ # Refrain - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 200),

            SendOSC(klickport, '/klick/simple/set_tempo', 200),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.522388),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.522388),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.6296),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],

            ]),


            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry,
            bassscape,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],


    ]
