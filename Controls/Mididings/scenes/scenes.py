#encoding: utf-8

import sys
sys.path.append('..')

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC


#### Scenes ################################################

#### Climat ####
climat = PortFilter('PBCtrlIn') >> [
    Filter(PROGRAM) >> Ctrl(0, 0) >> tapeutapecontrol,
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Couplet - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 74),
            SendOSC(slport, '/set', 'tempo', 150),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 74, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'X.x.x.x.X.x.x.x.X.x.x.x.Xxx.x.x.X.x.x.xX.x.x.x.X.x.x.x.X.x.xxx.X.x.x.x.X.x'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.8955),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.8955),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.4444),


            SendOscState([
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -7.0],
                [samplesreversedelayport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -2.0],
                [samplesringmodport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -2.0],
            ]),



            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,


            ] >> Discard()
        ],
    ProgramFilter(3) >> [ # Refrain - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 74),
            SendOSC(slport, '/set', 'tempo', 150),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 74, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'X.x.x.x.X.x.x.x.X.x.x.x.Xxx.x.x.X.x.x.xX.x.x.x.X.x.x.x.X.x.xxx.X.x.x.x.X.x'),
#            SendOSC(klickport, '/klick/simple/set_pattern', 'X.x.x.x.X.x.x.x.X.x.x.x.X.x.x.x.X.x.x.xX.x.x.x.X.x.x.x.X.x.x.x.X.x.x.x.X.x'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.8955),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.8955),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.4444),

            SendOscState([

                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplestremoloport, '/strip/SamplesTremolo/Gain/Gain%20(dB)/unscaled', -6.0],
                [samplesscapeport, '/strip/SamplesTremolo/Gain/Gain%20(dB)/unscaled', -7.50],
                [samplestremoloport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -18.],
                [samplestremoloport, '/strip/SamplesPitch/Gain/Gain%20(dB)/unscaled', 0.0],
                [samplesscapeport, '/strip/SamplesPitch/Gain/Gain%20(dB)/unscaled', -7.50],
                [samplespitchport, '/strip/SamplesPitch1/AM%20pitchshifter/Pitch%20shift/unscaled', 2],
                [samplespitchport, '/strip/SamplesPitch2/AM%20pitchshifter/Pitch%20shift/unscaled', 2.3],
                [samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -7.0],
                [samplesringmodport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -2.0],

            ]),

            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,

            ] >> Discard()
        ],

    ProgramFilter(4) >> [ # The shit - Bouton 4
        Program(67) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 150),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),


            SendOscState([

                [bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.8955],
                [samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.8955],
                [samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.4444],

                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplestremoloport, '/strip/SamplesTremolo/Gain/Gain%20(dB)/unscaled', -6.0],
                [samplesscapeport, '/strip/SamplesTremolo/Gain/Gain%20(dB)/unscaled', -7.50],
                [samplestremoloport, '/strip/Samples5/Gain/Gain%20(dB)/unscaled', -6.],
                [samplespitchport, '/strip/SamplesPitch1/AM%20pitchshifter/Pitch%20shift/unscaled', 2],
                [samplespitchport, '/strip/SamplesPitch2/AM%20pitchshifter/Pitch%20shift/unscaled', 2.3],
            ]),


            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_on,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_on,

            ] >> Discard()
        ],

    ProgramFilter(5) >> [ # Transe Pédé - Bouton 5
        Program(68) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 74),
            SendOSC(slport, '/set', 'tempo', 150),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 74, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'X.x.x.x.X.x.x.x.X.x.x.x.Xxx.x.x.X.x.x.xX.x.x.x.X.x.x.x.X.x.xxx.X.x.x.x.X.x'),
