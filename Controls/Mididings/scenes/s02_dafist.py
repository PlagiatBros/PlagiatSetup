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
    4:'green',
    4:'green',
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
    [orl, jeannot] >> ProgramFilter([range(2,9)]) >> [
       SendOSC(lightseqport, '/Lightseq/Sequence/Disable', '*'),
        SendOSC(lightseqport, '/Lightseq/Scene/Stop', '*'),
        SendOSC(rpijardinport, '/pyta/slide/animate/stop', -1),
        SendOSC(rpicourport, '/pyta/slide/animate/stop', -1),
        SendOSC(rpijardinport, '/pyta/slide/visible', -1, 0),
        SendOSC(rpicourport, '/pyta/slide/visible', -1, 0),
        SendOSC(rpijardinport, '/pyta/text/reset', -1),
        SendOSC(rpicourport, '/pyta/text/reset', -1),
        SendOSC(qlcstopport, '/Stop'),
    ] >> Discard(),
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    orl >> ProgramFilter(2) >> [ # Intro Thème glockentspiel - Bouton 2
        Program(65) >> cseqtrigger,
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

#            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'dafist_intro'),

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
            vxjeannotvocode_off,
            ] >> Discard()
        ],
    orl >> ProgramFilter(3) >> [ # Intro Thème 2 avec instrus - Bouton 3
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

            # SendOSC(lightseqport, '/Lightseq/Bpm', 120),
            # SendOSC(lightseqport, '/Lightseq/Scene/Play', 'dafist_entreeinstru'),
            # SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_entreeinstru_leslie'),
            # SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_clignotage'),
            # SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            SendOSC(rpijardinport, '/pyta/text', 0, 'PLAGIAT'),
            SendOSC(rpijardinport, '/pyta/text/visible', 0, 1),
            SendOSC(rpijardinport, '/pyta/text/size', 0, 0.5),
            SendOSC(rpijardinport, '/pyta/text', 1, 'faute de          frappe '),
            SendOSC(rpijardinport, '/pyta/text/visible', 1, 1),
            SendOSC(rpijardinport, '/pyta/text/align', 1, 'center', 'top'),
            SendOSC(rpijardinport, '/pyta/text/position', 1, 0, -20),
            SendOSC(rpijardinport, '/pyta/text/size', 1, 0.15),
            SendOSC(rpijardinport, '/pyta/text', 2, 'petites             s'),
            SendOSC(rpijardinport, '/pyta/text/visible', 2, 1),
            SendOSC(rpijardinport, '/pyta/text/align', 2, 'right', 'top'),
            SendOSC(rpijardinport, '/pyta/text/position', 2, -110, -50),
            SendOSC(rpijardinport, '/pyta/text/size', 2, 0.03),
            SendOSC(rpijardinport, '/pyta/text/strobe', 2, 1, 13, 0.66),
            SendOSC(rpicourport, '/pyta/text', 0, 'PLAGIAT'),
            SendOSC(rpicourport, '/pyta/text/visible', 0, 1),
            SendOSC(rpicourport, '/pyta/text/size', 0, 0.5),
            SendOSC(rpicourport, '/pyta/text', 1, 'faute de          frappe '),
            SendOSC(rpicourport, '/pyta/text/visible', 1, 1),
            SendOSC(rpicourport, '/pyta/text/align', 1, 'center', 'top'),
            SendOSC(rpicourport, '/pyta/text/position', 1, 0, 0),
            SendOSC(rpicourport, '/pyta/text/size', 1, 0.15),
            SendOSC(rpicourport, '/pyta/text', 2, 'petites              s'),
            SendOSC(rpicourport, '/pyta/text/visible', 2, 1),
            SendOSC(rpicourport, '/pyta/text/size', 2, 0.03),
            SendOSC(rpicourport, '/pyta/text/align', 2, 'right', 'top'),
            SendOSC(rpicourport, '/pyta/text/position', 2, -110, -65),
            SendOSC(rpicourport, '/pyta/text/strobe', 2, 1, 15, 0.7),


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

            # SendOSC(lightseqport, '/Lightseq/Bpm', 120),
            # SendOSC(lightseqport, '/Lightseq/Scene/Play', 'dafist_clignotageA'),

            SendOSC(rpijardinport, '/pyta/text', 0, '??'),
            SendOSC(rpijardinport, '/pyta/text/size', 0, 1),
            SendOSC(rpijardinport, '/pyta/text/visible', 0, 1),
            SendOSC(rpijardinport, '/pyta/text/strobe', 0, 1, 3, 0.6),
            SendOSC(rpicourport, '/pyta/text', 2, '??'),
            SendOSC(rpicourport, '/pyta/text/size', 2, 1),
            SendOSC(rpicourport, '/pyta/text/visible', 2, 1),
            SendOSC(rpicourport, '/pyta/text/strobe', 2, 1, 5, 0.6),




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
    jeannot >> ProgramFilter(3) >> [ # Refrain initial et final (basse / meshuggah)- Bouton 3
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

            SendOSC(lightseqport, '/Lightseq/Bpm', 120),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_refrain'),
            # SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_roulettearabesques'),
            # SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_themerefrain_clignotagestrob'),
            # SendOSC(lightseqport, '/Lightseq/Play', timestamp),

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
    orl >> ProgramFilter(4) >> [ # Couplet - Bouton 4
        #TODO son synthé (pour après bouclage basse)
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
    jeannot >> ProgramFilter(4) >> [ # "Look" - Bouton 4
        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'dafist_look') >> Discard()
    ],
    orl >> ProgramFilter(5) >> [ # Couplet part 2 - Bouton 5
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
            # SendOSC(lightseqport, '/Lightseq/Scene/Play', 'dafist_entreeinstru'),
            #SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_entreeinstru_leslie'),
            #SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_clignotage'),

            SendOSC(rpijardinport, '/pyta/text/size', 2, 0.2),
            SendOSC(rpicourport, '/pyta/text/size', 2, 0.2),

            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_prerefrain'),
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

            SendOSC(cmeinport, '/mididings/switch_scene', 7),

            bassdry,
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,

            ] >> Discard()
        ],
    orl >> ProgramFilter(6) >> [ # Refrain milieu (synthé / skrillex) - Bouton 6
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

            SendOSC(cmeinport, '/mididings/switch_scene', 5),

            bassdry,
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,

            ] >> Discard()
        ],
    orl >> ProgramFilter(7) >> [ # Couplet 2 - Bouton 7
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
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'dafist_mooncupwaters_alpha', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_mooncupwaters_alpha'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'dafist_mooncupwaters_rgb', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_mooncupwaters_rgb'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'dafist_mooncupwaters_jardin', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_mooncupwaters_jardin'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'dafist_mooncupwaters_cour', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_mooncupwaters_cour'),

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

            SendOSC(rpijardinport, '/pyta/text', 2, ' Transe Loading'),
            SendOSC(rpijardinport, '/pyta/text/strobe', 2, 1, 8, 0.6),
            SendOSC(rpijardinport, '/pyta/text/size', 2, 0.05),
            SendOSC(rpijardinport, '/pyta/text/visible', 2, 1),
            SendOSC(rpijardinport, '/pyta/text/align', 2, 'left', 'bottom'),
            SendOSC(rpijardinport, '/pyta/text/position', 2, 10, 20),
            SendOSC(rpicourport, '/pyta/text', 2, 'Transloading '),
            SendOSC(rpicourport, '/pyta/text/strobe', 2, 1, 10, 0.4),
            SendOSC(rpicourport, '/pyta/text/size', 2, 0.05),
            SendOSC(rpicourport, '/pyta/text/visible', 2, 1),
            SendOSC(rpicourport, '/pyta/text/position', 2, -10, 20),
            SendOSC(rpicourport, '/pyta/text/align', 2, 'right', 'bottom'),

            # Smoke show
            SendOSC(rpijardinport, '/pyta/slide/alpha', smokes, 0.1),
            SendOSC(rpicourport, '/pyta/slide/alpha', smokes, 0.1),
            SendOSC(rpijardinport, '/pyta/slide/rgb', smokes, 255, 255, 255),
            SendOSC(rpicourport, '/pyta/slide/rgb', smokes, 255, 255, 255),
            SendOSC(lightseqport, '/Lightseq/Bpm', 520),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'dafist_transe_smokes_jardin', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_transe_smokes_jardin'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'dafist_transe_smokes_cour', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_transe_smokes_cour'),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            # Création de la barre de chargement
            SendOSC(rpijardinport, '/pyta/slide/position_z', 'Mask_1', -90),
            SendOSC(rpicourport, '/pyta/slide/position_z', 'Mask_1', -90),


            SendOSC(rpijardinport, '/pyta/slide/clone', 'White', 'Dafist_trance_bar'),
            SendOSC(rpijardinport, '/pyta/slide/position_z', 'Dafist_trance_bar', -99),
            SendOSC(rpijardinport, '/pyta/slide/position_y', 'Dafist_trance_bar', -580),
            SendOSC(rpijardinport, '/pyta/slide/position_x', 'Dafist_trance_bar', -800),
            SendOSC(rpijardinport, '/pyta/slide/visible', 'Dafist_trance_bar', 1),

            SendOSC(rpicourport, '/pyta/slide/clone', 'White', 'Dafist_trance_bar'),
            SendOSC(rpicourport, '/pyta/slide/position_z', 'Dafist_trance_bar', -99),
            SendOSC(rpicourport, '/pyta/slide/position_y', 'Dafist_trance_bar', -580),
            SendOSC(rpicourport, '/pyta/slide/position_x', 'Dafist_trance_bar', 800),
            SendOSC(rpicourport, '/pyta/slide/visible', 'Dafist_trance_bar', 1),

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

        # Barre de chargement monte + alpha smoke show
        SendOSC(rpijardinport, '/pyta/slide/animate', 'Dafist_trance_bar', 'position_x', '+0', '+200', 7),
        SendOSC(rpijardinport, '/pyta/slide/animate', smokes, 'alpha', '+0', '+0.05', 6),
        SendOSC(rpicourport, '/pyta/slide/animate', 'Dafist_trance_bar', 'position_x', '+0', '-200', 7),
        SendOSC(rpicourport, '/pyta/slide/animate', smokes, 'alpha', '+0', '+0.05', 6),

        ] >> Discard(),
    orl >> ProgramFilter(10) >> [ # sl 10 overdub
        SendOSC(slport, '/sl/7/hit', 'overdub'),

        # Barre de chargement monte encore
        SendOSC(rpijardinport, '/pyta/slide/animate', 'Dafist_trance_bar', 'position_x', '+0', '+150', 4),
        SendOSC(rpijardinport, '/pyta/slide/animate', smokes, 'alpha', '+0', '+0.15', 6),
        SendOSC(rpicourport, '/pyta/slide/animate', 'Dafist_trance_bar',  'position_x', '+0', '-150', 4),
        SendOSC(rpicourport, '/pyta/slide/animate', smokes, 'alpha', '+0', '+0.15', 6),
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

            # Barre de chargement
            SendOSC(rpijardinport, '/pyta/slide/visible', 'Dafist_trance_bar', 1),
            SendOSC(rpicourport, '/pyta/slide/visible', 'Dafist_trance_bar', 1),
            SendOSC(rpijardinport, '/pyta/slide/position_x', 'Dafist_trance_bar', 0),
            SendOSC(rpijardinport, '/pyta/slide/position_y', 'Dafist_trance_bar', 0),
            SendOSC(rpicourport, '/pyta/slide/position_x', 'Dafist_trance_bar', 0),
            SendOSC(rpicourport, '/pyta/slide/position_y', 'Dafist_trance_bar', 0),
            SendOSC(rpijardinport, '/pyta/slide/strobe', 'Dafist_trance_bar', 1),
            SendOSC(rpicourport, '/pyta/slide/strobe', 'Dafist_trance_bar', 1),

            SendOSC(lightseqport, '/Lightseq/Bpm', 130),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_transe_blinkload'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'dafist_transe_cutoff'),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'dafist_transe_blinkload', 1),

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
