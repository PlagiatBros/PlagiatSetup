#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################

instouboul_mk2lights = {
    1:'blue',
    2:'yellow',
    3:'yellow',
    4:'yellow',
    5:'white',
    7:'white',
    8:'blue',
}

coffee_redseas = " ".join(["Coffee_" + str(i) for i in range(1,11)])
coffee_redseas+=" Dunes_1"
coffee_redseas+=" Rock_1"
coffee_redseas+=" Moon_1"
coffee_redseas+=" Moon_2"
coffee_redseas+=" Mars_1"
coffee_redseas+=" Mars_2"
coffee_redseas+=" Mountains_1"
coffee_redseas+=" Mountains_2"


twerks = " ".join(['Twerk_'+str(i) for i in range(1,33)])

#### Instouboul ####
instouboul = [
    Init([
        Program(seq24PageMap[5]) >> seq24once,
        Ctrl(0, 3) >> tapeutapecontrol,

        enable_microtonal,
        set_microtonal(0, 0.35, 0, 0.35, 0, 0, 0, 0, 0.35, 0, 0, 0),
        # zynmicrotonal_on,
        # SendOSC(zyntrebleport, '/microtonal/tunings', '100.0\n200.0\n300.0\n435.0\n500.0\n635.0\n700.0\n800.0\n900.0\n1000.0\n1135.0\n2/1'),

        SendOSC(mk2inport, '/mididings/switch_scene', 1),
        mk2lights(instouboul_mk2lights),
        ]),
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    jeannot_padrelease >> mk2lights(instouboul_mk2lights),
    [orl, jeannot] >> ProgramFilter([range(1,12)]) >> [
        SendOSC(audioseqport, '/Audioseq/Sequence/Disable', '*'),
        SendOSC(samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.),
        SendOSC(vxmainport, '/strip/VxJeannotMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.),
        SendOSC(vxmainport, '/strip/VxORLMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.),
        SendOSC(bassmainport, '/strip/BassMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.),
        SendOSC(samplesmainport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled',20000.),

    ] >> Discard(),
    orl >> ProgramFilter([range(2,12)]) >> light_reset >> Discard(),
    jeannot >> ProgramFilter([range(2,8)]) >> light_reset >> Discard(),
    orl >> ProgramFilter(2) >> [ # Instouboul sans batterie - Bouton 2
        Program(77) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(120)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(120)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(120)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(120)),

            SendOSC(lightseqport, '/Lightseq/Bpm', 120),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'le5_boum_jardin', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'le5_boum_cour', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Play', 'le5_boum_jardin'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Play', 'le5_boum_cour'),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),
            SendOSC(rpijardinport, '/pyta/text', 0, "Instouboul"),
            SendOSC(rpicourport, '/pyta/text', 0, "Instouboul"),
            SendOSC(rpijardinport, '/pyta/text/align', 0, 'top', 'left'),
            SendOSC(rpicourport, '/pyta/text/align', 0, 'top', 'right'),
            SendOSC(rpijardinport, '/pyta/text/animate', 0, 'size', 0, 1, 300),
            SendOSC(rpicourport, '/pyta/text/animate', 0, 'size', 0, 1, 300),
            SendOSC(rpijardinport, '/pyta/text/animate', 0, 'alpha', 0.1, 1, 300),
            SendOSC(rpicourport, '/pyta/text/animate', 0, 'alpha', 0.1, 1, 300),
            SendOSC(rpijardinport, '/pyta/text/visible', 0, 1),
            SendOSC(rpicourport, '/pyta/text/visible', 0, 1),

            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxorlvocode_off,

            SendOSC(samplesmainport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled',200.),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),
        ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,
            ]
        ],
    orl >> ProgramFilter(3) >> [ # Instouboul bouclage voix + bass - Bouton 3
        [

            SendOSC(samplesmainport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled',200.),

            SendOSC(slport, '/sl/0/hit', 'record'), # bass pre
            SendOSC(slport, '/sl/2/hit', 'record'), # vxorl pre
            SendOSC(slport, '/sl/4/hit', 'record'), # vxjeannot pre

            ] >> Discard()
        ],
    jeannot >> ProgramFilter(2) >> [ # Vx jeannot
        vxjeannotdelay_off,
        vxjeannotgars_on,
        vxjeannotmeuf_off,
        vxjeannotdisint_off,
        vxjeannotvocode_off,
    ] >> Discard(),
    jeannot >> ProgramFilter(3) >> [ # Vx jeannot
        vxjeannotgars_off,
        vxjeannotmeuf_on,
        vxjeannotdisint_off,
        vxjeannotdelay_off,
        vxjeannotvocode_off,
    ] >> Discard(),
    jeannot >> ProgramFilter(4) >> [ # Vx jeannot
        vxjeannotgars_off,
        vxjeannotmeuf_off,
        vxjeannotdisint_off,
        vxjeannotdelay_off,
        vxjeannotvocode_on,
    ] >> Discard(),
    jeannot >> ProgramFilter(5) >> [ # Instouboul entrée batterie meshuggah - bouton 7
        Program(78) >> cseqtrigger,
        [

            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(audioseqport, '/Audioseq/Bpm', 120),
            SendOSC(audioseqport, '/Audioseq/Play', timestamp),
            SendOSC(audioseqport, '/Audioseq/Sequence/Enable', 'le5_louboutin'),

            SendOSC(slport, '/sl/0/hit', 'pause_on'), # bass
            SendOSC(slport, '/sl/2/hit', 'pause_on'), # vxorlpre
            SendOSC(slport, '/sl/4/hit', 'pause_on'), # vxjeannotpre

            SendOSC(lightseqport, '/Lightseq/Bpm', 960),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'le5_boum_jardin', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'le5_boum_cour', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Play', 'le5_boum_jardin'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Play', 'le5_boum_cour'),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            ] >> Discard()
        ],
    jeannot >> ProgramFilter(8) >> [  # stop reverse Instouboul => Louboutin - Bouton 10
        Program(73) >> cseqtrigger,
        [

            SendOSC(slport, '/sl/-1/hit', 'reverse'),
            SendOSC(surfaceorlport, '/sl/-1/hit', 'reverse', 1),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_instouboulouboutin'),
            SendOSC(rpijardinport, '/pyta/text/visible', 0, 1),
            SendOSC(rpicourport, '/pyta/text/visible', 0, 1),


            ] >> Discard()
        ],
    orl >> ProgramFilter(11) >> [ # SW
        SceneSwitch(7) >> Discard(),
        Program(2) >> Output('PBCtrlOut', 1)
        ],

    ]
