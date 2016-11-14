# coding=utf8
from mididings import *
from mididings.extra.osc import OSCInterface
from mididings.extra.inotify import AutoRestart
from mididings.extra.osc import SendOSC
from customosc import OSCCustomInterface
from oscSendProxy import OscSendProxy

import liblo


config(
	backend='jack',
	client_name='PedalBoardsRoutes',
	out_ports=['PBseq24', 'PBAMSClassicalSynth', 'PBTapeutape', 'PBCtrlOut'],
	in_ports=['PBCtrlIn']
)

hook(
    OSCInterface(56422, 56423), # "osc.udp://CtrlOrl:56423"),
    OSCCustomInterface(56418),
    AutoRestart()
)


#### Ports OSC ################################################

klickport = 1234
slport = 9951
testport = 1111
# qlcport = ("192.168.0.13", 7772)
# qlcstopport = ("192.168.0.13", 7771)
# #qlcport = 7777
# videoCport = ("192.168.0.31", 56418)
# videoCseqport = 12346
# videoJport = ("192.168.0.30", 56418)
# videoJseqport = 12347
# videoKport = ("192.168.0.32", 56418)
# videoKseqport = 12348
# qlcseqport = 12345 #("CtrlRegie", 12345)
# #videoseqport = ("CtrlDag", 12346)
# audioseqport=12344
# mainseqport = ("CtrlDag", 12343)
# desktoporlport = ("CtrlOrl", 12345)

# Non Mixers

vxorlpreport = 6666
vxorlmeufport = 6667
vxorlpostport = 6668
vxmainport = 6669
vxorlgarsport = 6670

vxjeannotpreport = 6671
vxjeannotmeufport = 6672
vxjeannotgarsport = 6673
vxjeannotpostport = 6674


samplespitchport = 7000
samplesdelaymungeport = 7001
samplesreversedelayport = 7002
samplesringmodport = 7003
samplestremoloport = 7005
samplesscapeport = 7006
samplesdegradeport = 7009
samplesdisintegratorport = 7007
samplesmainport = 7008


bassmainport = 7020
monitorsorlport = 7030
monitorsjeannotport = 7031

# mainmixport = 6666
# drumsport = 6667
# bassesport = 6668
# guitarsport = 6669
# mxsynthport = 6670
# mxdrumsport = 6671
# vocalsport = 6672
# tomsport = 6673
# acousticsport = 6674
# mondagport = 6675
# monjeport = 6676
# monorlport = 6677
# mainsport = 6678


### OSC send proxy #####################################

