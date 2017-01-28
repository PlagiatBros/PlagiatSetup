#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################

#### Le5 ####
le5 = [
    [orl, jeannot] >> Filter(PROGRAM) >> Ctrl(0, 3) >> tapeutapecontrol,
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    orl >> ProgramFilter(2) >> [ # Intro - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.48148),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

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
            ] >> Discard()
        ],
    orl >> ProgramFilter(3) >> [ # Couplet A - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.48148),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

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
            ] >> Discard()
        ],
    orl >> ProgramFilter(4) >> [ # Couplet B - Bouton 4
        Program(67) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.48148),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

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
            ] >> Discard()
        ],
    orl >> ProgramFilter(5) >> [ # Couplet C - Bouton 5
        Program(68) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.48148),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

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
            ] >> Discard()
        ],
    jeannot >> ProgramFilter(2) >> [ # Refrain (meeeaaan) - Bouton 2
        Program(69) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.48148),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_on,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_on,

            bassscape,
            bassdegrade,
            ] >> Discard()
        ],
    orl >> ProgramFilter(7) >> [ # Couplet A (niggah don't you know) - Bouton 7
        Program(70) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 80),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.48148),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

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
            ] >> Discard()
        ],
    jeannot >> ProgramFilter(3) >> [ # Couplet Bbis (call your jesus) - Bouton 3
        Program(71) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 80),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.48148),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

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
            ] >> Discard()
        ],
    orl >> ProgramFilter(8) >> [ # Couplet Cbis (ain't no challenger left)- Bouton 8
        Program(72) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.48148),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

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
            ] >> Discard()
        ],

    orl >> ProgramFilter(9) >> [ # Ballade rhodes vocodeur - Bouton 10
        #TODO son rhodes
        stop,
        [

            vxorlgars_off,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_on,

            vxjeannotgars_off,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotdelay_on,
            vxjeannotvocode_on,

            ] >> Discard()
        ],
    jeannot >> ProgramFilter(4) >> [ # Sebkha 5/8 (batterie ternaire sur synthé, puis death sebkha, puis meshugagah)
        Program(73) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.48148),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxorlvocode_off,

            bassscape,
            bassdegrade,
            basswobble,

            ] >> Discard()
        ],
    ]
