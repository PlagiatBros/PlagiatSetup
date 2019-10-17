# globals
seq = None
restarting = False
state = {}

# watcher
def restart(event=None):
    global seq, restarting, state
    if not seq:
        return
    restarting = True
    state = {'bpm': seq.bpm, 'playing': seq.playing, 'cursor': seq.cursor}
    seq.exit()
    print('Restarting Lightseq...')

import sys, os, pyinotify
watcher = pyinotify.WatchManager()
notifier = pyinotify.ThreadedNotifier(watcher, restart)
base_dir = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
watcher.add_watch(base_dir, pyinotify.IN_MODIFY, rec=True)
notifier.start()


# module reload
if sys.version_info[0] == 3:
    from importlib import reload


# sequencer starting loop
while True:
    try:
        import light
        if seq and restarting:
            seq.server.free()
            restarting = False
            reload(light)
        seq = light.lightseq
        if state:
            seq.bpm = state['bpm']
            seq.playing = state['playing']
            seq.cursor = state['cursor']
        seq.start()
        if not restarting:
            break
    except Exception as e:
        notifier.stop()
        raise e


# exit
notifier.stop()