oscsendproxy = OscSendProxy([
    # SamplesMain
    [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 1.0],
    [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 1.0],
    [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 1.0],
    [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0],
    [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0],
    [samplesmainport, '/strip/SamplesDrumKlit/Gain/Mute', 0.0],
    [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0],
    [samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0],
    [samplesmainport, '/strip/SamplesScape/Gain/Mute', 1.0],
    [samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0],
    [samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0],
    [samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0],
    [samplesmainport, '/strip/SamplesPitch/Gain/Mute', 1.0],
    [samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0],

    # SamplesDelayMunge
    [samplesdelaymungeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdelaymungeport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdelaymungeport, '/strip/Samples5/Gain/Gain%20(dB)/unscaled', -70.0],

    # SamplesReverseDelay
    [samplesreversedelayport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesreversedelayport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesreversedelayport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesreversedelayport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesreversedelayport, '/strip/Samples5/Gain/Gain%20(dB)/unscaled', -70.0],

    # SamplesScape
    [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesscapeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesscapeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesscapeport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesscapeport, '/strip/Samples5/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesscapeport, '/strip/SamplesTremolo/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesscapeport, '/strip/SamplesDegrade/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesscapeport, '/strip/SamplesPitch/Gain/Gain%20(dB)/unscaled', -70.0],

    # SamplesTremolo
    [samplestremoloport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplestremoloport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplestremoloport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplestremoloport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplestremoloport, '/strip/Samples5/Gain/Gain%20(dB)/unscaled', -70.0],

    # SamplesDegrade
    [samplesdegradeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdegradeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdegradeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdegradeport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdegradeport, '/strip/Samples5/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdegradeport, '/strip/SamplesScape/Gain/Gain%20(dB)/unscaled', -70.0],

    # SamplesDisintegrator
    [samplesdisintegratorport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdisintegratorport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdisintegratorport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdisintegratorport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdisintegratorport, '/strip/Samples5/Gain/Gain%20(dB)/unscaled', -70.0],

    # SamplesPitch
    [samplespitchport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplespitchport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplespitchport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplespitchport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplespitchport, '/strip/Samples5/Gain/Gain%20(dB)/unscaled', -70.0],

    # SamplesRingMod
    [samplesringmodport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesringmodport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesringmodport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesringmodport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesringmodport, '/strip/Samples5/Gain/Gain%20(dB)/unscaled', -70.0],


])

SendOscState = oscsendproxy.sendOscState



#### Outputs ################################################
seq24=Output('PBseq24',1)
seq24once=Output('PBseq24',2)

tapeutape=Output('PBTapeutape',10)
tapeutapecontrol=Output('PBTapeutape',1)


#### Functions #############################################
#### Trigger seq24 ####
p_firstpart=[range(1,65)]
p_secondpart=[range(65,129)]

note2seq = ProgramFilter(p_firstpart) >> seq24 # mute-groups seq24
note2seqNplay = ProgramFilter(p_secondpart) >> [ # mute-groups + play
			NoteOn(EVENT_PROGRAM,127) >> Transpose(-62) >> Program('PBseq24',1,EVENT_NOTE) >> seq24,
			Program('PBseq24',1,1),
		]


seq24start = Program('PBseq24',1,1)

seqtrigger = Filter(PROGRAM) >> [
		ChannelFilter(1) >> [ 
             		note2seq,
			note2seqNplay,
		],
		ChannelFilter(2) >> [
			seq24once,
		]
	]

cseqtrigger = Channel(1) >> seqtrigger

#### BPM Scape & Delay Vx ####
# Formule : (x-30)/134.
scapebpmpath = 'C%2A%20Scape%20-%20Stereo%20delay%20with%20chromatic%20resonances/bpm'
# Formule : (x-30)/270.
delaybpmpath = 'Calf%20Vintage%20Delay/Tempo'

#### Vocals ####
# VxORLMeuf
vxorlmeuf_on = [
    SendOSC(vxorlpreport, '/strip/VxORLMeuf/Gain/Mute', 0.0),
    SendOSC(vxorlpostport, '/strip/VxORLMeufPost/Gain/Mute', 0.0),
    ] >> Discard()

vxorlmeuf_off = [
    SendOSC(vxorlpreport, '/strip/VxORLMeuf/Gain/Mute', 1.0),
    SendOSC(vxorlpostport, '/strip/VxORLMeufPost/Gain/Mute', 1.0),
    ] >> Discard()

# VxORLGars
vxorlgars_on = [
    SendOSC(vxorlpreport, '/strip/VxORLGars/Gain/Mute', 0.0),
    SendOSC(vxorlpostport, '/strip/VxORLGarsPost/Gain/Mute', 0.0),
    ] >> Discard()

vxorlgars_off = [
    SendOSC(vxorlpreport, '/strip/VxORLGars/Gain/Mute', 1.0),
    SendOSC(vxorlpostport, '/strip/VxORLGarsPost/Gain/Mute', 1.0),
    ] >> Discard()

# VxORLDisint
vxorldisint_on = [
    SendOSC(vxorlpreport, '/strip/VxORLDisint/Gain/Mute', 0.0),
    SendOSC(vxorlpostport, '/strip/VxORLDisintPost/Gain/Mute', 0.0),
    ] >> Discard()

vxorldisint_off = [
    SendOSC(vxorlpreport, '/strip/VxORLDisint/Gain/Mute', 1.0),
    SendOSC(vxorlpostport, '/strip/VxORLDisintPost/Gain/Mute', 1.0),
    ] >> Discard()

# VxORLDelay
vxorldelay_on = [
    SendOSC(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 0.0),
    SendOSC(vxorlpostport, '/strip/VxORLDelayPost/Gain/Mute', 0.0),
    ] >> Discard()

vxorldelay_off = [
    SendOSC(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 1.0),
    SendOSC(vxorlpostport, '/strip/VxORLDelayPost/Gain/Mute', 1.0),
    ] >> Discard()

# VxORLVocode
vxorlvocode_on= [
    SendOSC(vxorlpostport, '/strip/VxORLVocodePost/Gain/Mute', 0.0),
    ] >> Discard()
vxorlvocode_off= [
    SendOSC(vxorlpostport, '/strip/VxORLVocodePost/Gain/Mute', 1.0),
    ] >> Discard()

# VxJeannotMeuf
vxjeannotmeuf_on = [
    SendOSC(vxjeannotpreport, '/strip/VxJeannotMeuf/Gain/Mute', 0.0),
    SendOSC(vxjeannotpostport, '/strip/VxJeannotMeufPost/Gain/Mute', 0.0),
    ] >> Discard()

vxjeannotmeuf_off = [
    SendOSC(vxjeannotpreport, '/strip/VxJeannotMeuf/Gain/Mute', 1.0),
    SendOSC(vxjeannotpostport, '/strip/VxJeannotMeufPost/Gain/Mute', 1.0),
    ] >> Discard()

# VxJeannotGars
vxjeannotgars_on = [
    SendOSC(vxjeannotpreport, '/strip/VxJeannotGars/Gain/Mute', 0.0),
    SendOSC(vxjeannotpostport, '/strip/VxJeannotGarsPost/Gain/Mute', 0.0),
    ] >> Discard()

vxjeannotgars_off = [
    SendOSC(vxjeannotpreport, '/strip/VxJeannotGars/Gain/Mute', 1.0),
    SendOSC(vxjeannotpostport, '/strip/VxJeannotGarsPost/Gain/Mute', 1.0),
    ] >> Discard()

# VxJeannotDisint
vxjeannotdisint_on = [
    SendOSC(vxjeannotpreport, '/strip/VxJeannotDisint/Gain/Mute', 0.0),
    SendOSC(vxjeannotpostport, '/strip/VxJeannotDisintPost/Gain/Mute', 0.0),
    ] >> Discard()

vxjeannotdisint_off = [
    SendOSC(vxjeannotpreport, '/strip/VxJeannotDisint/Gain/Mute', 1.0),
    SendOSC(vxjeannotpostport, '/strip/VxJeannotDisintPost/Gain/Mute', 1.0),
    ] >> Discard()

# VxJeannotDelay
vxjeannotdelay_on = [
    SendOSC(vxjeannotpreport, '/strip/VxJeannotDelayPre/Gain/Mute', 0.0),
    SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/Gain/Mute', 0.0),
    ] >> Discard()

vxjeannotdelay_off = [
    SendOSC(vxjeannotpreport, '/strip/VxJeannotDelayPre/Gain/Mute', 1.0),
    SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/Gain/Mute', 1.0),
    ] >> Discard()

#### Bass ####
# Dry #
bassdry = [
    SendOSC(bassmainport, '/strip/BassScapePre/Gain/Mute', 1.0),
    SendOSC(bassmainport, '/strip/BassDegradePre/Gain/Mute', 1.0),    
    ] >> Discard()

# Scape #
bassscape = [
    SendOSC(bassmainport, '/strip/BassScapePre/Gain/Mute', 0.0),
    ] >> Discard()

# Degrade #
bassdegrade = [
    SendOSC(bassmainport, '/strip/BassDegradePre/Gain/Mute', 0.0),
    ] >> Discard()

# Bass Pedal
basspedal= [
    ProgramFilter(13) >> SendOSC(slport, '/sl/0/hit', 'record') >> Discard(),
    ProgramFilter(14) >> SendOSC(slport, '/sl/0/hit', 'pause_on') >> Discard(),
    ProgramFilter(15) >> SendOSC(slport, '/sl/0/hit', 'overdub') >> Discard(),
    ProgramFilter(16) >> SendOSC(slport, '/sl/0/hit', 'multiply') >> Discard(),
#    ProgramFilter(18) >> SendOSC(slport, '/sl/0/hit', 'trigger') >> Discard(),
    ProgramFilter(17) >> SendOSC(slport, '/sl/1/hit', 'record') >> Discard(),
    ProgramFilter(18) >> SendOSC(slport, '/sl/1/hit', 'pause_on') >> Discard(),
    ProgramFilter(19) >> SendOSC(slport, '/sl/1/hit', 'overdub') >> Discard(),
    ProgramFilter(20) >> SendOSC(slport, '/sl/1/hit', 'multiply') >> Discard(),
#    ProgramFilter(18) >> SendOSC(slport, '/sl/0/hit', 'trigger') >> Discard(),
    ProgramFilter(23) >> bassdry,
    ProgramFilter(22) >> bassscape,
    ProgramFilter(21) >> bassdegrade,
    ]

#### Vocals ####

#### Stop ####
stop = [
        Program(2) >> cseqtrigger,
        SendOSC(slport, '/sl/-1/hit', 'pause_on') >> Discard(),
        SendOSC(klickport, '/klick/metro/stop') >> Discard(),

        # [
        #     SendOSC(qlcstopport, '/AllStop', 1),
        #     SendOSC(qlcseqport, '/Sequencer/DisableAll', 1),
        #     SendOSC(videoCseqport, '/Sequencer/DisableAll', 1),
        #     SendOSC(videoCport, '/pyta/slide/visible', -1, 0),
        #     SendOSC(videoJseqport, '/Sequencer/DisableAll', 1),
        #     SendOSC(videoJport, '/pyta/slide/visible', -1, 0),
        #     SendOSC(videoKseqport, '/Sequencer/DisableAll', 1),
        #     SendOSC(videoKport, '/pyta/slide/visible', -1, 0),
        #     SendOSC(audioseqport, '/Sequencer/DisableAll', 1),
        #     ] >> Discard()
]

#### FX Pedals #############################################
# ORL

#### Scenes ################################################

#### Climat ####
climat = PortFilter('PBCtrlIn') >> [
    Filter(PROGRAM) >> Ctrl(0, 0) >> tapeutapecontrol,
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Couplet - Bouton 2
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
    ProgramFilter(3) >> [ # Refrain - Bouton 3
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

    ProgramFilter(4) >> [ # The shit - Bouton 4
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

    ProgramFilter(5) >> [ # Transe Pédé - Bouton 5
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

    ProgramFilter(6) >> [ # Transe Pédé (2) - Bouton 6
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

    ProgramFilter(7) >> [ # Transe Pédé (2) - Bouton 7
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

#### ConnassesSACEM ####
connassessacem = PortFilter('PBCtrlIn') >> [
    Filter(PROGRAM) >> Ctrl(0, 1) >> tapeutapecontrol,
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Thème Intro - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 125),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 125),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.708955),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.708955),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.35185),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -7.0],
            
            ]),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_off,

            vxjeannotdelay_on,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,

            ] >> Discard()
        ],
    ProgramFilter(3) >> [ # Thème Intro - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 125),

            SendOSC(klickport, '/klick/simple/set_tempo', 125),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.708955),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.708955),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.35185),

            SendOscState([
                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB]/unscaled', -7.0],

            ]),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_off,

            vxjeannotdelay_on,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,

            ] >> Discard()
        ],

    ]


