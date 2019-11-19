from ports import *

from liblo import Server, send
from time import sleep

server = Server(vxpitchshifterport)

def handler(path, *args):
    fval = args[0][0]
    val = 0
    if fval < 1:
        val = fval * 24 / 0.75 + (-24 / 0.75)
    elif fval > 1:
        val = fval * 12 - 12

    for port in [vocoderjeannotport, vocoderorlport]:
        send(port, '/x42/parameter', 6, val)
    for port in [vocoderjeannotportgars, vocoderorlportgars]:
        send(port, '/x42/parameter', 6, val - 4)
    for port in [vocoderjeannotportmeuf, vocoderorlportmeuf]:
        send(port, '/x42/parameter', 6, val  +4)

server.add_method('/x42/pitch', 'f', handler)

while True:
    server.recv(1)
