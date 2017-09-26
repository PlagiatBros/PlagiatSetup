#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################

#### TrapOne ####
trapone = [
    Init([
        Program(seq24PageMap[6]) >> seq24once,
        Ctrl(0, 10) >> tapeutapecontrol,
        zynmicrotonal_off,
        SubSceneSwitch(2),
        SendOSC(mk2inport, '/mididings/switch_scene', 4),
        mk2lights([1,2,3,4,5,6,8]),
    ]),
    [jeannot_padrelease] >> mk2lights([1,2,3,4,5,6,8]),
    [orl, jeannot] >> ProgramFilter([range(1,12)]) >> [
        SendOSC(audioseqport, '/Audioseq/Sequence/Disable', '*'),
        SubSceneSwitch(2), # vx pedal
    ] >> Discard(),
    [orl, jeannot] >> ProgramFilter([range(2,12)]) >> [
        SendOSC(lightseqport, '/Lightseq/Sequence/Disable', '*'),
        SendOSC(lightseqport, '/Lightseq/Scene/Stop', '*'),
        SendOSC(vporlport, '/pyta/slide/visible', -1, 0),
        SendOSC(vpjeannotport, '/pyta/slide/visible', -1, 0),
        SendOSC(qlcstopport, '/Stop'),
    ] >> Discard(),
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    orl >> ProgramFilter(2) >> [ # intro bass
        stop,

        [

            SendOSC(slport, '/set', 'eighth_per_cycle', 33),
            SendOSC(slport, '/set', 'tempo', 120),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 33, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'X-x-x-x-X-x-x-x-xX-x-x-x-X-x-x-x-'),
            SendOSC(klickport, '/klick/metro/start'),

            bassdry,
            basswobble,

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

            SendOSC(bassmainport, '/strip/BassMain/Calf%20Filter/Frequency/unscaled', 71.),
            SendOSC(bassmainport, '/strip/BassDry/Calf%20Filter/Frequency/unscaled', 71.),
            SubSceneSwitch(1), # bass pedal
        ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
    ],
    orl >> ProgramFilter(3) >> [ # Couplet 1 (Levée) - Bouton 3
        Program(65) >> cseqtrigger,
        [
            SendOSC(audioseqport, '/Audioseq/Bpm', 120),
            SendOSC(audioseqport, '/Audioseq/Scene/Play', 'trapone_intro', timestamp),


            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(120)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(120)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(120)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(120)),

            SendOSC(bassmainport, '/strip/BassMain/Calf%20Filter/Frequency/unscaled', 20000.),
            SendOSC(bassmainport, '/strip/BassDry/Calf%20Filter/Frequency/unscaled', 20000.),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

                ]),

            bassdry,

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ],

        ],
    orl >> ProgramFilter(4) >> [ # Couplet 1  - Bouton 4
        Program(66) >> cseqtrigger,
        [
            SendOSC(audioseqport, '/Audioseq/Scene/Stop', 'trapone_altern_couplet', timestamp),
            SendOSC(audioseqport, '/Audioseq/Scene/Stop', 'trapone_altern_refrain', timestamp),
            SendOSC(audioseqport, '/Audioseq/Scene/Stop', 'trapone_altern_final', timestamp),

            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(trapcutport, '/Trapcut/Bpm', 240),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(120)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(120)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(120)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(120)),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),

            bassdry,

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ],

        ],
    jeannot >> ProgramFilter(2) >> [ # Couplet 1 (rattrapage) - Bouton 2
        SendOSC(56418, '/pedalBoard/button', 4) >> Discard(),
    ],
    jeannot >> ProgramFilter(3) >> [ # Refrain - Bouton 3 (rattrapage)
        SendOSC(56418, '/pedalBoard/button', 5)  >> Discard(),
    ],
    jeannot >> ProgramFilter(4) >> [ # Couplet Altern vers couplet - Bouton 4
        Program(67) >> cseqtrigger,
            [
                SendOSC(audioseqport, '/Audioseq/Bpm', 120),
                SendOSC(audioseqport, '/Audioseq/Scene/Play', 'trapone_altern_couplet', timestamp),
            ] >> Discard()
        ],
    jeannot >> ProgramFilter(5) >> [ # Couplet Altern vers refrain - Bouton 5
        Program(67) >> cseqtrigger,
        [
            SendOSC(audioseqport, '/Audioseq/Bpm', 120),
            SendOSC(audioseqport, '/Audioseq/Scene/Play', 'trapone_altern_refrain', timestamp),
        ] >> Discard()
        ],
    orl >> ProgramFilter(5) >> [ # Refrain - Bouton 5
        Program(68) >> cseqtrigger,
        [
            SendOSC(audioseqport, '/Audioseq/Scene/Stop', 'trapone_altern_couplet', timestamp),
            SendOSC(audioseqport, '/Audioseq/Scene/Stop', 'trapone_altern_refrain', timestamp),
            SendOSC(audioseqport, '/Audioseq/Scene/Stop', 'trapone_altern_final', timestamp),

            SendOSC(slport, '/set', 'eighth_per_cycle', 33),
            SendOSC(slport, '/set', 'tempo', 120),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 33, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'X-x-x-x-X-x-x-x-xX-x-x-x-X-x-x-x-'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(120)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(120)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(120)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(120)),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),

            bassdry,

            vxorlgars_on,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,
            ],

        ],
    jeannot >> ProgramFilter(6) >> [ # Couplet Altern vers fin - Bouton 6
        Program(67) >> cseqtrigger,
        SendOSC(audioseqport, '/Audioseq/Bpm', 120),
        SendOSC(audioseqport, '/Audioseq/Scene/Play', 'trapone_altern_final', timestamp),
        ],

    orl >> ProgramFilter(6) >> [ # Couplet 2  - Bouton 6
        Program(66) >> cseqtrigger,
        [
            SendOSC(audioseqport, '/Audioseq/Scene/Stop', 'trapone_altern_couplet', timestamp),
            SendOSC(audioseqport, '/Audioseq/Scene/Stop', 'trapone_altern_refrain', timestamp),
            SendOSC(audioseqport, '/Audioseq/Scene/Stop', 'trapone_altern_final', timestamp),

            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(trapcutport, '/Trapcut/Bpm', 240),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(120)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(120)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(120)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(120)),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),

            bassdry,

            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ],

        ],
    orl >> ProgramFilter(7) >> [ # Sortie (vers sonnerie de telephone) - Bouton 7
        Program(69) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            # SendOSC(klickport, '/klick/simple/set_tempo', 120),
            # SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            # SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'), #TODO ?? (instru qui sonne metronom déjà)
            # SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(120)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(120)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(120)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(120)),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),


            bassdry,

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_off,

            vxjeannotdelay_on,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            ] >> Discard()
        ],
    orl >> ProgramFilter(11) >> [ # SceneSwitch -> SW
        SceneSwitch(7) >> Discard(),
        Program(2) >> Output('PBCtrlOut', 1)
        ],
    jeannot >> ProgramFilter(8) >> SendOSC(trapcutport, '/Trapcut/Scene/Play', 'I') >> Discard(),

    ]