#            SendOSC(klickport, '/klick/simple/set_pattern', 'X.x.x.x.X.x.x.x.X.x.x.x.X.x.x.x.X.x.x.xX.x.x.x.X.x.x.x.X.x.x.x.X.x.x.x.X.x'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.8955),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.8955),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.4444),

            SendOscState([

                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplestremoloport, '/strip/SamplesTremolo/Gain/Gain%20(dB)/unscaled', -6.0],
                [samplesscapeport, '/strip/SamplesTremolo/Gain/Gain%20(dB)/unscaled', -7.50],
                [samplestremoloport, '/strip/Samples5/Gain/Gain%20(dB)/unscaled', -6.],
                [samplespitchport, '/strip/SamplesPitch1/AM%20pitchshifter/Pitch%20shift/unscaled', 2],
                [samplespitchport, '/strip/SamplesPitch2/AM%20pitchshifter/Pitch%20shift/unscaled', 2.3],

            ]),


            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,

            ] >> Discard()
        ],

    ProgramFilter(6) >> [ # Transe Pédé (2) - Bouton 6
        [


            SendOscState([

                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplestremoloport, '/strip/SamplesTremolo/Gain/Gain%20(dB)/unscaled', -6.0],
                [samplesscapeport, '/strip/SamplesTremolo/Gain/Gain%20(dB)/unscaled', -7.50],
                [samplestremoloport, '/strip/Samples5/Gain/Gain%20(dB)/unscaled', -6.],
                [samplestremoloport, '/strip/SamplesPitch/Gain/Gain%20(dB)/unscaled', -70.0],
                [samplesscapeport, '/strip/SamplesPitch/Gain/Gain%20(dB)/unscaled', -7.50],
                [samplespitchport, '/strip/SamplesPitch1/AM%20pitchshifter/Pitch%20shift/unscaled', 2],
                [samplespitchport, '/strip/SamplesPitch2/AM%20pitchshifter/Pitch%20shift/unscaled', 2.3],
                [samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -7.0],
                [samplesringmodport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -2.0],

            ]),

            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,

            ] >> Discard()
        ],

    ProgramFilter(7) >> [ # Transe Pédé (2) - Bouton 7
        [

            SendOscState([

                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 0.0],

                [samplestremoloport, '/strip/SamplesTremolo/Gain/Gain%20(dB)/unscaled', -6.0],
                [samplesscapeport, '/strip/SamplesTremolo/Gain/Gain%20(dB)/unscaled', -7.50],
                [samplestremoloport, '/strip/Samples5/Gain/Gain%20(dB)/unscaled', -6.],
                [samplestremoloport, '/strip/SamplesPitch/Gain/Gain%20(dB)/unscaled', -5.0],
                [samplesscapeport, '/strip/SamplesPitch/Gain/Gain%20(dB)/unscaled', -7.50],
                [samplespitchport, '/strip/SamplesPitch1/AM%20pitchshifter/Pitch%20shift/unscaled', 2],
                [samplespitchport, '/strip/SamplesPitch2/AM%20pitchshifter/Pitch%20shift/unscaled', 2.3],
                [samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -7.0],
                [samplesringmodport, '/strip/Samples5/Gain/Gain%20(dB)/unscaled', -12.0],
            ]),

            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,

            ] >> Discard()
        ],

    ]

#### ConnassesSACEM ####
connassessacem = PortFilter('PBCtrlIn') >> [
    Filter(PROGRAM) >> Ctrl(0, 1) >> tapeutapecontrol,
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Thème Intro - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 125),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 125),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.708955),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.708955),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.35185),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -7.0],

            ]),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_off,

            vxjeannotdelay_on,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,

            ] >> Discard()
        ],
    ProgramFilter(3) >> [ # Thème Intro - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 125),

            SendOSC(klickport, '/klick/simple/set_tempo', 125),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.708955),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.708955),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.35185),

            SendOscState([
                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB]/unscaled', -7.0],

            ]),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_off,

            vxjeannotdelay_on,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,

            ] >> Discard()
        ],

    ]


