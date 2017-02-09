import sys
sys.path.append("../Controls/Mididings/")

from ports import *

from liblo import ServerThread, make_method
from time import sleep

bars = ['CJ','BJ','BC','CC']
colors = ['Red','Green','Blue','White']
segments = ['1','2','3','4','5','6','7','8','All']

paths = []
# paths = ['/Decoupes/Jardin/Dimmer','/Decoupes/Cour/Dimmer','/Decoupes/Tyran/Dimmer','/Decoupes/Jeannot/Dimmer']

for bar in bars:
    for color in colors:
        for segment in segments:
            paths.append('/' + bar + '/' + color + '/Segment/' + segment)



class qlcStopper(object):
    def __init__(self, port, qlcappport):
        self.port = port
        if self.port is not None:
            self.server = ServerThread(self.port)
            self.server.register_methods(self)
            self.server.start()

    @make_method('/AllStop', 'i')
    def allStopQlc(self, path, args):
        for path in paths:
            self.server.send(qlcappport, path, 0)

class qlcDelayer(object):
    def __init__(self, port, qlcappport):
        self.port = port
        if self.port is not None:
            self.server = ServerThread(self.port)
            self.server.register_methods(self)
            self.server.start()

    @make_method(None, 'i')
    def sendToQlc(self, path, args):
	sleep(.001)
        self.server.send(qlcappport, path, args[0])





s = qlcStopper(qlcstopport, qlcappport)
d = qlcDelayer(qlcport, qlcappport)



raw_input('Listening on port '+ str(qlcstopport) + ' for Qlc+ AllStop messages and port ' + str(qlcport) + ' for regular messages (which will get a 1ms delay).\nPress enter to quit...')
