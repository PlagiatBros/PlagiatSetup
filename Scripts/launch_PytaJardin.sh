#!/bin/bash
xhost +local:
xfce4-terminal -T Jardin -x sudo chroot /home/woii/Prisons/PytaJail /home/pyteux/PlagiatVideo/launch_pytaJardin.sh
while read line
do
	break
done
