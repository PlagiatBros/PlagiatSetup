#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################

horrorcore_mk2lights = {
    1:'blue',
    2:'purple',
    3:'purple',
    4:'purple',
    5:'purple',
    6:'yellow',
    7:'yellow',
    8:'yellow',
}

#### HorroCore ####
horrorcore = [
    Init([
        Program(seq24PageMap[9]) >> seq24once,
        Ctrl(0, 8) >> tapeutapecontrol,

        enable_microtonal,
        set_microtonal(0, 0, 0, 0, 0, 0.35, 0, 0, -0.35, 0, 0.35, 0),
        # zynmicrotonal_on,
        # SendOSC(zyntrebleport, '/microtonal/tunings', '135.0\n200.0\n300.0\n400.0\n500.0\n600.0\n700.0\n835.0\n900.0\n1000.0\n1065.0\n2/1'),

        SubSceneSwitch(1),
        mk2lights(horrorcore_mk2lights),
    ]),
    jeannot_padrelease >> mk2lights(horrorcore_mk2lights),
    orl >> ProgramFilter([range(1,12)]) >> [
        SendOSC(mk2inport, '/mididings/switch_scene', 4),
        SendOSC(audioseqport, '/Audioseq/Sequence/Disable', '*'),
        SubSceneSwitch(1),
    ] >> Discard(),
    jeannot >> ProgramFilter([range(1,9)]) >> [
        SendOSC(mk2inport, '/mididings/switch_scene', 4),
        SendOSC(audioseqport, '/Audioseq/Sequence/Disable', '*'),
    ] >> Discard(),
    orl >> ProgramFilter([range(2,12)]) >> light_reset >> Discard(),
    jeannot >> ProgramFilter([range(3,6)]) >> light_reset >> Discard(),
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    orl >> ProgramFilter(2) >> [ # Intro - Bouton 2 (mk2 notes = vx jean meuf; vx orl vocod; stop samples)
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 150),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),

            SendOSC(mk2inport, '/mididings/switch_scene', 5),

            SendOSC(lightseqport, '/Lightseq/Bpm', 150),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_intro'),

            SendOSC(rpijardinport, '/pyta/scene_recall', 'horrorcore_intro_jardin'),
            SendOSC(rpicourport, '/pyta/scene_recall', 'horrorcore_intro_cour'),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0],

                # [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                #
                # [samplesdelaymungeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -12.0],
                # [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -12.0],
                # [samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -15.0],

            ]),


            vxorlmeuf_on,
            vxorlgars_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
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
    jeannot >> ProgramFilter(2) >> [ # Couplet 1 - Bouton 2 (mk2 notes = vx jean meuf; vx orl vocod; stop samples)
        # TODO: envoyer samples dans la reverb
        # TODO: stereo samples
        SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'horrorcore_couplet_blinkBass'),
        SendOSC(lightseqport, '/Lightseq/Play', timestamp),
        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_couplet_stable'),

        SendOSC(rpijardinport, '/pyta/scene_recall', 'horrorcore_couplet_1'),
        SendOSC(rpicourport, '/pyta/scene_recall', 'horrorcore_couplet_1'),

        SendOscState([
            [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
            # [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
            # [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],
            # [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
            # [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0],
            [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
            [samplesdelaymungeport, '/strip/Samples[1-5]/Gain/Gain%20(dB)/unscaled', -9.0],


        ]),
    ],
    orl >> ProgramFilter(3) >> [ # Stupid donkey - Bouton 3
        Program(5) >> cseqtrigger,
        [
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'horrorcore_couplet_blinkBass'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'horrorcore_couplet_mooncup'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_mooncup_glitch'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_couplet_donkey'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_stupidDonkeys_trigger'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_mooncup_obama'),


            SendOSC(rpijardinport, '/pyta/scene_recall', 'horrorcore_couplet_donkey'),
            SendOSC(rpicourport, '/pyta/scene_recall', 'horrorcore_couplet_donkey'),


            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),




            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],

                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', 0.0],
                [samplesreversedelayport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', 0.0],
                [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', 0.0],


            ]),


            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotdelay_off,
            vxjeannotvocode_off,

            bassdry,

            ] >> Discard(),
        [
            bassdetunest_off,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,
            ]
        ],
    jeannot >> ProgramFilter(3) >> [ # Refrain - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 150),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),


            SendOSC(lightseqport, '/Lightseq/Bpm', 150),

            #light
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_refrain_stable'),

            #video
            SendOSC(rpijardinport, '/pyta/scene_recall', 'horrorcore_refrain_jardin'),
            SendOSC(rpicourport, '/pyta/scene_recall', 'horrorcore_refrain_cour'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_autruche_glitch'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'horrorcore_refrain_jardin'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'horrorcore_refrain_cour'),

            SendOSC(lightseqport, '/Lightseq/Play', timestamp),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],

                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', 0.0],
                [samplesreversedelayport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', 0.0],
                [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', 0.0],


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

            SendOSC(cmeinport, '/mididings/switch_scene', 5),



            ] >> Discard(),
        [
            bassdetunest_off,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,
            ]
        ],
    jeannot >> ProgramFilter(4) >> [ # Couplet 2 - Bouton 4
        Program(69) >> cseqtrigger,

        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 150),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),

            SendOSC(cmeinport, '/mididings/switch_scene', 7),
            SendOSC(mk2inport, '/mididings/switch_scene', 6),


            SendOSC(lightseqport, '/Lightseq/Bpm', 150),

            #light
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_couplet2_intro'),

            #video
            SendOSC(rpijardinport, '/pyta/scene_recall', 'horrorcore_couplet_2'),
            SendOSC(rpicourport, '/pyta/scene_recall', 'horrorcore_couplet_2'),
            # SendOSC(rpicourport, '/pyta/scene_recall', 'horrorcore_refrain_cour'),
            # SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_autruche_glitch'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'horrorcore_couplet_2_screenswitch'),
            # SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'horrorcore_refrain_cour'),

            SendOSC(lightseqport, '/Lightseq/Play', timestamp),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0],

                # [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                #
                # [samplesdelaymungeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -12.0],
                # [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -12.0],
                # [samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -15.0],

            ]),


            vxorlmeuf_on,
            vxorlgars_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_on,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
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
    orl >> ProgramFilter(4) >> [ # Should I - Bouton 4
        Program(5) >> cseqtrigger,
        [
            SendOSC(lightseqport, '/Lightseq/Bpm', 1500),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_couplet2_dubstep_extinction'),
#            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'horrorcore_couplet_blinkBass'),
#            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'horrorcore_couplet_mooncup'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_mooncup_glitch'),
            # SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_couplet_donkey'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_couplet_obama'),

            SendOSC(rpijardinport, '/pyta/scene_recall', 'horrorcore_couplet_donkey'),
            SendOSC(rpicourport, '/pyta/scene_recall', 'horrorcore_couplet_donkey'),


            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),




            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],

                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', 0.0],
                [samplesreversedelayport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', 0.0],
                [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', 0.0],


            ]),


            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotdelay_off,
            vxjeannotvocode_off,

            bassdry,

            ] >> Discard(),
        [
            bassdetunest_off,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,
            ]
        ],
    jeannot >> ProgramFilter(5) >> [ # Yep (orl meuf) - Bouton 5
        Program(70) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 150),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),

            SendOSC(slport, '/sl/0/set', 'sync', 0),
            SendOSC(slport, '/sl/0/hit', 'pause_off'),
            SendOSC(slport, '/sl/0/hit', 'trigger'),
            SendOSC(slport, '/sl/0/set', 'sync', 1),

            SendOSC(lightseqport, '/Lightseq/Bpm', 150),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_intro'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_couplet2_blinder_surcouche'),

            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'horrorcore_couplet_blinkBass'),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_lyrics_glitch'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'horrorcore_couplet_2_fin'),
            SendOSC(rpicourport, '/pyta/scene_recall', 'horrorcore_couplet_2_fin'),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0],

                # [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                #
                # [samplesdelaymungeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -12.0],
                # [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -12.0],
                # [samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -15.0],

            ]),


            vxorlmeuf_on,
            vxorlgars_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
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
    orl >> ProgramFilter(5) >> [ # Refrain grand messe - bouton 5
        stop,
        Program(72) >> cseqtrigger,
        [

            SendOSC(lightseqport, '/Lightseq/Bpm', 150),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_messe'),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_messe_christ'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'horrorcore_messe_jardin'),
            SendOSC(rpicourport, '/pyta/scene_recall', 'horrorcore_messe_cour'),

            SendOscState([

            ]),

            SendOSC(cmeinport, '/mididings/switch_scene', 12),

            vxorlmeuf_off,
            vxorlgars_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_on,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotvocode_on,

            bassdry,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],
    orl >> ProgramFilter(6) >> [ # AC4 disco - Bouton 6
        Program(71) >> cseqtrigger,
        [

            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 150),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],

            ]),


            SendOSC(lightseqport, '/Lightseq/Bpm', 150),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_ac4_intro1'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_ac4_intro2'),
            #
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_disco_christ'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'horrorcore_disco_jardin'),
            SendOSC(rpicourport, '/pyta/scene_recall', 'horrorcore_disco_cour'),


            vxorlmeuf_off,
            vxorlgars_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotdelay_off,
            vxjeannotvocode_off,

            SubSceneSwitch(1),

            SendOSC(cmeinport, '/mididings/switch_scene', 5),


            ] >> Discard()
        ],
    orl >> ProgramFilter(7) >> [ # Drop da bass - Bouton 7
        Program(71) >> cseqtrigger,
        [

            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 150),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],

            ]),


            SendOSC(lightseqport, '/Lightseq/Bpm', 150),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_dropTheBass'),

            SendOSC(rpijardinport, '/pyta/scene_recall', 'horrorcore_drop_merde'),
            SendOSC(rpicourport, '/pyta/scene_recall', 'horrorcore_drop_merde'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_drop_merde'),


            vxorlmeuf_off,
            vxorlgars_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotdelay_off,
            vxjeannotvocode_off,

            SubSceneSwitch(1),

            SendOSC(cmeinport, '/mididings/switch_scene', 5),


            ] >> Discard()
        ],
    orlCtrl >> CtrlFilter(2) >> [
        SendOSC(rpijardinport, '/pyta/slide/mecdansefondvert/set', 'gif_speed', lambda ev: 0.2 + pow(ev.value / 127., 2) * 2),
        SendOSC(rpicourport, '/pyta/slide/mecdansefondvert/set', 'gif_speed', lambda ev: 0.2 + pow(ev.value / 127., 2) * 2),
        SendOSC(rpicourport, '/pyta/slide/wood_1/animate', 'offset', '+0', 0, '-1', 0, lambda ev: 10 / (ev.value / 12.7) , 1),
    ] >> Discard(),
    orl >> ProgramFilter(8) >> [ # Ramner Mooncup Maison - Bouton 8
        Program(71) >> cseqtrigger,
        [

            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 150),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],

            ]),


            SendOSC(rpijardinport, '/pyta/scene_recall', 'horrorcore_relance'),
            SendOSC(rpicourport, '/pyta/scene_recall', 'horrorcore_relance'),

            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'horrorcore_ragga'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'horrorcore_mooncup_maison'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 150),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),


            vxorlmeuf_on,
            vxorlgars_on,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_on,

            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotdelay_off,
            vxjeannotvocode_off,

            SubSceneSwitch(1),

            SendOSC(cmeinport, '/mididings/switch_scene', 5),


            ] >> Discard()
        ],
    orl >> ProgramFilter(9) >> [ # Meshuggah Ramner Mooncup Maison - Bouton 9
        Program(71) >> cseqtrigger,
        [

            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 150),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],

            ]),

            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'horrorcore_meshuragga'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'horrorcore_mesh_jardin'),
            SendOSC(rpicourport, '/pyta/scene_recall', 'horrorcore_mesh_cour'),


            SendOSC(lightseqport, '/Lightseq/Bpm', 150),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),


            vxorlmeuf_on,
            vxorlgars_on,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_on,

            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotdelay_off,
            vxjeannotvocode_off,

            SubSceneSwitch(1),

            SendOSC(cmeinport, '/mididings/switch_scene', 5),


            ] >> Discard()
        ],
    jeannot >> ProgramFilter(6) >> [
        vxjeannotdelay_off,
        vxjeannotgars_on,
        vxjeannotmeuf_off,
        vxjeannotdisint_off,
        vxjeannotvocode_off,
    ] >> Discard(),
    jeannot >> ProgramFilter(7) >> [
        vxjeannotgars_off,
        vxjeannotmeuf_on,
        vxjeannotdisint_off,
        vxjeannotdelay_off,
        vxjeannotvocode_off,
    ] >> Discard(),
    jeannot >> ProgramFilter(8) >> [
        vxjeannotgars_off,
        vxjeannotmeuf_off,
        vxjeannotdisint_off,
        vxjeannotdelay_off,
        vxjeannotvocode_on,
    ] >> Discard(),
    ]
