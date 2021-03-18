#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################

sw_mk2lights = {
    1:'blue',
    2:'purple',
    3:'purple',
    4:'purple',
    5:'red',
    6:'blue',
    7:'yellow',
    8:'yellow',
}


#### SW ####
sw = [
    Init([
        Program(seq24PageMap[7]) >> seq24once,
        Ctrl(0, 4) >> tapeutapecontrol,

        disable_microtonal,
        # zynmicrotonal_off,

        SendOSC(mk2inport, '/mididings/switch_scene', 2),
        mk2lights(sw_mk2lights),
    ]),
    jeannot_padrelease >> mk2lights(sw_mk2lights),
    [orl, jeannot] >> ProgramFilter([range(1,12)]) >> [
        SendOSC(audioseqport, '/Audioseq/Sequence/Disable', '*')
    ] >> Discard(),
    orl >> ProgramFilter([range(2,12)]) >> light_reset >> Discard(),
    jeannot >> ProgramFilter([3]) >> light_reset >> Discard(),
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    orl >> ProgramFilter(2) >> [ # intro - Bouton 2
        #TODO filtre --> Degrade déjà en place ?
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(178.5)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(178.5)),


            SendOSC(rpicourport, '/pyta/scene_recall', 'dafist_couplet'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'dafist_couplet'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'no_budget_andra'),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'sw_intro'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 178.5),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),


            SendOscState([

                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],

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

            SendOSC(cmeinport, '/mididings/switch_scene', 9),

            bassdry,

            ] >> Discard()
        ],
    jeannot >> ProgramFilter(2) >> [ # Lanceur du Couplet (delais = 2 mesures) - Bouton 2
        [
            SendOSC(audioseqport, '/Audioseq/Bpm', 178.5),
            SendOSC(audioseqport, '/Audioseq/Scene/Play', 'sw_couplet_auto', timestamp),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'XxXx'),
            SendOSC(klickport, '/klick/metro/start'),


            SendOSC(rpicourport, '/pyta/scene_recall', 'dafist_couplet'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'dafist_couplet'),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'no_budget_pastis'),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'sw_couplet_auto_lights'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 178.5),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            ] >> Discard()
        ],
    orl >> ProgramFilter(3) >> [ # Couplet - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(178.5)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(178.5)),


            SendOSC(rpicourport, '/pyta/scene_recall', 'dafist_couplet'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'dafist_couplet'),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'sw_couplet1'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 178.5),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),


            SendOscState([

                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],
                [samplesdegradeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -3.0],
                [samplesscapeport, '/strip/SamplesDegrade/Gain/Gain%20(dB)/unscaled', -18.0],

            ]),


            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_off,
            SendOSC(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 1.0),

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry,

            ] >> Discard()
        ],
    jeannot >> ProgramFilter(3) >> [ # Break + delay vers orl-bouton 4 -  Bouton 3
        Program(5) >> cseqtrigger,
        [
            SendOSC(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 1.0),
            SendOSC(audioseqport, '/Audioseq/Scene/Play', 'sw_couplet_break1', timestamp),
            ] >> Discard()
        ],

    orl >> ProgramFilter(4) >> [ # Couplet funk- Bouton 4
        Program(68) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(178.5)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(178.5)),


            SendOSC(rpicourport, '/pyta/scene_recall', 'dafist_couplet'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'dafist_couplet'),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'sw_couplet1'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 178.5),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),


            SendOscState([

                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],
                [samplesdegradeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -3.0],
                [samplesscapeport, '/strip/SamplesDegrade/Gain/Gain%20(dB)/unscaled', -18.0],

            ]),


            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_off,
            SendOSC(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 1.0),

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry,

            ] >> Discard()
        ],

    jeannot >> ProgramFilter(4) >> [ # Break + delay vers orl-bouton 5 - Bouton 4
        Program(5) >> cseqtrigger,
        NoteOn(40, 127) >> Output('PBTapeutape', 1),
        [
            SendOSC(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 1.0),
            SendOSC(audioseqport, '/Audioseq/Scene/Play', 'sw_couplet_break2', timestamp),

            ] >> Discard()
        ],

    orl >> ProgramFilter(5) >> [ # Couplet latin - Bouton 5
        Program(69) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(178.5)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(178.5)),


            SendOSC(rpicourport, '/pyta/scene_recall', 'dafist_couplet'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'dafist_couplet'),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'sw_couplet1'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 178.5),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),


            SendOscState([

                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],
                [samplesdegradeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -3.0],
                [samplesscapeport, '/strip/SamplesDegrade/Gain/Gain%20(dB)/unscaled', -18.0],

            ]),


            vxorlgars_off,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_on,
            SendOSC(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 1.0),

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry,

            ] >> Discard()
        ],

    orl >> ProgramFilter(6) >> [ # Quintes au lait - Bouton 6
        Program(70) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(178.5)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(178.5)),

            SendOSC(rpicourport, '/pyta/scene_recall', 'dafist_couplet'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'dafist_couplet'),

            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'sw_refrain_red_flashes'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'sw_refrain_white_flash'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 178.5),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -4.5],

            ]),

            vxorlgars_off,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_on,

            vxjeannotgars_on,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotdelay_off,
            vxjeannotvocode_on,


            bassdry,
            bassdisto,


            ] >> Discard()
        ],
    orl >> ProgramFilter(7) >> [ # Refrain - Bouton 7
        Program(71) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(178.5)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(178.5)),

            SendOSC(rpicourport, '/pyta/scene_recall', 'dafist_couplet'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'dafist_couplet'),

            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'sw_refrain_red_flashes'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'sw_refrain_white_flash'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 178.5),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
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


            bassdry,
            bassdisto,


            ] >> Discard()
        ],

    orl >> ProgramFilter(8) >> [ # break vers Couplet 2 - Bouton 8
        Program(65) >> cseqtrigger,
        [
            SendOSC(audioseqport, '/Audioseq/Bpm', 178.5),
            SendOSC(audioseqport, '/Audioseq/Scene/Play', 'sw_couplet_auto2', timestamp),

            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(178.5)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(178.5)),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'sw_intro'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 178.5),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            SendOscState([

                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],
                [samplesdegradeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -3.0],
                [samplesscapeport, '/strip/SamplesDegrade/Gain/Gain%20(dB)/unscaled', -18.0],

                [vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 1.0],
                [surfaceorlport, '/strip/VxORLDelayPre/Gain/Mute', 1.0],
            ]),


            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry

            ] >> Discard()
        ],
    orl >> ProgramFilter(81) >> [ # Couplet 2 trompette - Bouton 9
        Program(72) >> cseqtrigger,
        [

            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(178.5)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(178.5)),

            SendOscState([

                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],

            ]),


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

            bassdry

            ] >> Discard()
        ],
    orl >> ProgramFilter(9) >> [ # DnB - Bouton 10
        Program(73) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(178.5)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(178.5)),

            SendOSC(rpicourport, '/pyta/scene_recall', 'dafist_couplet'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'dafist_couplet'),

            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'sw_refrain_red_flashes'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'sw_refrain_white_flash'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 178.5),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),


            SendOscState([

                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],

            ]),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_on,
            vxjeannotdelay_on,
            vxjeannotvocode_off,


            bassdry,

            ] >> Discard()
        ],
        orl >> ProgramFilter(10) >> [ # Lmabo Trap - Bouton 8
            SendOSC(cmeinport, '/mididings/switch_scene', 16),
            Program(74) >> cseqtrigger,
            [
                SendOSC(slport, '/set', 'eighth_per_cycle', 8),
                SendOSC(slport, '/set', 'tempo', 178.5),
                SendOSC(slport, '/sl/-1/hit', 'pause_on'),

                SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
                SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
                SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
                SendOSC(klickport, '/klick/metro/start'),

                SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(178.5)),
                SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(178.5)),
                SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(178.5)),
                SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(178.5)),

                SendOSC(rpicourport, '/pyta/scene_recall', 'dafist_couplet'),
                SendOSC(rpijardinport, '/pyta/scene_recall', 'dafist_couplet'),

                SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'sw_refrain_red_flashes'),
                SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'sw_refrain_white_flash'),

                SendOSC(lightseqport, '/Lightseq/Bpm', 178.5),
                SendOSC(lightseqport, '/Lightseq/Play', timestamp),


                SendOscState([

                    [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                    [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                    [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],
                    [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -6.0],

                ]),

                vxorlgars_on,
                vxorlmeuf_off,
                vxorldisint_off,
                vxorldelay_off,
                vxorlvocode_off,

                vxjeannotgars_off,
                vxjeannotmeuf_off,
                vxjeannotdisint_off,
                vxjeannotdelay_off,
                vxjeannotvocode_on,

                bassdry,

                ] >> Discard()
            ],

    jeannot >> ProgramFilter(5) >> [ # alarme  dnb -  Bouton 5
        Program(70) >> seq24once,
        ],

    jeannot >> ProgramFilter(6) >> [ # stop Three get the shit going- Bouton 6
        stop,
        [

            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(178.5)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(178.5)),

            SendOscState([

                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/SamplesDegrade/Gain/Gain%20(dB)/unscaled', -18.0],

            ]),


            vxorlgars_off,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_on,

            vxjeannotgars_off,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotdelay_off,
            vxjeannotvocode_on,

            SendOSC(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 1.0),
            SendOSC(vxjeannotpreport, '/strip/VxJeannotDelayPre/Gain/Mute', 1.0),

            SendOSC(audioseqport, '/Audioseq/Bpm', 178.5),
            SendOSC(audioseqport, '/Audioseq/Scene/Play', 'sw_shit_going', timestamp),

            ] >> Discard()
        ],

    jeannot >> ProgramFilter(7) >> [
        vxjeannotdelay_off,
        vxjeannotgars_on,
        vxjeannotmeuf_off,
        vxjeannotdisint_off,
        vxjeannotvocode_off,
    ] >> Discard(),
    jeannot >> ProgramFilter(8) >> [
        vxjeannotgars_off,
        vxjeannotmeuf_off,
        vxjeannotdisint_off,
        vxjeannotdelay_off,
        vxjeannotvocode_on,
    ] >> Discard(),


    orl >> ProgramFilter(11) >> [ # SlowMotium
        SceneSwitch(8) >> Discard(),
        Program(2) >> Output('PBCtrlOut', 1)
        ],

    ]