#### Fifty ####
fifty = PortFilter('PBCtrlIn') >> [
    Filter(PROGRAM) >> Ctrl(0, 2) >> tapeutapecontrol,
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Couplet - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 64),
            SendOSC(slport, '/set', 'tempo', 117),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 117),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.64925),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.64925),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.32222),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB]/unscaled', -7.0],
            
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
    ProgramFilter(3) >> [ # Pont Refrain - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 117),

            SendOSC(klickport, '/klick/simple/set_tempo', 117),
            SendOSC(klickport, '/klick/simple/set_meter', 3, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.64925),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.64925),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.32222),


            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOscState([

                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

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
    ProgramFilter(4) >> [ # Refrain - Bouton 4
        Program(67) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 117),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 117),
            SendOSC(klickport, '/klick/simple/set_meter', 3, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.64925),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.64925),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.32222),

            SendOscState([

                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

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
    ProgramFilter(5) >> [ # Couplet avec boucle - Bouton 5
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 64),
            SendOSC(slport, '/set', 'tempo', 117),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),
            SendOSC(slport, '/sl/0/set', 'play_sync', 0),            
            SendOSC(slport, '/sl/0/hit', 'pause_off'),
            SendOSC(slport, '/sl/0/hit', 'trigger'),
            SendOSC(slport, '/sl/0/set', 'play_sync', 1),            

            SendOSC(klickport, '/klick/simple/set_tempo', 117),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.64925),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.64925),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.32222),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB]/unscaled', -7.0],
            
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
    ProgramFilter(6) >> [ # Boucle rationnelle - Bouton 6
        Program(68) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 64),
            SendOSC(slport, '/set', 'tempo', 117),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 117),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.64925),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.64925),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.32222),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB]/unscaled', -7.0],
            
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

