# encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *

from liblo import Server, make_method
from time import sleep
from math import ceil, sin, pi

from qlcRegexp import osc_to_regexp
from barDmxRangeAdapter import barDmxRangeAdapter as bar_adapter

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
        self.damper = {}


        if self.port is not None:
            self.server = Server(self.port)
            self.server.register_methods(self)

    def send(self, port, path, dimmer):
        self.server.send(port, path, bar_adapter(dimmer))

    @make_method('/damper', 'sf')
    def damper_met(self, path, args):
        x = min(max(args[1],0),1)
        self.damper[args[0]] = (sin(x * pi - pi / 2) + 1) / 2
        # print('damper_path ' + str(self.damper_path))
        # print('damper ' + str(self.damper))

    @make_method('/damper/clean', None)
    def damper_clean(self, path, args):
        self.damper = {}

    @make_method('/Stop', None)
    def allStopQlc(self, path, args):
        for path in paths:
            self.server.send(qlcappport, path, 0)
        sleep(0.001)


    @make_method(None, 'i')
    def sendToQlc(self, path, args):

        # Damper
        if path in self.damper:
            dimmer = int(ceil(args[0] * self.damper[path]))
            # print('damped %s : %i (by %f)' % (path, dimmer, self.damper[path]))
        else:
            dimmer = int(args[0])

        # regexp
        if '{' in path or '[' in path or '*' in path:
            regexp = osc_to_regexp(path)
            for path in possible_paths:
                match = regexp.match(path)
                if match != None and len(match.string) > 0:
                    # print('regexp match:')
                    # print(match.string)
                    self.sendToQlc(match.string, [dimmer])
            return




        # Changement des denominations pour matcher nouveau setup Plagiat (a cause de QLC qui utilise un code binaire pour le path OSC)
        path = path.replace('ProcheCour', 'CC').replace('ProcheJardin', 'BC').replace('LointainJardin', 'CJ').replace('LointainCour', 'BJ')

        # Aliases
        if 'Tutti' in path:
            if 'Lointain' in path:
                multipath=[path.replace('TuttiLointain', 'CJ'), path.replace('TuttiLointain', 'BJ')]
                self.send(qlcappport, multipath[0], dimmer)
                self.send(qlcappport, multipath[1], dimmer)

            elif 'Proche' in path:
                multipath=[path.replace('TuttiProche', 'CC'), path.replace('TuttiProche', 'BC')]
                self.send(qlcappport, multipath[0], dimmer)
                self.send(qlcappport, multipath[1], dimmer)

            elif 'Jardin' in path:
                multipath=[path.replace('TuttiJardin', 'BC'), path.replace('TuttiJardin', 'CJ')]
                self.send(qlcappport, multipath[0], dimmer)
                self.send(qlcappport, multipath[1], dimmer)

            elif 'Cour' in path:
                multipath=[path.replace('TuttiCour', 'CC'), path.replace('TuttiCour', 'BJ')]
                self.send(qlcappport, multipath[0], dimmer)
                self.send(qlcappport, multipath[1], dimmer)

            else:
                multipath=[path.replace('Tutti', 'CJ'), path.replace('Tutti', 'BJ'), path.replace('Tutti', 'BC'), path.replace('Tutti', 'CC')]
                self.send(qlcappport, multipath[0], dimmer)
                self.send(qlcappport, multipath[1], dimmer)
                self.send(qlcappport, multipath[2], dimmer)
                self.send(qlcappport, multipath[3], dimmer)

            return


        self.send(qlcappport, path, dimmer)



d = qlcDelayer(qlcport, qlcappport)


while d.server:
    d.server.recv(0)
    sleep(0.001)

# raw_input('Listening on port '+ str(qlcstopport) +
