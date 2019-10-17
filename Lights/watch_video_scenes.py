import liblo

# watcher
def reload(event=None):
    liblo.send('osc.udp://127.0.0.1:5555', '/pyta/scene_import', '../Scenes/*/*.video')
    liblo.send('osc.udp://127.0.0.1:5556', '/pyta/scene_import', '../Scenes/*/*.video')

reload()

import sys, os, pyinotify
watcher = pyinotify.WatchManager()
notifier = pyinotify.Notifier(watcher, reload)
base_dir = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
watcher.add_watch('./Scenes', pyinotify.IN_MODIFY | pyinotify.IN_CREATE, rec=True)
print('Monitoring video scene files... (press ctrl+x to exit)')
notifier.loop()
