# encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *

from liblo import Server, make_method
from time import sleep

from qlcRegexp import osc_to_regexp

bars = ['CJ','BJ','BC','CC']
colors = ['Red','Green','Blue','White']
segments = ['1','2','3','4','5','6','7','8','All']

paths = []
# paths = ['/Decoupes/Jardin/Dimmer','/Decoupes/Cour/Dimmer','/Decoupes/Tyran/Dimmer','/Decoupes/Jeannot/Dimmer']

for bar in bars:
    for color in colors:
        for segment in segments:
            paths.append('/' + bar + '/' + color + '/Segment/' + segment)




bars_aliases = ['Tutti', 'TuttiLointain','TuttiProche','TuttiJardin','TuttiCour', 'ProcheJardin', 'ProcheCour', 'LointainJardin', 'LointainCour']

possible_paths = []
for bar in bars_aliases:
    for color in colors:
        for segment in segments:
            possible_paths.append('/' + bar + '/' + color + '/Segment/' + segment)




class qlcDelayer(object):
    def __init__(self, port, qlcappport):
        self.port = port
        if self.port is not None:
            self.server = Server(self.port)
            self.server.register_methods(self)

    @make_method('/Stop', None)
    def allStopQlc(self, path, args):
        for path in paths:
            self.server.send(qlcappport, path, 0)
        sleep(0.001)

    @make_method(None, 'i')
    def sendToQlc(self, path, args):

        # regexp
        if '{' in path or '[' in path or '*' in path:
            regexp = osc_to_regexp(path)
            for path in possible_paths:
                match = regexp.match(path)
                if match != None and len(match.string) > 0:
                    # print('regexp match:')
                    # print(match.string)
                    self.sendToQlc(match.string, args)
            return

        # Changement des denominations pour matcher nouveau setup Plagiat (a cause de QLC qui utilise un code binaire pour le path OSC)
        path = path.replace('ProcheCour', 'CC').replace('ProcheJardin', 'BC').replace('LointainJardin', 'CJ').replace('LointainCour', 'BJ')

        # Aliases
        if 'Tutti' in path:
            if 'Lointain' in path:
                multipath=[path.replace('TuttiLointain', 'CJ'), path.replace('TuttiLointain', 'BJ')]
                self.server.send(qlcappport, multipath[0], args[0])
                self.server.send(qlcappport, multipath[1], args[0])

            elif 'Proche' in path:
                multipath=[path.replace('TuttiProche', 'CC'), path.replace('TuttiProche', 'BC')]
                self.server.send(qlcappport, multipath[0], args[0])
                self.server.send(qlcappport, multipath[1], args[0])

            elif 'Jardin' in path:
                multipath=[path.replace('TuttiJardin', 'BC'), path.replace('TuttiJardin', 'CJ')]
                self.server.send(qlcappport, multipath[0], args[0])
                self.server.send(qlcappport, multipath[1], args[0])

            elif 'Cour' in path:
                multipath=[path.replace('TuttiCour', 'CC'), path.replace('TuttiCour', 'BJ')]
                self.server.send(qlcappport, multipath[0], args[0])
                self.server.send(qlcappport, multipath[1], args[0])

            else:
                multipath=[path.replace('Tutti', 'CJ'), path.replace('Tutti', 'BJ'), path.replace('Tutti', 'BC'), path.replace('Tutti', 'CC')]
                self.server.send(qlcappport, multipath[0], args[0])
                self.server.send(qlcappport, multipath[1], args[0])
                self.server.send(qlcappport, multipath[2], args[0])
                self.server.send(qlcappport, multipath[3], args[0])

            return


        self.server.send(qlcappport, path, args[0])



d = qlcDelayer(qlcport, qlcappport)


while d.server:
    d.server.recv(0.001)

# raw_input('Listening on port '+ str(qlcstopport) + ' for Qlc+ AllStop messages and port ' + str(qlcport) + ' for regular messages (which will get a 1ms delay).\nPress enter to quit...')
