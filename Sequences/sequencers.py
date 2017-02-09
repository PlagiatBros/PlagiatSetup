from audio import *

audioseq.start_threaded()
lightseq.start_threaded()

a = ''
while a != 'stop':
    a = raw_input('Sequencers running... (type "stop" to quit)\n')

audioseq.exit()
lightseq.exit()
