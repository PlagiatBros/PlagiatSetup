#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################


#### Climat ####
climat = [
    [orl, jeannot] >> Filter(PROGRAM) >> Ctrl(0, 0) >> tapeutapecontrol,
    orl >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    orl >> ProgramFilter(2) >> [ # Couplet - Bouton 2
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
    orl >> ProgramFilter(3) >> [ # Refrain - Bouton 3
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

    orl >> ProgramFilter(4) >> [ # The shit - Bouton 4
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

    orl >> ProgramFilter(5) >> [ # Transe Pédé - Bouton 5
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

    orl >> ProgramFilter(6) >> [ # Transe Pédé (2) - Bouton 6
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

    orl >> ProgramFilter(7) >> [ # Transe Pédé (2) - Bouton 7
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
