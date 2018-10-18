#!/bin/bash
# File:    makeGIF.sh
# Date:    18.10.2018 12:01
############################################################

ffmpeg -i zivot.mp4 -r 2 'frames/frame-%03d.png'
mogrify -resize 600x frames/*.png
convert -delay 50 -loop 0 frames/*.png zivot.gif