#### Fifty ####
fifty = PortFilter('PBCtrlIn') >> [
    Filter(PROGRAM) >> Ctrl(0, 2) >> tapeutapecontrol,
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Couplet - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 64),
            SendOSC(slport, '/set', 'tempo', 117),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 117),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.64925),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.64925),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.32222),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB]/unscaled', -7.0],

            ]),


            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,

            ] >> Discard()
        ],
    ProgramFilter(3) >> [ # Pont Refrain - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 117),

            SendOSC(klickport, '/klick/simple/set_tempo', 117),
            SendOSC(klickport, '/klick/simple/set_meter', 3, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.64925),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.64925),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.32222),


            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOscState([

                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),

            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            ] >> Discard()
        ],
    ProgramFilter(4) >> [ # Refrain - Bouton 4
        Program(67) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 117),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 117),
            SendOSC(klickport, '/klick/simple/set_meter', 3, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.64925),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.64925),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.32222),

            SendOscState([

                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),

            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,

            ] >> Discard()
        ],
    ProgramFilter(5) >> [ # Couplet avec boucle - Bouton 5
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 64),
            SendOSC(slport, '/set', 'tempo', 117),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),
            SendOSC(slport, '/sl/0/set', 'play_sync', 0),
            SendOSC(slport, '/sl/0/hit', 'pause_off'),
            SendOSC(slport, '/sl/0/hit', 'trigger'),
            SendOSC(slport, '/sl/0/set', 'play_sync', 1),

            SendOSC(klickport, '/klick/simple/set_tempo', 117),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.64925),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.64925),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.32222),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB]/unscaled', -7.0],

            ]),


            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,

            ] >> Discard()
        ],
    ProgramFilter(6) >> [ # Boucle rationnelle - Bouton 6
        Program(68) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 64),
            SendOSC(slport, '/set', 'tempo', 117),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 117),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.64925),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.64925),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.32222),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB]/unscaled', -7.0],

            ]),


            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,

            ] >> Discard()
        ],

    ]

#### Le5 ####
le5 = PortFilter('PBCtrlIn') >> [
    Filter(PROGRAM) >> Ctrl(0, 3) >> tapeutapecontrol,
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Intro - Bouton 2
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

            bassdry,
            ] >> Discard()
        ],
    ProgramFilter(3) >> [ # Couplet A - Bouton 3
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

            bassdry,
            ] >> Discard()
        ],
    ProgramFilter(4) >> [ # Couplet B - Bouton 4
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

            bassdry,
            ] >> Discard()
        ],
    ProgramFilter(5) >> [ # Couplet C - Bouton 5
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

            bassdry,
            ] >> Discard()
        ],
    ProgramFilter(6) >> [ # Refrain - Bouton 6
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
    ProgramFilter(7) >> [ # Couplet A - Bouton 7 - #TODO INUTILE?
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

            bassdry,
            ] >> Discard()
        ],
    ProgramFilter(8) >> [ # Couplet Bbis - Bouton 8
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
            ] >> Discard()
        ],
    ProgramFilter(9) >> [ # Couplet Cbis - Bouton 9
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
            ] >> Discard()
        ],

    ProgramFilter(10) >> [ # Transe Pédé - Bouton 10
        Program(73) >> cseqtrigger,
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

                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 0.0],
                [samplesdegradeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -12.0],
                [samplesdegradeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -9.0],
                [samplesdegradeport, '/strip/SamplesTremolo/Gain/Gain%20(dB)/unscaled', -6.0],
                [samplestremoloport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -6.0],

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
            ] >> Discard()
        ],

    ProgramFilter(11) >> [ # Transe Pédé - Bouton 11
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
                [samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 0.0],

                [samplesdegradeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -12.0],
                [samplesdegradeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -9.0],
                [samplesdegradeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -4.0],
                [samplesdisintegratorport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -4.0],
                [samplestremoloport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -6.0],
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
            ] >> Discard()
        ],
    ]


#### SW ####
sw = PortFilter('PBCtrlIn') >> [
    Filter(PROGRAM) >> Ctrl(0, 4) >> tapeutapecontrol,
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Couplet - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.44216),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.44216),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.55),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, 0.55),

            SendOscState([

                [samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesdegradeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -3.0],
                [samplesscapeport, '/strip/SamplesDegrade/Gain/Gain%20(dB)/unscaled', -18.0],

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
            ] >> Discard()
        ],
    ProgramFilter(3) >> [ # Couplet - Bouton 3
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.44216),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.44216),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.55),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, 0.55),

            SendOscState([

                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],
                [samplesdegradeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -3.0],
                [samplesscapeport, '/strip/SamplesDegrade/Gain/Gain%20(dB)/unscaled', -18.0],

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
            ] >> Discard()
        ],

    ProgramFilter(4) >> [ # Refrain - Bouton 4
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.44216),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.44216),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.55),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, 0.55),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -4.5],

            ]),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_on,
            vxorldelay_on,
            vxorlvocode_off,

            vxjeannotdelay_on,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_on,
            ] >> Discard()
        ],

    ProgramFilter(5) >> [ # Couplet - Bouton 5
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.44216),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.44216),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.55),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, 0.55),

            SendOscState([

                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/SamplesDegrade/Gain/Gain%20(dB)/unscaled', -18.0],

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
            ] >> Discard()
        ],

    ]