#### Le5 ####
le5 = PortFilter('PBCtrlIn') >> [
    Filter(PROGRAM) >> Ctrl(0, 3) >> tapeutapecontrol,
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Intro - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.48148),

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

            bassdry,
            ] >> Discard()
        ],
    ProgramFilter(3) >> [ # Couplet A - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.48148),

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

            bassdry,
            ] >> Discard()
        ],
    ProgramFilter(4) >> [ # Couplet B - Bouton 4
        Program(67) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.48148),

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

            bassdry,
            ] >> Discard()
        ],
    ProgramFilter(5) >> [ # Couplet C - Bouton 5
        Program(68) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.48148),

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

            bassdry,
            ] >> Discard()
        ],
    ProgramFilter(6) >> [ # Refrain - Bouton 6
        Program(69) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.48148),

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
            ] >> Discard()
        ],
    ProgramFilter(7) >> [ # Couplet A - Bouton 7 - #TODO INUTILE?
        Program(70) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 80),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.48148),

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

            bassdry,
            ] >> Discard()
        ],
    ProgramFilter(8) >> [ # Couplet Bbis - Bouton 8
        Program(71) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 80),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.48148),

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
            ] >> Discard()
        ],
    ProgramFilter(9) >> [ # Couplet Cbis - Bouton 9
        Program(72) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.48148),

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
            ] >> Discard()
        ],

    ProgramFilter(10) >> [ # Transe Pédé - Bouton 10
        Program(73) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.48148),

            SendOscState([

                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 0.0],
                [samplesdegradeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -12.0],
                [samplesdegradeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -9.0],
                [samplesdegradeport, '/strip/SamplesTremolo/Gain/Gain%20(dB)/unscaled', -6.0],
                [samplestremoloport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -6.0],

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
            ] >> Discard()
        ],

    ProgramFilter(11) >> [ # Transe Pédé - Bouton 11
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.9701),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.48148),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 0.0],

                [samplesdegradeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -12.0],
                [samplesdegradeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -9.0],
                [samplesdegradeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -4.0],
                [samplesdisintegratorport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -4.0],
                [samplestremoloport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -6.0],
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
            ] >> Discard()
        ],
    ]


