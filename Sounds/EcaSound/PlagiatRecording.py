#!/usr/bin/python3


from datetime import datetime
import liblo
import time
from pyeca import *
e = ECA_CONTROL_INTERFACE()
e.command("cs-add PlagiatRecording")

chains = ['Kick', 'OH', 'Basses', 'Samples', 'Keyboards', 'Vx_Missy', 'Vx_Nano', 'Vx_Public', 'Ambiance']

def create_ports():
    for chain in chains:
        e.command("c-add " + chain)
        e.command("ai-add jack")
        e.command("ao-add jack")

def create_wavs():
    timestamp = datetime.now().isoformat(timespec='minutes')
    chemin = '/home/ukbaison/Clips/2017-2018_Plagiat/uk/RehearsalsAndLives/' + timestamp
    subprocess.run(['mkdir', chemin])
    for chain in chains:
        e.command("c-select " + chain)
        e.command("ai-add jack")
        e.command("ao-add jack")
        e.command("ao-add " + chemin + '/' +chain + ".wav")

create_ports()

e.command("cs-connect")
e.command("-G:jack,ecasound,notransport")
e.command("start")


def osc(path, args):
    if path == '/ecasound/start':
        e.command("stop")
        create_wavs()
        e.command("start")
    elif path == '/ecasound/stop':
        e.command("stop")

server = liblo.Server(15003)
server.add_method(None, None, osc)

while 1:
    time.sleep(1)
    server.recv(0)
    print(e.command("engine-status"))
    e.command("get_position")



