#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################

le5_mk2lights = {
    1:'blue',
    2:'purple',
    3:'white',
    4:'white',
    5:'purple',
    6:'purple',
    8:'red',
}

#### Le5 ####
le5 = [
    Init([
        Program(seq24PageMap[5]) >> seq24once,
        Ctrl(0, 3) >> tapeutapecontrol,

        enable_microtonal,
        set_microtonal(0, 0.35, 0, 0.35, 0, 0, 0, 0, 0.35, 0, 0, 0),
        # zynmicrotonal_on,
        # SendOSC(zyntrebleport, '/microtonal/tunings', '100.0\n200.0\n300.0\n435.0\n500.0\n635.0\n700.0\n800.0\n900.0\n1000.0\n1135.0\n2/1'),

        SendOSC(mk2inport, '/mididings/switch_scene', 1),
        mk2lights(le5_mk2lights),
        ]),
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    jeannot_padrelease >> mk2lights(le5_mk2lights),
    [orl, jeannot] >> ProgramFilter([range(1,12)]) >> [
        SendOSC(audioseqport, '/Audioseq/Sequence/Disable', '*'),
        SendOSC(samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.),
        SendOSC(vxmainport, '/strip/VxJeannotMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.),
        SendOSC(vxmainport, '/strip/VxORLMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.),
        SendOSC(bassmainport, '/strip/BassMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.),
        SendOSC(samplesmainport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled',20000.),

    ] >> Discard(),
    orl >> ProgramFilter([range(2,12)]) >> light_reset >> Discard(),
    jeannot >> ProgramFilter([range(2,7)]) >> light_reset >> Discard(),
    jeannot >> ProgramFilter(2) >> [ # Intro Shut your dickhole + break fitting me suit - Bouton 2
        Program(65) >> cseqtrigger,
        NoteOn(66,127) >> Output('PBTapeutape', 3), # gunshot
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(160)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(160)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(160)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(160)),


            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_ballade'),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_shotgun'),
            SendOSC(lightseqport, '/Lightseq/Bpm', 160 * 2),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_on,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry,
            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,
            ]
        ],
    orl >> ProgramFilter(2) >> [ # Couplet A - Bouton 2
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(160)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(160)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(160)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(160)),


            SendOSC(rpicourport, '/pyta/scene_recall', 'le5_couplet1'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'le5_couplet1'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_couplet1', 1),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_couplet1_part1_fixe'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_couplet1_anim1'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 160 * 2),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

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

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,
            ]
        ],
    jeannot >> ProgramFilter(3) >> [ # Stop vers Before Me - Bouton 3

            stop,
            SendOSC(rpicourport, '/pyta/scene_recall', 'climat_cock'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'climat_cock'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_climax_cock'),
            SendOSC(audioseqport, '/Audioseq/Scene/Play', 'le5_cock'),
            NoteOn(65,127) >> Output('PBTapeutape', 3),
    ],
    jeannot >> ProgramFilter(4) >> [ # Before Me - Bouton 4
        Program(65) >> cseqtrigger,
        NoteOn(66,127) >> Output('PBTapeutape', 3), # gunshot
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(160)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(160)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(160)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(160)),


            SendOSC(rpicourport, '/pyta/scene_recall', 'le5_couplet1_before_cour'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'le5_couplet1_before_jardin'),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_couplet1_before_me'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 160 * 2),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_on,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry,
            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,
            ]
        ],
    orl >> ProgramFilter(3) >> [ # Couplet B - Bouton 3
        Program(67) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(160)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(160)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(160)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(160)),



            SendOSC(rpicourport, '/pyta/scene_recall', 'le5_couplet1'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'le5_couplet1'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_couplet1', 2),


            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_couplet1_part1_fixe'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_couplet1_anim2'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 160 * 2),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

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

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],
    orl >> ProgramFilter(4) >> [ # Couplet C (salted) - Bouton 4
        Program(68) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(160)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(160)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(160)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(160)),

            SendOSC(rpicourport, '/pyta/scene_recall', 'le5_couplet1'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'le5_couplet1'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_couplet1', 3),


            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_couplet1_part1_fixe'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_couplet1_anim3'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 160 * 2),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),


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

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],
    jeannot >> ProgramFilter(5) >> [ # Refrain (meeeaaan) - Bouton 3
        Program(69) >> cseqtrigger,
        [
            SendOSC(audioseqport, '/Audioseq/Bpm', 320),
            SendOSC(audioseqport, '/Audioseq/Play', timestamp),
            SendOSC(audioseqport, '/Audioseq/Sequence/Enable', 'le5_refrain_cutdown'),

            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(160)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(160)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(160)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(160)),


            SendOSC(rpicourport, '/pyta/scene_recall', 'le5_refrain_mean'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'le5_refrain_mean'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_refrain_mean'),


            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_refrain_anim'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 160 * 2),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

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

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,
            ]
        ],
    orl >> ProgramFilter(5) >> [ # Couplet A (niggah don't you know) - Bouton 5
        Program(70) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 80),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(160)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(160)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(160)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(160)),



            SendOSC(rpicourport, '/pyta/scene_recall', 'le5_niglou'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'le5_niglou'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_niglou'),


            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_couplet2_nigro'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 160 * 2),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

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

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],
    jeannot >> ProgramFilter(6) >> [ # Couplet Bbis (call your jesus) - Bouton 4
        Program(71) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 80),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(trapcutport, '/Trapcut/Bpm', 320),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(160)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(160)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(160)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(160)),

            SendOSC(rpicourport, '/pyta/scene_recall', 'le5_trap'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'le5_trap'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_trap_jesus'),


            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_couplet2_trap'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_couplet2_trap_anim'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 160 * 2),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),


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

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],
    orl >> ProgramFilter(6) >> [ # Couplet Cbis (ain't no challenger left)- Bouton 6
        Program(72) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(160)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(160)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(160)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(160)),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(160)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(160)),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(160)),



            SendOSC(rpicourport, '/pyta/scene_recall', 'le5_couplet1'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'le5_couplet1'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_couplet1', 4),


            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_couplet2_anim4'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 160 * 2),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

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

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],
    orl >> [ProgramFilter(7), ProgramFilter(11)] >> [ # Nymphotrap
        SceneSwitch(6) >> Discard(),
        Program(2) >> Output('PBCtrlOut', 1)
        ],
    jeannot >> ProgramFilter(8) >> [
        SendOSC(trapcutport, '/Trapcut/Scene/Play', 'I') >> Discard(),
        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_trapcup'),
    ],
]