#### SW ####
sw = PortFilter('PBCtrlIn') >> [
    Filter(PROGRAM) >> Ctrl(0, 4) >> tapeutapecontrol,
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Couplet - Bouton 2
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
            ] >> Discard()
        ],
    ProgramFilter(3) >> [ # Couplet - Bouton 3
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
            ] >> Discard()
        ],

    ProgramFilter(4) >> [ # Refrain - Bouton 4
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

            vxjeannotdelay_on,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_on,
            ] >> Discard()
        ],

    ProgramFilter(5) >> [ # Couplet - Bouton 5
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
            ] >> Discard()
        ],

    ]

#### Whole World ####
wholeworld = PortFilter('PBCtrlIn') >> [
    Filter(PROGRAM) >> Ctrl(0, 5) >> tapeutapecontrol,
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Couplet - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 90),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 90),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.44776),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.44776),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.2222),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -6.0],

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
            ] >> Discard()
        ],
    ProgramFilter(3) >> [ # Refrain - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 90),

            SendOSC(klickport, '/klick/simple/set_tempo', 90),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.44776),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.44776),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.2222),

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

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            ] >> Discard()
        ],
    ProgramFilter(4) >> [ # Pont - Bouton 4
        Program(67) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 90),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 90),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.44776),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.44776),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.2222),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -6.0],

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
            ] >> Discard()
        ],

    ProgramFilter(5) >> [ # Pont - Bouton 5
        Program(68) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 90),

            SendOSC(klickport, '/klick/simple/set_tempo', 90),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.44776),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.44776),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.2222),

            SendOscState([

                [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -6.0],

            ]),

            vxorlgars_on,
            vxorlmeuf_on,
            vxorldisint_on,
            vxorldelay_on,
            vxorlvocode_off,

            vxjeannotdelay_on,
            vxjeannotgars_on,
            vxjeannotmeuf_on,
            vxjeannotdisint_on,

            bassscape,
            bassdegrade,
            ] >> Discard()
        ],
    ]

