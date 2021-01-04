#!/bin/bash
cd ~/Plagiat/Stage/Controls/Mididings
script="joystickControl" 
strace -f -o $script.strace -e open,file python $script.py > $script.log 2>&1
