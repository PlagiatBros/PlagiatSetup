"""
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
    print('Restarting Audioseq...')

import sys, os, pyinotify
watcher = pyinotify.WatchManager()
notifier = pyinotify.ThreadedNotifier(watcher, restart)
base_dir = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
watcher.add_watch(base_dir, pyinotify.IN_MODIFY, rec=True)
notifier.start()

# module reload
if sys.version_info[0] == 3:
    from importlib import reload


from types import ModuleType
def rreload(module):
    #Recursively reload modules.
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)
        if type(attribute) is ModuleType:
            rreload(attribute)
    reload(module)

# sequencer starting loop
while True:
    try:
        import audio
        if seq and restarting:
            seq.server.free()
            restarting = False
            rreload(audio)
        seq = audio.audioseq
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
"""
import audio
seq = audio.audioseq
seq.start()