#### Whole World ####
wholeworld = PortFilter('PBCtrlIn') >> [
    Filter(PROGRAM) >> Ctrl(0, 5) >> tapeutapecontrol,
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Couplet - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 90),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 90),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.44776),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.44776),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.2222),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -6.0],

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
            ] >> Discard()
        ],
    ProgramFilter(3) >> [ # Refrain - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 90),

            SendOSC(klickport, '/klick/simple/set_tempo', 90),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.44776),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.44776),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.2222),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -6.0],

            ]),

            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            ] >> Discard()
        ],
    ProgramFilter(4) >> [ # Pont - Bouton 4
        Program(67) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 90),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 90),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.44776),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.44776),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.2222),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -6.0],

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
            ] >> Discard()
        ],

    ProgramFilter(5) >> [ # Pont - Bouton 5
        Program(68) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 90),

            SendOSC(klickport, '/klick/simple/set_tempo', 90),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.44776),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.44776),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.2222),

            SendOscState([

                [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -6.0],

            ]),

            vxorlgars_on,
            vxorlmeuf_on,
            vxorldisint_on,
            vxorldelay_on,
            vxorlvocode_off,

            vxjeannotdelay_on,
            vxjeannotgars_on,
            vxjeannotmeuf_on,
            vxjeannotdisint_on,

            bassscape,
            bassdegrade,
            ] >> Discard()
        ],
    ]

#### Da Fist ####
dafist = PortFilter('PBCtrlIn') >> [
    Filter(PROGRAM) >> Ctrl(0, 6) >> tapeutapecontrol,
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Intro Thème - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.3333),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
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
            ] >> Discard()
        ],
    ProgramFilter(3) >> [ # Intro Thème 2 - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.3333),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -5.0],

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
            ] >> Discard()
        ],
    ProgramFilter(4) >> [ # Couplet - Bouton 4
        Program(67) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.3333),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -5.0],
                [samplesscapeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -10.0],
                [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -9.0],

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
            ] >> Discard()
        ],
    ProgramFilter(5) >> [ # Couplet part 2 - Bouton 5
        Program(68) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.3333),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -5.0],

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
            ] >> Discard()
        ],
    ProgramFilter(6) >> [ # Intro Refrain - Bouton 6
        Program(69) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.3333),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -5.0],

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
            ] >> Discard()
        ],
    ProgramFilter(7) >> [ # Refrain - Bouton 7
        Program(70) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.3333),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -5.0],

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
            ] >> Discard()
        ],

    ProgramFilter(8) >> [ # Refrain - Bouton 8
        Program(71) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.3333),

            SendOscState([

                [samplesscapeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -5.0],

            ]),


            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_off,

            vxjeannotdelay_on,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,

            bassscape,
            ] >> Discard()
        ],
    ]


#### Get Ur Freak On ####
geturfreakon = PortFilter('PBCtrlIn') >> [
    Filter(PROGRAM) >> Ctrl(0, 7) >> tapeutapecontrol,
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Couplet - Bouton 2
#        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 200),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

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
            ] >> Discard()
        ],
    ProgramFilter(3) >> [ # Couplet - Bouton 3
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
            ] >> Discard()
        ],
    ]

#### SlowMotium ####
slowmotium = PortFilter('PBCtrlIn') >> [
    Filter(PROGRAM) >> Ctrl(0, 8) >> tapeutapecontrol,
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Couplet - Bouton 2
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
    ProgramFilter(3) >> [ # Couplet - Bouton 3
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

    ProgramFilter(4) >> [ # Couplet - Bouton 4
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

#### HorroCore ####
horrorcore = PortFilter('PBCtrlIn') >> [
    Filter(PROGRAM) >> Ctrl(0, 9) >> tapeutapecontrol,
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Couplet - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 200),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

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
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_on,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            ] >> Discard()
        ],

    ]

#### TrapOne ####
trapone = PortFilter('PBCtrlIn') >> [
    Filter(PROGRAM) >> Ctrl(0, 10) >> tapeutapecontrol,
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Couplet - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 17),
            SendOSC(slport, '/set', 'tempo', 120),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 17, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'X-x-x-x-X-x-x-x-x'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.522388),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.522388),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.6296),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),


            vxorlgars_off,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_on,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            ] >> Discard()
        ],

    ]
