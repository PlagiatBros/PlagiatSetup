#encoding: utf-8

from mididings import *
from mididings.extra.osc import SendOSC

from ports import *

from oscSendProxy import OscSendProxy


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
#    SendOSC(vxorlpreport, '/strip/VxORLMeuf/Gain/Mute', 1.0),
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

# VxJeannotVocode
vxjeannotvocode_on= [
    SendOSC(vxorlpostport, '/strip/VxJeannotVocodePost/Gain/Mute', 0.0),
    ] >> Discard()
vxjeannotvocode_off= [
    SendOSC(vxorlpostport, '/strip/VxJeannotVocodePost/Gain/Mute', 1.0),
    ] >> Discard()


#### Bass ####
# Dry #
bassdry = [
    SendOSC(bassmainport, '/strip/BassScapePre/Gain/Mute', 1.0),
    SendOSC(bassmainport, '/strip/BassDegradePre/Gain/Mute', 1.0),
    SendOSC(bassmainport, '/strip/BassWobblePre/Gain/Mute', 1.0),
    ] >> Discard()

# Scape #
bassscape = [
    SendOSC(bassmainport, '/strip/BassScapePre/Gain/Mute', 0.0),
    ] >> Discard()

# Degrade #
bassdegrade = [
    SendOSC(bassmainport, '/strip/BassDegradePre/Gain/Mute', 0.0),
    ] >> Discard()

# Degrade #
basswobble = [
    SendOSC(bassmainport, '/strip/BassWobblePre/Gain/Mute', 0.0),
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
]


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