#### Da Fist ####
dafist = PortFilter('PBCtrlIn') >> [
    Filter(PROGRAM) >> Ctrl(0, 6) >> tapeutapecontrol,
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Intro Thème - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.3333),


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
            ] >> Discard()
        ],
    ProgramFilter(3) >> [ # Intro Thème 2 - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.3333),

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
            ] >> Discard()
        ],
    ProgramFilter(4) >> [ # Couplet - Bouton 4
        Program(67) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.3333),

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
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            ] >> Discard()
        ],
    ProgramFilter(5) >> [ # Couplet part 2 - Bouton 5
        Program(68) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),    

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.3333),

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
            ] >> Discard()
        ],
    ProgramFilter(6) >> [ # Intro Refrain - Bouton 6
        Program(69) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.3333),

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
            ] >> Discard()
        ],
    ProgramFilter(7) >> [ # Refrain - Bouton 7
        Program(70) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.3333),

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
            ] >> Discard()
        ],

    ProgramFilter(8) >> [ # Refrain - Bouton 8
        Program(71) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.6716),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.3333),

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

            bassscape,
            ] >> Discard()
        ],
    ]


#### Get Ur Freak On ####
geturfreakon = PortFilter('PBCtrlIn') >> [
    Filter(PROGRAM) >> Ctrl(0, 7) >> tapeutapecontrol,
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Couplet - Bouton 2
#        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 200),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 200),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.522388),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.522388),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.6296),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],

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
            ] >> Discard()
        ],
    ProgramFilter(3) >> [ # Couplet - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 200),

            SendOSC(klickport, '/klick/simple/set_tempo', 200),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.522388),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.522388),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.6296),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],

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
            ] >> Discard()
        ],
    ]

#### SlowMotium ####
slowmotium = PortFilter('PBCtrlIn') >> [
    Filter(PROGRAM) >> Ctrl(0, 8) >> tapeutapecontrol,
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Couplet - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 200),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 200),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.522388),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.522388),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.6296),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],

            ]),


            vxorlgars_off,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_on,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            ] >> Discard()
        ],

#### RUN ###################################################

