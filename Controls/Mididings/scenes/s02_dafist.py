#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################

smokes = " ".join(['Smoke_'+str(i) for i in range(1,20)])

dafist_mk2lights = {
    1:'blue',
    2:'purple',
    3:'purple',
    4:'purple',
    5:'green',
    6:'purple',
    7:'yellow',
    8:'yellow',
}



#### Da Fist ####
dafist = [
    Init([
        Program(seq24PageMap[2]) >> seq24once,
        Ctrl(0, 6) >> tapeutapecontrol,

        enable_microtonal,
        set_microtonal(0, 0, 0, 0, 0, 0.35, 0, 0, 0.35, 0, 0.35, 0),
        # zynmicrotonal_on,
        # SendOSC(zyntrebleport, '/microtonal/tunings', '135.0\n200.0\n300.0\n400.0\n500.0\n600.0\n700.0\n835.0\n900.0\n1000.0\n1135.0\n2/1'),

        SendOSC(mk2inport, '/mididings/switch_scene', 8),

        mk2lights(dafist_mk2lights),

        ]),
    jeannot_padrelease >> mk2lights(dafist_mk2lights),
    [orl, jeannot] >> ProgramFilter([range(1,12)]) >> [
        SendOSC(audioseqport, '/Audioseq/Sequence/Disable', '*')
    ] >> Discard(),
    orl >> ProgramFilter([range(2,9)]) >> light_reset >> Discard(),
    jeannot >> ProgramFilter([2,3,4,6]) >> light_reset >> Discard(),
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #

    orl >> ProgramFilter(2) >> [ # Intro - Bouton 2
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(120)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(120)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(120)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(120)),


            SendOSC(rpicourport, '/pyta/scene_recall', 'dafist_intro'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'dafist_intro'),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'dafist_intro_fixe'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'dafist_battements_intensity'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_intro_anim'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 120),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),


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
            vxjeannotvocode_off,

            SendOSC(cmeinport, '/mididings/switch_scene', 7),

            ] >> Discard()
        ],
    jeannot >> ProgramFilter(2) >> [ # Psychose - Bouton 2
        Program(69) >> cseqtrigger,
        [
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


            SendOSC(rpicourport, '/pyta/scene_recall', 'dafist_psychose'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'dafist_psychose'),

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
            vxjeannotvocode_off,

            bassdry,
            bassdetunest_on,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,

            ] >> Discard()
        ],
    jeannot >> ProgramFilter(3) >> [ # Refrain - Bouton 3
        Program(70) >> cseqtrigger,
        [
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


            SendOSC(rpicourport, '/pyta/scene_recall', 'dafist_refrain'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'dafist_refrain'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_refrain'),

            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_refrain_anim'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 120),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),


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
            vxjeannotvocode_off,

            bassdry,
            bassdetunest_on,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,

            SendOSC(cmeinport, '/mididings/switch_scene', 5),

            ] >> Discard()
        ],
    orl >> ProgramFilter(3) >> [ # Couplet - Bouton 3
        Program(67) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(120)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(120)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(240)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(120)),


            SendOSC(lightseqport, '/Lightseq/Bpm', 120),

            # video
            SendOSC(rpicourport, '/pyta/scene_recall', 'dafist_couplet'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'dafist_couplet'),

            # light
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'dafist_couplet_firstpart_fixe'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_couplet_anim1'),

            SendOSC(lightseqport, '/Lightseq/Play', timestamp),



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


            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,
            vxjeannotverb_on,

            SendOSC(cmeinport, '/mididings/switch_scene', 9),

            bassdry,
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,


            ] >> Discard()
        ],
    jeannot >> ProgramFilter(5) >> [ # "Look" (video text) - Bouton 5
        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'dafist_look') >> Discard()
    ],
    orl >> ProgramFilter(4) >> [ # Couplet part 2 (orl meuf) - Bouton 4


        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'dafist_couplet_firstpart_fixe'),
        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'dafist_couplet_secondpart_fixe'),


        SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'dafist_mooncupwaters_alpha', 1),
        SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_mooncupwaters_alpha'),
        SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'dafist_mooncupwaters_rgb', 1),
        SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_mooncupwaters_rgb'),
        SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'dafist_mooncupwaters_jardin', 1),
        SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_mooncupwaters_jardin'),
        SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'dafist_mooncupwaters_cour', 1),
        SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_mooncupwaters_cour'),


        SendOSC(lightseqport, '/Lightseq/Bpm', 1800),
        SendOSC(lightseqport, '/Lightseq/Play', timestamp),

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

        SendOSC(cmeinport, '/mididings/switch_scene', 5),

    ] >> Discard(),
    jeannot >> ProgramFilter(4) >> [ # Couplet part 3 (ragga) - Bouton 4
        Program(72) >> cseqtrigger,
        [

            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(120)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(120)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(240)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(120)),



            # video
            SendOSC(rpicourport, '/pyta/scene_recall', 'dafist_couplet_ragga'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'dafist_couplet_ragga'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_couplet_ragga_pdiddz'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'dafist_transe_basse_reset'),

            # light
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_couplet_anim2'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 120),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),



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
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            SendOSC(cmeinport, '/mididings/switch_scene', 5),

            bassdry,
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,

        ] >> Discard(),
    ],
    orl >> ProgramFilter(5) >> [ # Pre-refrain nano - Bouton 5
        Program(68) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 120),

            SendOSC(rpicourport, '/pyta/scene_recall', 'dafist_prerefrain'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'dafist_prerefrain'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_prerefrain'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_prerefrain_zoom'),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'dafist_intro_fixe'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'dafist_battements_intensity'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_intro_anim'),


            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(120)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(120)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(120)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(120)),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -5.0],

            ]),


            vxorlgars_on,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            SendOSC(cmeinport, '/mididings/switch_scene', 7),

            bassdry,
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,

            ] >> Discard()
        ],
    orl >> ProgramFilter(6) >> [ # Couplet 2 - Bouton 6
        Program(67) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(slport, '/sl/-1/hit', 'pause_on'),
            SendOSC(slport, '/sl/0/set', 'sync', 0),
            SendOSC(slport, '/sl/0/hit', 'pause_off'),
            SendOSC(slport, '/sl/0/hit', 'trigger'),
            SendOSC(slport, '/sl/0/set', 'sync', 1),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(120)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(120)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(240)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(120)),

            SendOSC(lightseqport, '/Lightseq/Bpm', 1800),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'dafist_mooncupwaters_alpha', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_mooncupwaters_alpha'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'dafist_mooncupwaters_rgb', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_mooncupwaters_rgb'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'dafist_mooncupwaters_jardin', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_mooncupwaters_jardin'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'dafist_mooncupwaters_cour', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_mooncupwaters_cour'),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

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


            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,
            vxjeannotverb_on,

            SendOSC(cmeinport, '/mididings/switch_scene', 9),

            bassdry,
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,

            ] >> Discard()
        ],
 

    orl >> ProgramFilter(7) >> [ # Blast - Bouton 7
        Program(73) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassSynth/Gain/Mute', 1.0),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(120)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(120)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(120)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(120)),


            SendOSC(rpicourport, '/pyta/scene_recall', 'dafist_refrain'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'dafist_refrain'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_refrain'),

            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_refrain_anim'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 120),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            SendOSC(audioseqport, '/Audioseq/Scene/Play', 'dafist_blast_bassopen'),
            SendOSC(audioseqport, '/Audioseq/Bpm', 120),
            SendOSC(audioseqport, '/Audioseq/Play', timestamp),


            SendOscState([
                [bassmainport, '/strip/BassSynth/Gain/Mute', 1.0],

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
            vxjeannotvocode_off,

            bassdry,
            bassdetunest_on,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,

            SendOSC(cmeinport, '/mididings/switch_scene', 5),

            ] >> Discard()

        ],
    orl >> ProgramFilter(8) >> [ # Transe goa - Bouton 8
        Program(71) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 130),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 130),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(130)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(130)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(130)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(130)),

            SendOSC(rpicourport, '/pyta/scene_recall', 'dafist_loading_cour'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'dafist_loading_jardin'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'dafist_loading_increment_init', timestamp),

            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_transe_anim'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'dafist_transe_intro'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'dafist_transe_intro_init'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 130),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

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
            vxorldelay_on,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            SendOSC(cmeinport, '/mididings/switch_scene', 9),

            bassdry,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],
    orl >> ProgramFilter(9) >> [ # sl 9 record
        SendOSC(slport, '/sl/7/hit', 'record'),

        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'dafist_loading_increment'),
        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'dafist_transe_intro_step'),

        ] >> Discard(),
    orl >> ProgramFilter(10) >> [ # sl 10 overdub
        SendOSC(slport, '/sl/7/hit', 'overdub'),

        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'dafist_loading_increment'),
        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'dafist_transe_intro_step'),

        ] >> Discard(),
    jeannot >> ProgramFilter(6) >> [ # RELANCE Transe goa - Bouton 6
        # Program(71) >> cseqtrigger,
        Ctrl(0, 0) >> tapeutapecontrol,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 130),

            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(slport, '/sl/7/set', 'sync', 0),
            SendOSC(slport, '/sl/7/hit', 'pause_off'),
            SendOSC(slport, '/sl/7/hit', 'trigger'),
            SendOSC(slport, '/sl/7/set', 'sync', 1),

            SendOSC(klickport, '/klick/simple/set_tempo', 130),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(audioseqport, '/Audioseq/Bpm', 130),
            SendOSC(audioseqport, '/Audioseq/Play', timestamp),
            SendOSC(audioseqport, '/Audioseq/Sequence/Enable', 'dafist_outro_filter'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(130)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(130)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(130)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(130)),


            SendOSC(lightseqport, '/Lightseq/Bpm', 130),


            SendOSC(rpicourport, '/pyta/scene_recall', 'dafist_disco_jardin'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'dafist_disco_cour'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_transe_cutoff'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_transe_roll_jardin'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_transe_roll_cour'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'dafist_transe_roll_jardin', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'dafist_transe_roll_cour', 1),

            # SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_transe_toto'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_transe_tata'),


            SendOSC(lightseqport, '/Lightseq/Play', timestamp),



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
            vxjeannotvocode_off,

            bassdry,

            # Transition Trains Climat
            SendOSC(cmeinport, '/mididings/switch_scene', 11),
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

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],
        jeannot >> ProgramFilter(7) >> [ # Delay Jeannot Off
            vxjeannotdelay_on,
            vxjeannotgars_on,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_on,
        ] >> Discard(),
            jeannot >> ProgramFilter(8) >> [ # Delay Jeannot On
            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,
            vxjeannotverb_on,
        ] >> Discard(),

        orl >> ProgramFilter(11) >> [ # Passage vers Fifty - Bouton 11
            SceneSwitch(4) >> Discard(),
            Program(2) >> Output('PBCtrlOut', 1),
            SendOSC(audioseqport, '/Audioseq/Bpm', 117),
            SendOSC(audioseqport, '/Audioseq/Scene/Play', 'fifty_intro', timestamp),


        ],

    ]
