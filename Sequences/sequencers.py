from audio import *

audioseq.start_threaded()

print "Sequencers running... (ctrl+c to quit)"

while True:
    sleep(0.001)

audioseq.exit()
