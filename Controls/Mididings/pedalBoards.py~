# coding=utf8
from mididings import *
from mididings.extra.osc import OSCInterface
from mididings.extra.inotify import AutoRestart
from utils import OSCCustomInterface


config(
	backend='jack',
	client_name='PedalBoardsRoutes',
	out_ports=['PBseq24', 'PBAMSClassicalSynth', 'PBTapeutape', 'PBCtrlOut', 'Mk2CtrlOut', 'PBguitarix', 'Mk2SysexOut'],
	in_ports=['PBCtrlIn', 'PBMk2In', 'PBCmeIn']
)



from scenes import *

hook(
    OSCInterface(56422, 56423), # "osc.udp://CtrlOrl:56423"),
    OSCInterface(57422, 11000), # open-stage-control orl,
    OSCCustomInterface(56418),
    AutoRestart()
)


run(
    scenes = {
        3: SceneGroup("Climat", [
  		Scene("Bass ORL",
                      [
                        climat,
                        basspedal,
                        ]
		),
		Scene("Vx ORL",
                      [
                        climat,
                        vxpedal,
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
		Scene("Pedal Select",
                      [
                        climat,
                        pedalselect,
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
        1: SceneGroup("ConnassesSACEM", [
  		Scene("Bass ORL",
                      [
                        connassessacem,
                        basspedal,
                        ]
		),
		Scene("Vx ORL",
                      [
                        connassessacem,
                        vxpedal,
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
		Scene("Pedal Select",
                      [
                        connassessacem,
                        pedalselect,
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
        4: SceneGroup("Fifty", [
  		Scene("Bass ORL",
                      [
                        fifty,
                        basspedal,
                        ]
		),
		Scene("Vx ORL",
                      [
                        fifty,
                        vxpedal,
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
		Scene("Pedal Select",
                      [
                        fifty,
                        pedalselect,
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
        5: SceneGroup("Le5", [
  		Scene("Bass ORL",
                      [
                        le5,
                        basspedal,
                        ]
		),
		Scene("Vx ORL",
                      [
                        le5,
                        vxpedal,
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
		Scene("Pedal Select",
                      [
                        le5,
                        pedalselect,
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
        6: SceneGroup("Nymphotrap", [
  		Scene("Bass ORL",
                      [
                        nymphotrap,
                        basspedal,
                        ]
		),
		Scene("Vx ORL",
                      [
                        nymphotrap,
                        vxpedal,
                        ]
		),
		Scene("Nope",
                      [
                        nymphotrap,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        nymphotrap,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        nymphotrap,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        nymphotrap,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        nymphotrap,
                        basspedal,
                        ]
		),
		Scene("Pedal Select",
                      [
                        nymphotrap,
                        pedalselect,
                        ]
		),
		Scene("Tune Select",
                      [
                        nymphotrap,
                        basspedal,
                        ]
		),
	    ]
        ),
        61: SceneGroup("Instouboul", [
  		Scene("Bass ORL",
                      [
                        instouboul,
                        basspedal,
                        ]
		),
		Scene("Vx ORL",
                      [
                        instouboul,
                        vxpedal,
                        ]
		),
		Scene("Nope",
                      [
                        instouboul,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        instouboul,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        instouboul,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        instouboul,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        instouboul,
                        basspedal,
                        ]
		),
		Scene("Pedal Select",
                      [
                        instouboul,
                        pedalselect,
                        ]
		),
		Scene("Tune Select",
                      [
                        instouboul,
                        basspedal,
                        ]
		),
	    ]
        ),
        7: SceneGroup("SW", [
  		Scene("Bass ORL",
                      [
                        sw,
                        basspedal,
                        ]
		),
		Scene("Vx ORL",
                      [
                        sw,
                        vxpedal,
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
		Scene("Pedal Select",
                      [
                        sw,
                        pedalselect,
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
        10: SceneGroup("Wholeworld", [
  		Scene("Bass ORL",
                      [
                        wholeworld,
                        basspedal,
                        ]
		),
		Scene("Vx ORL",
                      [
                        wholeworld,
                        vxpedal,
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
		Scene("Pedal Select",
                      [
                        wholeworld,
                        pedalselect,
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
        2: SceneGroup("Da Fist", [
  		Scene("Bass ORL",
                      [
                        dafist,
                        basspedal,
                        ]
		),
		Scene("Vx ORL",
                      [
                        dafist,
                        vxpedal,
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
		Scene("Pedal Select",
                      [
                        dafist,
                        pedalselect,
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
		Scene("Vx ORL",
                      [
                        geturfreakon,
                        vxpedal,
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
		Scene("Pedal Select",
                      [
                        geturfreakon,
                        pedalselect,
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
        9: SceneGroup("Horrorcore", [
  		Scene("Bass ORL",
                      [
                        horrorcore,
                        basspedal,
                        ]
		),
		Scene("Vx ORl",
                      [
                        horrorcore,
                        vxpedal,
                        ]
		),
		Scene("Nope",
                      [
                        horrorcore,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        horrorcore,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        horrorcore,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        horrorcore,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        horrorcore,
                        basspedal,
                        ]
		),
		Scene("Pedal Select",
                      [
                        horrorcore,
                        pedalselect,
                        ]
		),
		Scene("Tune Select",
                      [
                        horrorcore,
                        basspedal,
                        ]
		),
	    ]
        ),
        99: SceneGroup("Trapone", [
  		Scene("Bass ORL",
                      [
                        trapone,
                        basspedal,
                        ]
		),
		Scene("Vx ORL",
                      [
                        trapone,
                        vxpedal,
                        ]
		),
		Scene("Nope",
                      [
                        trapone,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        trapone,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        trapone,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        trapone,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        trapone,
                        basspedal,
                        ]
		),
		Scene("Pedal Select",
                      [
                        trapone,
                        pedalselect,
                        ]
		),
		Scene("Tune Select",
                      [
                        trapone,
                        basspedal,
                        ]
		),
	    ]
        ),

    },
)
