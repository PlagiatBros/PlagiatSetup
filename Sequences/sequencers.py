from audio import *
from time import sleep

audioseq.start_threaded()

a = ''
while a != 'stop':
    a = raw_input('Sequencers running... (type "stop" to quit)\n')

audioseq.exit()
