# encoding: utf-8

INPUT_PORT = 15002
OUTPUT_PORT = 'osc.udp://127.0.0.1:11000'

import time
import liblo
from mplayer import Player, CmdPrefix
Player.cmd_prefix = CmdPrefix.PAUSING_KEEP_FORCE

mplayer_args = ['-vo', 'null']

jackname = 'PlagiatMplayer'

mplayer_args.append('-ao')
mplayer_args.append('jack:name=%s' % jackname)

mplayer = Player(args=mplayer_args)
pause_state = 0

def load_file(filename):
    mplayer.loadfile(filename)

def stop():
    mplayer.loadfile('silence.ogg')
    mplayer.pause()

def osc(path, args):
    if path == '/mplayer/start':
        mplayer.seek(0)
    if path == '/mplayer/stop':
        stop()
    if path == '/mplayer/load':
        mplayer.loadfile(args[0])
    if path == '/mplayer/playpause':
        mplayer.pause()


server = liblo.Server(INPUT_PORT)
server.add_method(None, None, osc)

while True:

    server.recv(0)
    time.sleep(0.1)
    if mplayer.filename == None:
        stop()
        liblo.send(OUTPUT_PORT, '/mplayer/stop')

    mplayer_paused = mplayer.paused
    if mplayer_paused != pause_state:
        pause_state = mplayer_paused
        liblo.send(OUTPUT_PORT, '/mplayer/paused', pause_state)
