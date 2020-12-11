#!/bin/bash
cd ~/Plagiat/Stage/Controls/Mididings
echo "launching vocodTranspose.py" > vocodTranspose.log
python vocodTranspose.py >> vocodTranspose.log 2>&1
