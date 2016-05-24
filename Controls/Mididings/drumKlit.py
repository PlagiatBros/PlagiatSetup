# coding=utf8
from mididings import *
from mididings.extra.osc import OSCInterface
from mididings.extra.inotify import AutoRestart
from mididings.extra.osc import SendOSC
from customosc import OSCCustomInterface

import liblo


config(
	backend='jack',
	client_name='DrumKlitRoutes',
	out_ports=['DKTapeutape'],
	in_ports=['DKJeannotIn']
)

hook(
#    OSCInterface(57422, 57423), # "osc.udp://CtrlOrl:56423"),
#    OSCCustomInterface(57418),
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
samplesmainport=7008
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



#### Outputs ################################################
tapeutape=Output('DKTapeutape',10)


#### Scenes ################################################

#### Slicing ####
slicing = PortFilter('DKJeannotIn') >> [
    Filter(NOTEON) >> 
    [
        KeyFilter(64) >> NoteOn(64, 127),
        ~KeyFilter(64) >> Pass(),
        ]
    ]


#### RUN ###################################################

run(
    scenes = {
        1: SceneGroup("Slicing", [
  		Scene("Slicing",
                      [
                        slicing,
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