run(
    scenes = {
        1: SceneGroup("Climat", [
  		Scene("Bass ORL",
                      [
                        climat,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        climat,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        climat,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        climat,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        climat,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        climat,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        climat,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        climat,
                        basspedal,
                        ]
		),
		Scene("Tune Select",
                      [
                        climat,
                        basspedal,
                        ]
		),
	    ]
        ),
        2: SceneGroup("ConnassesSACEM", [
  		Scene("Bass ORL",
                      [
                        connassessacem,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        connassessacem,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        connassessacem,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        connassessacem,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        connassessacem,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        connassessacem,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        connassessacem,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        connassessacem,
                        basspedal,
                        ]
		),
		Scene("Tune Select",
                      [
                        connassessacem,
                        basspedal,
                        ]
		),
	    ]
        ),
        3: SceneGroup("Fifty", [
  		Scene("Bass ORL",
                      [
                        fifty,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        fifty,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        fifty,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        fifty,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        fifty,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        fifty,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        fifty,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        fifty,
                        basspedal,
                        ]
		),
		Scene("Tune Select",
                      [
                        fifty,
                        basspedal,
                        ]
		),
	    ]
        ),
        4: SceneGroup("Le5", [
  		Scene("Bass ORL",
                      [
                        le5,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        le5,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        le5,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        le5,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        le5,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        le5,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        le5,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        le5,
                        basspedal,
                        ]
		),
		Scene("Tune Select",
                      [
                        le5,
                        basspedal,
                        ]
		),
	    ]
        ),
        5: SceneGroup("SW", [
  		Scene("Bass ORL",
                      [
                        sw,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        sw,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        sw,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        sw,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        sw,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        sw,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        sw,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        sw,
                        basspedal,
                        ]
		),
		Scene("Tune Select",
                      [
                        sw,
                        basspedal,
                        ]
		),
	    ]
        ),
        6: SceneGroup("Wholeworld", [
  		Scene("Bass ORL",
                      [
                        wholeworld,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        wholeworld,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        wholeworld,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        wholeworld,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        wholeworld,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        wholeworld,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        wholeworld,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        wholeworld,
                        basspedal,
                        ]
		),
		Scene("Tune Select",
                      [
                        wholeworld,
                        basspedal,
                        ]
		),
	    ]
        ),
        7: SceneGroup("Da Fist", [
  		Scene("Bass ORL",
                      [
                        dafist,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        dafist,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        dafist,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        dafist,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        dafist,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        dafist,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        dafist,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        dafist,
                        basspedal,
                        ]
		),
		Scene("Tune Select",
                      [
                        dafist,
                        basspedal,
                        ]
		),
	    ]
        ),
        8: SceneGroup("GetYourFreakOn", [
  		Scene("Bass ORL",
                      [
                        geturfreakon,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        geturfreakon,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        geturfreakon,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        geturfreakon,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        geturfreakon,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        geturfreakon,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        geturfreakon,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        geturfreakon,
                        basspedal,
                        ]
		),
		Scene("Tune Select",
                      [
                        geturfreakon,
                        basspedal,
                        ]
		),
	    ]
        ),
        # 2: SceneGroup("", [
  	# 	Scene("Bass ORL",
        #               [
        #                 acte1,
        #                 orl_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar ORL",
        #               [
        #                 acte1,
        #                 orl_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix ORL",
        #               [
        #                 acte1,
        #                 orl_vxpedal
        #                 ]
	#         ),
	# 	Scene("Bass Dag",
        #               [
        #                 acte1,
        #                 dag_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar Dag",
        #               [
        #                 acte1,
        #                 dag_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix Dag",
        #               [
        #                 acte1,
        #                 dag_vxpedal
        #                 ]
	# 	),
	# 	Scene("Boucles",
        #               acte1
	# 	),
	# 	Scene("Bank Select",
        #               acte1
	# 	),
	# 	Scene("Tune Select",
        #               acte1
	# 	)
	#     ]
        # ),
        # 3: SceneGroup("Acte II", [
  	# 	Scene("Bass ORL",
        #               [
        #                 acte2,
        #                 orl_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar ORL",
        #               [
        #                 acte2,
        #                 orl_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix ORL",
        #               [
        #                 acte2,
        #                 orl_vxpedal
        #                 ]
	#         ),
	# 	Scene("Bass Dag",
        #               [
        #                 acte2,
        #                 dag_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar Dag",
        #               [
        #                 acte2,
        #                 dag_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix Dag",
        #               [
        #                 acte2,
        #                 dag_vxpedal
        #                 ]
	# 	),
	# 	Scene("Boucles",
        #               acte2
	# 	),
	# 	Scene("Bank Select",
        #               acte2
	# 	),
	# 	Scene("Tune Select",
        #               acte2
	# 	)
	#     ]
        # ),
        # 4: SceneGroup("Forain Acte II", [
  	# 	Scene("Bass ORL",
        #               [
        #                 forainacte2,
        #                 orl_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar ORL",
        #               [
        #                 forainacte2,
        #                 orl_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix ORL",
        #               [
        #                 forainacte2,
        #                 orl_vxpedal
        #                 ]
	#         ),
	# 	Scene("Bass Dag",
        #               [
        #                 forainacte2,
        #                 dag_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar Dag",
        #               [
        #                 forainacte2,
        #                 dag_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix Dag",
        #               [
        #                 forainacte2,
        #                 dag_vxpedal
        #                 ]
	# 	),
	# 	Scene("Boucles",
        #               forainacte2
	# 	),
	# 	Scene("Bank Select",
        #               forainacte2
	# 	),
	# 	Scene("Tune Select",
        #               forainacte2
	# 	)
	#     ]
        # ),
        # 5: SceneGroup("Acte III", [
  	# 	Scene("Bass ORL",
        #               [
        #                 acte3,
        #                 orl_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar ORL",
        #               [
        #                 acte3,
        #                 orl_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix ORL",
        #               [
        #                 acte3,
        #                 orl_vxpedal
        #                 ]
	#         ),
	# 	Scene("Bass Dag",
        #               [
        #                 acte3,
        #                 dag_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar Dag",
        #               [
        #                 acte3,
        #                 dag_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix Dag",
        #               [
        #                 acte3,
        #                 dag_vxpedal
        #                 ]
	# 	),
	# 	Scene("Boucles",
        #               acte3
        #               ),
	# 	Scene("Bank Select",
        #               acte3
        #               ),
	# 	Scene("Tune Select",
        #               acte3
	# 	)
	#     ]
        # ),
        # 6: SceneGroup("Acte III Part II", [
  	# 	Scene("Bass ORL",
        #               [
        #                 acte3partII,
        #                 orl_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar ORL",
        #               [
        #                 acte3partII,
        #                 orl_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix ORL",
        #               [
        #                 acte3partII,
        #                 orl_vxpedal
        #                 ]
	#         ),
	# 	Scene("Bass Dag",
        #               [
        #                 acte3partII,
        #                 dag_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar Dag",
        #               [
        #                 acte3partII,
        #                 dag_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix Dag",
        #               [
        #                 acte3partII,
        #                 dag_vxpedal
        #                 ]
	# 	),
	# 	Scene("Boucles",
        #               acte3partII
	# 	),
	# 	Scene("Bank Select",
        #               acte3partII
	# 	),
	# 	Scene("Tune Select",
        #               acte3partII
	# 	)
	#     ]
        # ),
        # 7: SceneGroup("Acte III Part III", [
  	# 	Scene("Bass ORL",
        #               [
        #                 acte3partIII,
        #                 orl_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar ORL",
        #               [
        #                 acte3partIII,
        #                 orl_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix ORL",
        #               [
        #                 acte3partIII,
        #                 orl_vxpedal
        #                 ]
	#         ),
	# 	Scene("Bass Dag",
        #               [
        #                 acte3partIII,
        #                 dag_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar Dag",
        #               [
        #                 acte3partIII,
        #                 dag_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix Dag",
        #               [
        #                 acte3partIII,
        #                 dag_vxpedal
        #                 ]
	# 	),
	# 	Scene("Boucles",
        #               acte3partIII,
	# 	),
	# 	Scene("Bank Select",
        #               acte3partIII
	# 	),
	# 	Scene("Tune Select",
        #               acte3partIII
	# 	)
	#     ]
        # ),
        # 8: SceneGroup("Acte IV", [
  	# 	Scene("Bass ORL",
        #               [
        #                 acte4,
        #                 orl_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar ORL",
        #               [
        #                 acte4,
        #                 orl_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix ORL",
        #               [
        #                 acte4,
        #                 orl_vxpedal
        #                 ]
	#         ),
	# 	Scene("Bass Dag",
        #               [
        #                 acte4,
        #                 dag_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar Dag",
        #               [
        #                 acte4,
        #                 dag_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix Dag",
        #               [
        #                 acte4,
        #                 dag_vxpedal
        #                 ]
	# 	),
	# 	Scene("Boucles",
	# 	    acte4
	# 	),
	# 	Scene("Bank Select",
	# 	    acte4
	# 	),
	# 	Scene("Tune Select",
	# 	    acte4
	# 	)
	#     ]
        # ),

    },
)

