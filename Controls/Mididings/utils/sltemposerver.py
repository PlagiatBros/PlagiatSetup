"""
Mididings hooks that gets sooperlooper's tempo updates
Usage:
- instanciate : server = SLTempoServer(port, slhost)
- add server to mididings' hooks:
    hooks(
        server,
        AutoRestart()
    )
- retreive server.getTempo() where needed
"""

from liblo import ServerThread, make_method
from time import sleep
from threading import Thread

class SLTempoServer(ServerThread):
    def __init__(self, port=18000, slhost='127.0.0.1:9951', **kwargs):
        ServerThread.__init__(self, port, **kwargs)
        self.ping = False
        self.tempo = 120
        self.prefix = 'osc.udp://'
        self.slhost = self.prefix + slhost
        self.host =  self.prefix + '127.0.0.1:' + str(port)

    def register(self):
        while self.ping is False and self.running is True:
            self.send(self.slhost, '/get', 'tempo', self.host, '/tempo')
            sleep(1)

    def on_start(self):
        self.start()
        self.running = True

        t = Thread(target=self.register)
        t.start()

        if self.running is True:
            self.send(self.slhost, '/register_update', 'tempo', self.host, '/tempo')

    def on_exit(self):
        self.running = False
        self.send(self.slhost, '/unregister_update', 'tempo', self.host, '/tempo')
        self.stop()

    @make_method('/tempo', None)
    def setTempo(self, path, *args):
        self.tempo = args[0][2]
        if self.ping is False:
            self.ping = True
        print self.tempo

    def getTempo(self):
        return float(self.tempo)
