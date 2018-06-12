from mididings import *

try:

    jeannot = PortFilter('PBMk2In') >> Filter(CTRL) >> CtrlFilter(range(101,109)) >> CtrlValueFilter(127) >> NoteOn(EVENT_CTRL, 127) >> Transpose(-101) >> Program(EVENT_NOTE)
    jeannot_sustain = PortFilter('PBMk2In') >> Filter(CTRL) >> CtrlFilter(64) >> CtrlValueFilter(127) 
 

    jeannot_padrelease = PortFilter('PBMk2In') >> Filter(CTRL) >> CtrlFilter(range(101,117)) >> CtrlValueFilter(0)

    orl     = PortFilter('PBCtrlIn')

except:

    pass
