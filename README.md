# PlagiatSetup

The Plagiat Brothers' audio/video/light live setup:

23 x mixers & plugin hosts (non mixer)
2 x synthesizer (zynaddsubfx)
1 x main midi/osc routing patches (mididings)
5 x secondary midi/osc routing patches (mididings)
1 x loopstation (sooperlooper)
1 x midi sequencer (seq24)
3 x osc sequencers (seqzero)
1 x sampler (Tapeutape)
1 x klick
8 x autotuners (zita-at1 / x42-fat1)
1 x calf jack host
1 x osc control surface (open stage control)
1 x qlc+

![jack patch](https://user-images.githubusercontent.com/5261671/52136607-b3f21b80-2648-11e9-9cd9-c8dd62a4f180.png)

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
    - open-stage-control
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
