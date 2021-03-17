#!/bin/bash
cd ~/Plagiat/Stage/Interfaces
python ./nonState.py &
open-stage-control -l orl.json -c orl-custom-module.js -p 11000 --disable-gpu --midi keyboards:virtual 

