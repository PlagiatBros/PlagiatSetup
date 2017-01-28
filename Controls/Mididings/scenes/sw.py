#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################

#### SW ####
sw = [
    [orl, jeannot] >> Filter(PROGRAM) >> Ctrl(0, 4) >> tapeutapecontrol,
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    orl >> ProgramFilter(2) >> [ # intro - Bouton 2
        #TODO filtre
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
            vxjeannotvocode_off,
            ] >> Discard()
        ],
    jeannot >> ProgramFilter(2) >> [ # [delay] Lanceur du Couplet - Bouton 2
        [

            SendOSC(audioseqport, '/Audioseq/Bpm', 178.5),
            SendOSC(audioseqport, '/Audioseq/Scene/Play', 'sw_couplet_auto'),

            ] >> Discard()
        ],
    orl >> ProgramFilter(3) >> [ # Couplet - Bouton 3
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
            vxjeannotvocode_off,
            ] >> Discard()
        ],

    orl >> ProgramFilter(4) >> [ # Refrain - Bouton 4
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

            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_on,
            vxjeannotdelay_on,
            vxjeannotvocode_off,

            ] >> Discard()
        ],

    orl >> ProgramFilter(5) >> [ # Couplet 2 - Bouton 5
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
            vxjeannotvocode_off,
            ] >> Discard()
        ],

    jeannot >> ProgramFilter(3) >> [ # stop Three get the shit going- Bouton 3
        Program(65) >> cseqtrigger,
        [
            stop,

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
            vxorldisint_on,
            vxorldelay_on,
            vxorlvocode_off,

            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_on,
            vxjeannotdelay_on,
            vxjeannotvocode_off,

            SendOSC(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 1.0),
            SendOSC(vxjeannotpreport, '/strip/VxJeannotDelayPre/Gain/Mute', 1.0),

            SendOSC(audioseqport, '/Audioseq/Bpm', 178.5),
            SendOSC(audioseqport, '/Audioseq/Scene/Play', 'sw_shit_going'),

            ] >> Discard()
        ],


    ]
