#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################

nymphotrap_mk2lights = {
    1:'blue',
    2:'yellow',
    3:'yellow',
    4:'yellow',
    5:'white',
    6:'purple',
    7:'white',
    8:'purple',
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

#### Nymphotrap ####
nymphotrap = [
    Init([
        Program(seq24PageMap[5]) >> seq24once,
        Ctrl(0, 3) >> tapeutapecontrol,

        enable_microtonal,
        set_microtonal(0, 0.35, 0, 0.35, 0, 0, 0, 0, 0.35, 0, 0, 0),
        # zynmicrotonal_on,
        # SendOSC(zyntrebleport, '/microtonal/tunings', '100.0\n200.0\n300.0\n435.0\n500.0\n635.0\n700.0\n800.0\n900.0\n1000.0\n1135.0\n2/1'),

        SendOSC(mk2inport, '/mididings/switch_scene', 1),
        mk2lights(nymphotrap_mk2lights),
        ]),
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    jeannot_padrelease >> mk2lights(nymphotrap_mk2lights),
    [orl >> ProgramFilter([range(1,12)]), jeannot >>  ProgramFilter([1,5,6,7])] >> Filter(PROGRAM) >> [
        SendOSC(audioseqport, '/Audioseq/Sequence/Disable', '*'),
        SendOSC(samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.),
        SendOSC(vxmainport, '/strip/VxJeannotMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.),
        SendOSC(vxmainport, '/strip/VxORLMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.),
        SendOSC(bassmainport, '/strip/BassMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.),
        SendOSC(samplesmainport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled',20000.),

    ] >> Discard(),
    orl >> ProgramFilter([range(2,12)]) >> light_reset >> Discard(),
    jeannot >> ProgramFilter([range(5,8)]) >> light_reset >> Discard(),
    orl >> ProgramFilter(2) >> [ # Cloud rap ballade rhodes - Bouton 2
        stop,
        Program(73) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 60),

            SendOSC(klickport, '/klick/simple/set_tempo', 60),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),
            SendOSC(cmeinport, '/mididings/switch_scene', 10),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(60)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(60)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(60)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(60)),


            SendOSC(monitorsjeannotport, '/strip/Klick/Gain/Mute', 1.0),


            SendOSC(rpijardinport, '/pyta/slide/animate', 'Stars_1', 'zoom', 2, 6, 300),
            SendOSC(rpicourport, '/pyta/slide/animate', 'Stars_2', 'zoom', 2, 6, 300),
            SendOSC(rpijardinport, '/pyta/slide/visible', 'Stars_1', 1),
            SendOSC(rpicourport, '/pyta/slide/visible', 'Stars_2', 1),
            SendOSC(rpijardinport, '/pyta/text', 2, 'cu   is obvious'),
            SendOSC(rpijardinport, '/pyta/text/align', 2, 'top', 'left'),
            SendOSC(rpijardinport, '/pyta/text/visible', 2, 1),
            SendOSC(rpicourport, '/pyta/text', 2, 'cute is obvious'),
            SendOSC(rpicourport, '/pyta/text/align', 2, 'top', 'right'),
            SendOSC(rpicourport, '/pyta/text/visible', 2, 1),

            ] >> Discard(),
        [

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

            ] >> Discard()
        ],
    orl >> ProgramFilter(8) >> [ # Bouclage rhodes  - Bouton 8
            SendOSC(slport, '/sl/8/hit', 'record'),
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
    jeannot >> [ProgramFilter(5), ProgramFilter(6), ProgramFilter(7)]>> [ # nymphotrap bouliotte - bouton 5
        Program(75) >> cseqtrigger,
        [
            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(120)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(120)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(120)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(120)),

        SendOSC(mk2inport, '/mididings/switch_scene', 9), # sample cut
        SendOSC(cmeinport, '/mididings/switch_scene', 8),

		#TODO Positionnement
	    SendOSC(rpijardinport, '/pyta/text', 2, 'nAfr0-tRap'),
	    SendOSC(rpicourport, '/pyta/text', 1, 'NYMPH0 TRAP'),
	    SendOSC(rpijardinport, '/pyta/text/visible', 2, 1),
	    SendOSC(rpijardinport, '/pyta/text/strobe', 2, 1, 12, 0.5),
	    SendOSC(rpijardinport, '/pyta/text/alpha', 2, 0.5),
	    SendOSC(rpicourport, '/pyta/text/visible', 1, 1),
	    SendOSC(rpicourport, '/pyta/text/strobe', 1, 1, 11, 0.5),
	    SendOSC(rpijardinport, '/pyta/text/alpha', 1, 0.5),

	    SendOSC(lightseqport, '/Lightseq/Bpm', 125),
	    SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_nymphotrap_blow'),
	    SendOSC(rpijardinport, '/pyta/slide/alpha', twerks, 0.15),
	    SendOSC(rpicourport, '/pyta/slide/alpha', twerks, 0.15),
	    SendOSC(lightseqport, '/Lightseq/Play', timestamp),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry,
            basswobble,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
    ],
    jeannot >> ProgramFilter(5) >> [ # nymphotrap avec orl vx meuf (bouliotte) - bouton 5
        SendOSC(slport, '/set', 'eighth_per_cycle', 8),
        SendOSC(slport, '/set', 'tempo', 120),
        SendOSC(slport, '/sl/[7,8]/hit', 'pause_on'),

        vxorlgars_off,
        vxorlmeuf_on,
        vxorldisint_off,
        vxorldelay_off,
        vxorlvocode_off,
    ] >> Discard(),
    jeannot >> ProgramFilter(6) >> [ # nymphotrap avec orl vx gars (refrain) - bouton 6
        SendOSC(slport, '/set', 'eighth_per_cycle', 10),
        SendOSC(slport, '/set', 'tempo', 120),
        SendOSC(slport, '/sl/[7,8]/hit', 'pause_on'),

        vxorlgars_on,
        vxorlmeuf_off,
        vxorldisint_off,
        vxorldelay_off,
        vxorlvocode_off,
    ] >> Discard(),
    jeannot >> ProgramFilter(7) >> [ # nymphotrap avec orl vx vocod (couplet) - bouton 7
        [Program(84), Program(85)] >> seq24once, 
        [
        SendOSC(slport, '/set', 'eighth_per_cycle', 10),
        SendOSC(slport, '/set', 'tempo', 120),
        SendOSC(slport, '/sl/[7,8]/hit', 'pause_on'),

        vxorlgars_off,
        vxorlmeuf_off,
        vxorldisint_off,
        vxorldelay_off,
        vxorlvocode_on,
        vxjeannotmeuf_on,
        vxjeannotgars_off,
        ] >> Discard(),
    ],
#    jeannot >> ProgramFilter(8) >> [ # nymphotrap (couplet part 2, trig boucles bouliottes) - bouton 8
#        SendOSC(slport, '/sl/7/hit', 'trigger'),
#    ] >> Discard(),

    orl >> ProgramFilter(9) >> [ # Bouclage synth  - Bouton 9
            SendOSC(slport, '/sl/7/hit', 'record'), # synth aigu
        ],
    orl >> ProgramFilter(3) >> [ # thème ragga - bouton 3
        Program(76) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(slport, '/sl/8/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(120)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(120)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(120)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(120)),


		#TODO Positionnement
	    SendOSC(rpijardinport, '/pyta/text', 2, 'nAfr0-tRap'),
	    SendOSC(rpicourport, '/pyta/text', 1, 'NYMPH0 TRAP'),
	    SendOSC(rpijardinport, '/pyta/text/visible', 2, 1),
	    SendOSC(rpijardinport, '/pyta/text/strobe', 2, 1, 12, 0.5),
	    SendOSC(rpijardinport, '/pyta/text/alpha', 2, 0.5),
	    SendOSC(rpicourport, '/pyta/text/visible', 1, 1),
	    SendOSC(rpicourport, '/pyta/text/strobe', 1, 1, 11, 0.5),
	    SendOSC(rpijardinport, '/pyta/text/alpha', 1, 0.5),

	    SendOSC(lightseqport, '/Lightseq/Bpm', 125),
	    SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_nymphotrap_blow'),
	    SendOSC(rpijardinport, '/pyta/slide/alpha', twerks, 0.15),
	    SendOSC(rpicourport, '/pyta/slide/alpha', twerks, 0.15),
	    SendOSC(lightseqport, '/Lightseq/Play', timestamp),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),

            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_on,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry,
            basswobble,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
    ],

#   orl >> ProgramFilter(4) >> [
#        stop,
#        [
#            vxorlgars_on,
#            vxorlmeuf_off,
#            vxorldisint_off,
#            vxorldelay_off,
#            vxorlvocode_off,
#        ] >> Discard()
#    ],


    orl >> ProgramFilter(11) >> [ # Instouboul - bouton 11
        SceneSwitch(61) >> Discard(),
        Program(2) >> Output('PBCtrlOut', 1)
        ],

    ]
