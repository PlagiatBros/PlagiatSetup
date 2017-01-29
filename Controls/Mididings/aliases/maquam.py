from mididings import *

zynMaquam = '100.0\n200.0\n300.0\n400.0\n500.0\n600.0\n700.0\n800.0\n900.0\n1000.0\n1100.0\n2/1'
# SendOSC(zynTrebleport, '/microtonal/Penabled', True)
# SendOSC(zynTrebleport, '/microtonal/tunings', zynmaquam)

def maquamNoteFilter(notes, bend):

    def fixBug(ev):
        ev.value = bend
        return ev

    maquam = [
            KeyFilter(notes) >> [
                Filter(NOTEON) >> Pitchbend(bend) >> Process(fixBug),
                Filter(NOTEOFF) >> Pitchbend(0)
            ] >> Output('PBCtrlOut', 1),
            Output('PBCtrlOut', 1)
        ]

    return maquam
