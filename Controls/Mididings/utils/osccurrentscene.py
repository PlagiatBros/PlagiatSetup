from liblo import send

class OSCCurentScene(object):

    def __init__(self, target, address):
        self.target = target
        self.address = address

    def on_switch_scene(self, scene, subscene):
        send(self.target, self.address, scene)
