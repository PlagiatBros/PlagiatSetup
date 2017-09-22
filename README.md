# PlagiatSetup

The Plagiat Brothers' audio/video/light live setup

## Requirements

- apps
    - gladish
    - non-mixer (with lv2 support
    - seq24-plagiat
    - tapeutape
    - guitarix
    - sooperlooper
    - zynaddsubfx
    - x42 fat1.lv2 (patched)
    - zita-at1-plagiat
    - python 2.7
    - mididings
    - klick
    - qlc+
    - open-stage-control >= 0.20.3
    - alsa-tools-gui (rme soundcard)
- plugins
    - swh-plugins (Steve Harris LADSPA plugins)
    - caps (the C* Audio Plugin Suite)
    - mda-lv2 (Paul Kellett's MDA plugins ported to LV2)
    - cmt (Computer Music Toolkit, ladspa)
    - calf-plugins
    - infamousPlugins



## Setup

Many paths are hardcoded, the simplest way to get the system running is to create a fake user folder to replicate the original file tree.

```
$ git clone https://github.com/PlagiatBros/PlagiatSetup
$ git submodule init && git submodule update
$ sudo mkdir /home/woii
$ sudo mkdir /home/woii/Plagiat
$ sudo ln -s /full/path/to/PlagiatSetup /home/woii/Plagiat/Stage
$ cp PlagiatSetup/Ladish/Plagiat_2016.xml ~/.ladish/studios/
```
