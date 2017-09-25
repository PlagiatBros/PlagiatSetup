from mididings import *

try:

    jeannot = PortFilter('PBMk2In') >> Filter(CTRL) >> CtrlFilter(range(101,109)) >> CtrlValueFilter(127) >> NoteOn(EVENT_CTRL, 127) >> Transpose(-101) >> Program(EVENT_NOTE)

    # jeannot = PortFilter('PBMk2In') >> [ Filter(CTRL) >> CtrlFilter(range(101,109)) >> CtrlValueFilter(127) >> NoteOn(EVENT_CTRL, 127) >> Transpose(-101) >> Program(EVENT_NOTE),
    # 					 Filter(PROGRAM) >> [
	# 					ProgramFilter([1,2,3,4]) >> NoteOn(EVENT_PROGRAM, 127) >> Transpose(4) >> Program(EVENT_NOTE),
	# 					ProgramFilter([5,6,7,8]) >> NoteOn(EVENT_PROGRAM, 127) >> Transpose(-4) >> Program(EVENT_NOTE)
	# 					]
	# 				]

    jeannotKeys = PortFilter('PBMk2In') >> [
        Filter(CTRL) >> ~CtrlFilter(range(101,118)),
        ~Filter(CTRL)
    ]

    orl     = PortFilter('PBCtrlIn')

except:

    pass
