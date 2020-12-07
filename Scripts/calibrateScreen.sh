#!/bin/bash

Screen=`xinput --list  |grep PixArt |cut -f1 |sed -e 's/^.*Pix/Pix/g' |head -n1`
xinput --map-to-output "$Screen" DVI-0
