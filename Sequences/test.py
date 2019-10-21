import sys
from light import *
from time import sleep, time
lightseq.bpm = 200
lightseq.start_threaded()
lightseq.play()


from subprocess import check_output
sequences = check_output("./print_sequences.sh").split('\n')
scenes = check_output("./print_scenes.sh").split('\n')

def exit():
    lightseq.exit()
    sys.exit()

print('TESTING SEQUENCES')
print('#################\n')
for name in sequences:
    try:
        seq = lightseq.sequences[name]
    except:
        print('%s: NOT FOUND' % name)
        continue
    seq.toggle(True)

    for i in range(seq.beats):
        try:
            seq.play(i)
        except Exception as e:
            print(e)
            print('%s: ERROR in step %i' % (name, i))
            exit()
    sleep(0.01)
    print('%s: OK' % name)


print('TESTING SCENES')
print('#################\n')
for name in scenes:
    lightseq.scene_play(name)
    print('Playing scene %s...' % name)
    sleep(0.5)
    lightseq.disable_all()
