#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################

fifty_mk2lights = {
    1:'blue',
    2:'green',
    3:'green',
    4:'yellow',
    5:'yellow',
    6:'yellow',
    7:'green',
    8:'red',
}


colos = " ".join(['Colo_'+str(i) for i in range(1,47)])
twerks = " ".join(['Twerk_'+str(i) for i in range(1,33)])
twerks_beauf = " ".join(['Twerk_'+str(i) for i in range(11,26)])
teas = " ".join(['Tea_'+str(i) for i in range(1,9)])

#### Fifty ####
fifty = [
    Init([
        Program(seq24PageMap[4]) >> seq24once,
        Ctrl(0, 2) >> tapeutapecontrol,

        disable_microtonal,
        # zynmicrotonal_off,

        SendOSC(mk2inport, '/mididings/switch_scene', 1),
        mk2lights(fifty_mk2lights),
        ]),
    jeannot_padrelease >> mk2lights(fifty_mk2lights),
    [orl, jeannot] >> ProgramFilter([range(1,12)]) >> [
        SendOSC(audioseqport, '/Audioseq/Sequence/Disable', '*')
    ] >> Discard(),
    orl >> ProgramFilter([range(2,12)]) >> light_reset >> Discard(),
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    orl >> ProgramFilter(2) >> [ # Intro (fin du sample) - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 117),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 117),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(117)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(117)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(117)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(117)),


    		#TODO Scaling, Position en mode logo (en haut du cadre)
    	    SendOSC(rpijardinport, '/pyta/text', 0, "PLAGIAT"),
            SendOSC(rpijardinport, '/pyta/text/size', 0, 0.2),
            SendOSC(rpijardinport, '/pyta/text/align', 0, 'center', 'top'),
            SendOSC(rpijardinport, '/pyta/text/position', 0, 0, -100),
    	    SendOSC(rpijardinport, '/pyta/text/visible', 0, 1),

    	    SendOSC(rpijardinport, '/pyta/text', 2, "makes ~art~ wizz $hit"),
            SendOSC(rpijardinport, '/pyta/text/size', 2, 0.07),
            SendOSC(rpijardinport, '/pyta/text/align', 2, 'center', 'top'),
            SendOSC(rpijardinport, '/pyta/text/position', 2, 0, -230),
            SendOSC(rpijardinport, '/pyta/text/visible', 2, 1),


    	    SendOSC(rpicourport, '/pyta/text', 3, "[plaʒia]"),
            SendOSC(rpicourport, '/pyta/text/size', 3, 0.15),
            SendOSC(rpicourport, '/pyta/text/align', 3, 'center', 'top'),
            SendOSC(rpicourport, '/pyta/text/position', 3, 0, -100),
    	    SendOSC(rpicourport, '/pyta/text/visible', 3, 1),

    	    SendOSC(rpicourport, '/pyta/text', 1, "bakes $hit wiv butter"),
            SendOSC(rpicourport, '/pyta/text/size', 1, 0.07),
            SendOSC(rpicourport, '/pyta/text/align', 1, 'center', 'top'),
            SendOSC(rpicourport, '/pyta/text/position', 1, 0, -230),
            SendOSC(rpicourport, '/pyta/text/visible', 1, 1),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -7.0],

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
            vxjeannotvocode_off,


            ] >> Discard()
        ],
    orl >> ProgramFilter(3) >> [ # Intro stagiaire - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 64),
            SendOSC(slport, '/set', 'tempo', 117),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 117),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            # Bouclage basse manuel pour l'instant

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(117)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(117)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(117)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(117)),

    	    SendOSC(rpijardinport, '/pyta/text', 0, "PLAGIAT"),
            SendOSC(rpijardinport, '/pyta/text/size', 0, 0.2),
            SendOSC(rpijardinport, '/pyta/text/align', 0, 'center', 'top'),
            SendOSC(rpijardinport, '/pyta/text/position', 0, 0, -100),
    	    SendOSC(rpijardinport, '/pyta/text/visible', 0, 1),

    	    SendOSC(rpijardinport, '/pyta/text', 2, "makes ~art~ wizz $hit"),
            SendOSC(rpijardinport, '/pyta/text/size', 2, 0.07),
            SendOSC(rpijardinport, '/pyta/text/align', 2, 'center', 'top'),
            SendOSC(rpijardinport, '/pyta/text/position', 2, 0, -230),
            SendOSC(rpijardinport, '/pyta/text/visible', 2, 1),

            SendOSC(rpijardinport, '/pyta/text/size', 1, 0.05),
            SendOSC(rpijardinport, '/pyta/text/align', 1, 'center', 'center'),
            SendOSC(rpijardinport, '/pyta/text/position', 1, 0, -100),
            SendOSC(rpijardinport, '/pyta/text/visible', 1, 1),



    	    SendOSC(rpicourport, '/pyta/text', 3, "[plaʒia]"),
            SendOSC(rpicourport, '/pyta/text/size', 3, 0.15),
            SendOSC(rpicourport, '/pyta/text/align', 3, 'center', 'top'),
            SendOSC(rpicourport, '/pyta/text/position', 3, 0, -100),
    	    SendOSC(rpicourport, '/pyta/text/visible', 3, 1),

    	    SendOSC(rpicourport, '/pyta/text', 1, "bakes $hit wiv butter"),
            SendOSC(rpicourport, '/pyta/text/size', 1, 0.07),
            SendOSC(rpicourport, '/pyta/text/align', 1, 'center', 'top'),
            SendOSC(rpicourport, '/pyta/text/position', 1, 0, -230),
            SendOSC(rpicourport, '/pyta/text/visible', 1, 1),

            SendOSC(rpicourport, '/pyta/text/size', 2, 0.035),
            SendOSC(rpicourport, '/pyta/text/align', 2, 'center', 'center'),
            SendOSC(rpicourport, '/pyta/text/position', 2, 0, -100),
            SendOSC(rpicourport, '/pyta/text/visible', 2, 1),

            SendOSC(lightseqport, '/Lightseq/Bpm', 117/9.4),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'fifty_offre_emploi', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'fifty_offre_emploi_strobe', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'fifty_offre_emploi'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'fifty_offre_emploi_strobe'),
            SendOSC(lightseqport, '/Lightseq/Play'),


    	    SendOSC(rpijardinport, '/pyta/text/visible', -1, 1),
    	    SendOSC(rpicourport, '/pyta/text/visible', -1, 1),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -7.0],

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
    orl >> ProgramFilter(4) >> [ # Trap - Bouton 4
        Program(67) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 4),
            SendOSC(slport, '/set', 'tempo', 117),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 117),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(trapcutport, '/Trapcut/Bpm', 234),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(117)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(117)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(117)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(117)),


    	    SendOSC(rpijardinport, '/pyta/slide/visible', 'Mask_1', 1),
            SendOSC(rpicourport, '/pyta/slide/visible', 'Mask_1', 1),
    	    SendOSC(rpijardinport, '/pyta/slide/alpha', 'Mask_1', 2),
            SendOSC(rpicourport, '/pyta/slide/alpha', 'Mask_1', 2),
    	    SendOSC(rpijardinport, '/pyta/slide/alpha', colos, 0.1),
            SendOSC(rpicourport, '/pyta/slide/alpha', colos, 0.1),
    	    SendOSC(rpijardinport, '/pyta/slide/rgb', colos, 0,0,0),
            SendOSC(rpicourport, '/pyta/slide/rgb', colos, 0,0,0),
    	    SendOSC(rpijardinport, '/pyta/slide/zoom', colos, 2),
            SendOSC(rpicourport, '/pyta/slide/zoom', colos, 2),
    	    SendOSC(rpijardinport, '/pyta/slide/zoom', teas, 2),
            SendOSC(rpicourport, '/pyta/slide/zoom', teas, 2),
    	    SendOSC(rpijardinport, '/pyta/slide/rgb', teas, 1,1, 0),
    	    SendOSC(rpicourport, '/pyta/slide/rgb', teas, 1,1, 0),
    	    SendOSC(rpijardinport, '/pyta/slide/alpha', teas, 0.6),
    	    SendOSC(rpicourport, '/pyta/slide/alpha', teas, 0.6),
    	    SendOSC(lightseqport, '/Lightseq/Bpm', 117),
    	    SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'fifty_colo_jardin', 1),
    	    SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'fifty_colo_jardin'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'fifty_colo_cour', 1),
    	    SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'fifty_colo_cour'),
    	    SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'fifty_coffee'),
    	    SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            SendOscState([

                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0], # flute
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0], # percu

		# effet flute
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -7.0],

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
    orl >> ProgramFilter(5) >> [ # Refrain sttagier - Bouton 5
        Program(68) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 64),
            SendOSC(slport, '/set', 'tempo', 125),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),


            SendOSC(audioseqport, '/Audioseq/Scene/Stop', '*'),
            SendOSC(audioseqport, '/Audioseq/Bpm', 125),
            SendOSC(audioseqport, '/Audioseq/Play', timestamp),
            SendOSC(audioseqport, '/Audioseq/Sequence/Enable', 'fifty_refrain_stagiaire'),


            SendOSC(klickport, '/klick/simple/set_tempo', 125),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(125)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(125)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(125 * 2)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(125 * 2)),

    	    SendOSC(lightseqport, '/Lightseq/Bpm', 125),
    	    SendOSC(rpijardinport, '/pyta/slide/alpha', twerks, 1),
    	    SendOSC(rpicourport, '/pyta/slide/alpha', twerks, 1),
    	    SendOSC(rpijardinport, '/pyta/slide/scale', twerks, 800, 600, 1),
    	    SendOSC(rpicourport, '/pyta/slide/scale', twerks, 800, 600, 1),
    	    SendOSC(rpicourport, '/pyta/slide/rotate_y', twerks, 0),

    	    SendOSC(rpijardinport, '/pyta/slide/rotate_z', twerks_beauf, 180),
    	    SendOSC(rpicourport, '/pyta/slide/rotate_z', twerks_beauf, 180),

    	    SendOSC(rpijardinport, '/pyta/slide/rgb', twerks, 2, 0, 0),
    	    SendOSC(rpicourport, '/pyta/slide/rgb', twerks, 2, 0, 0),

    	    SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'fifty_twerk', 1),
    	    SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'fifty_twerk'),

    	    SendOSC(rpicourport, '/pyta/text/size', 2, 0.1),
    	    SendOSC(rpicourport, '/pyta/text/size', 0, 0.2),
    	    SendOSC(rpijardinport, '/pyta/text/size', 2, 0.1),
    	    SendOSC(rpijardinport, '/pyta/text/size', 0, 0.2),


    	    # SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'fifty_twerk_cour', 1),
    	    # SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'fifty_twerk_cour'),
    	    SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'fifty_stagier'),
    	    SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0], # gtr
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0], # flute
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0], # percu

		# effet flute
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -7.0],

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
    orl >> ProgramFilter(6) >> [ # Pont afro - Bount 6
        #TODO son synthé
        Program(69) >> cseqtrigger,
        [

            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 125),

            SendOSC(klickport, '/klick/simple/set_tempo', 125),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(125)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(125)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(125)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(125)),

    		#TODO Positionnement
    	    SendOSC(rpijardinport, '/pyta/text', 2, 'nAfr0-tRap'),
    	    SendOSC(rpicourport, '/pyta/text', 1, 'NYMPH0 TRAP'),
    	    SendOSC(rpijardinport, '/pyta/text/size', 2, 0.12),
    	    SendOSC(rpicourport, '/pyta/text/size', 1, 0.2),
    	    SendOSC(rpijardinport, '/pyta/text/alpha', 2, 0.5),
    	    SendOSC(rpicourport, '/pyta/text/alpha', 1, 0.5),
    	    SendOSC(rpijardinport, '/pyta/text/visible', 2, 1),
    	    SendOSC(rpijardinport, '/pyta/text/strobe', 2, 1, 12, 0.5),
    	    SendOSC(rpijardinport, '/pyta/text/alpha', 2, 0.5),
    	    SendOSC(rpicourport, '/pyta/text/visible', 1, 1),
    	    SendOSC(rpicourport, '/pyta/text/strobe', 1, 1, 11, 0.5),
    	    SendOSC(rpijardinport, '/pyta/text/alpha', 1, 0.5),


    	    SendOSC(lightseqport, '/Lightseq/Bpm', 125),
    	    SendOSC(rpijardinport, '/pyta/slide/alpha', twerks, 0.15),
    	    SendOSC(rpicourport, '/pyta/slide/alpha', twerks, 0.15),
    	    SendOSC(rpijardinport, '/pyta/slide/scale', twerks, 800, 600, 1),
    	    SendOSC(rpicourport, '/pyta/slide/scale', twerks, 800, 600, 1),
    	    SendOSC(rpicourport, '/pyta/slide/rotate_y', twerks, 180),
    	    SendOSC(rpijardinport, '/pyta/slide/rotate_z', twerks_beauf, 180),
    	    SendOSC(rpicourport, '/pyta/slide/rotate_z', twerks_beauf, 180),
    	    SendOSC(rpijardinport, '/pyta/slide/rgb', twerks, 2, -1, 0),
    	    SendOSC(rpicourport, '/pyta/slide/rgb', twerks, 2, -1, 0),

    	    SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'fifty_nymphotrap_blow'),
    	    SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'fifty_twerk', 1),
    	    SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'fifty_twerk'),
    	    SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            SendOSC(slport, '/sl/-1/hit', 'pause_on'),


            vxorlgars_on,
            vxorlmeuf_off,
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
    orl >> ProgramFilter(7) >> [ # Pont afro 2 - Bount 7
        #TODO son synthé
        Program(69) >> cseqtrigger,
        [

            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 125),

            SendOSC(klickport, '/klick/simple/set_tempo', 125),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(125)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(125)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(125)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(125)),

    	    SendOSC(lightseqport, '/Lightseq/Bpm', 125),
    	    SendOSC(rpijardinport, '/pyta/slide/alpha', twerks, 0.15),
    	    SendOSC(rpicourport, '/pyta/slide/alpha', twerks, 0.15),
    	    SendOSC(rpijardinport, '/pyta/slide/scale', twerks, 800, 600, 1),
    	    SendOSC(rpicourport, '/pyta/slide/scale', twerks, 800, 600, 1),
    	    SendOSC(rpicourport, '/pyta/slide/rotate_y', twerks, 180),
    	    SendOSC(rpijardinport, '/pyta/slide/rotate_z', twerks_beauf, 180),
    	    SendOSC(rpicourport, '/pyta/slide/rotate_z', twerks_beauf, 180),
    	    SendOSC(rpijardinport, '/pyta/slide/rgb', twerks, 2, -1, 0),
    	    SendOSC(rpicourport, '/pyta/slide/rgb', twerks, 2, -1, 0),

    	    SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'fifty_twerk', 1),
    	    SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'fifty_twerk'),
    	    SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            SendOSC(slport, '/sl/-1/hit', 'pause_on'),


            vxorlgars_on,
            vxorlmeuf_off,
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

    # orl >> ProgramFilter(7) >> [ # Refrain - Bouton 7
    #     Program(69) >> cseqtrigger,
    #     [
    #         SendOSC(audioseqport, '/Audioseq/Scene/Stop', '*'),
    #         SendOSC(audioseqport, '/Audioseq/Bpm', 117),
    #         SendOSC(audioseqport, '/Audioseq/Play', timestamp),
    #         SendOSC(audioseqport, '/Audioseq/Sequence/Enable', 'fifty_refrain_cutdown'),
    #
    #         SendOSC(slport, '/set', 'eighth_per_cycle', 8), # bolos c du 3/4
    #         SendOSC(slport, '/set', 'tempo', 117),
    #         SendOSC(slport, '/sl/-1/hit', 'pause_on'),
    #
    #         SendOSC(klickport, '/klick/simple/set_tempo', 117),
    #         SendOSC(klickport, '/klick/simple/set_meter', 3, 4),
    #         SendOSC(klickport, '/klick/simple/set_pattern', 'Xxx'),
    #         SendOSC(klickport, '/klick/metro/start'),
    #
    #         SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(117)),
    #         SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(117)),
    #         SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(117)),
    #         SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(117)),
    #
    #         SendOscState([
    #
    #             [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],
    #
    #         ]),
    #
    #         vxorlgars_on,
    #         vxorlmeuf_off,
    #         vxorldisint_off,
    #         vxorldelay_off,
    #         vxorlvocode_off,
    #
    #         vxjeannotdelay_off,
    #         vxjeannotgars_on,
    #         vxjeannotmeuf_off,
    #         vxjeannotdisint_off,
    #         vxjeannotvocode_off,
    #
    #         bassdry,
    #
    #         ] >> Discard(),
    #     [
    #         bassdetunest_on,
    #         bassringst_on,
    #         bassvibest_off,
    #         bassbufferst_off,
    #         ]
    #     ],
    # jeannot >> ProgramFilter(2) >> [ # boucle rationnelle
    #     SendOSC(56418, '/pedalBoard/button', 4),
    # ],
    # jeannot >> ProgramFilter(3) >> [ # couplet auto
    #     SendOSC(56418, '/pedalBoard/button', 2),
    #     SendOSC(audioseqport, '/Audioseq/Bpm', 117),
    #     SendOSC(audioseqport, '/Audioseq/Scene/Play', 'fifty_couplet_auto', timestamp),
    # ],
    # jeannot >> ProgramFilter(4) >> [ # refrain auto
    #     SendOSC(56418, '/pedalBoard/button', 6),
    # ],
    # jeannot >> ProgramFilter(5) >> [ # refrain direct
    #     SendOSC(56418, '/pedalBoard/button', 7),
    # ],
    orl >> ProgramFilter(11) >> [ # SceneSwitch -> climat (bouton jeannot 2)
        stop,
        SendOSC(audioseqport, '/Audioseq/Scene/Play', 'dafist_outro_filter_reset', timestamp) >> Discard(),
        SceneSwitch(3) >> Discard(),
        Ctrl(102, 127) >> Output('Mk2CtrlOut', 1)
        ],

    jeannot >> ProgramFilter(2) >> [ # Butter
	    SendOSC(lightseqport, '/Lightseq/Scene/Play', 'fifty_butter',timestamp),
    ] >> Discard(),
    jeannot >> ProgramFilter(3) >> [ # Shit
	    SendOSC(lightseqport, '/Lightseq/Scene/Play', 'fifty_shit',timestamp),
    ] >> Discard(),

    jeannot >> ProgramFilter(4) >> [ # Vx jeannot
        vxjeannotdelay_off,
        vxjeannotgars_on,
        vxjeannotmeuf_off,
        vxjeannotdisint_off,
        vxjeannotvocode_off,
    ] >> Discard(),
    jeannot >> ProgramFilter(5) >> [ # Vx jeannot
        vxjeannotgars_off,
        vxjeannotmeuf_on,
        vxjeannotdisint_off,
        vxjeannotdelay_off,
        vxjeannotvocode_off,
    ] >> Discard(),
    jeannot >> ProgramFilter(6) >> [ # Vx jeannot
        vxjeannotgars_off,
        vxjeannotmeuf_off,
        vxjeannotdisint_off,
        vxjeannotdelay_off,
        vxjeannotvocode_on,
    ] >> Discard(),

    jeannot >> ProgramFilter(8) >> [
        SendOSC(trapcutport, '/Trapcut/Scene/Play', 'I'),
	    SendOSC(lightseqport, '/Lightseq/Scene/Play', 'fifty_trapcup', timestamp),
    ] >> Discard()





]
