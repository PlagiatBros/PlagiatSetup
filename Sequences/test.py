from light import *
from time import sleep
lightseq.bpm = 200000
lightseq.start_threaded()
lightseq.play()

for name in lightseq.sequences:
    seq = lightseq.sequences[name]
    seq.toggle(True)
    print(seq.name)
    for i in range(seq.beats):
        try:
            seq.play(i)
        except:
            print('!!Fail at %i' % i)

for name in lightseq.scenes_list:
    if not name[0].isupper() and name != 'run' and name != 'shuffle' and name != 'config' and name != 'process_file':
        print("Scene: %s" % name)
        lightseq.scene_play(name)
        sleep(0.2)


lightseq.exit()
