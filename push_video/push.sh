#!/bin/bash
# ffmpeg -stream_loop -1 -re \
# -i live.mp4 \
# -c:v libx264 -pix_fmt yuv420p -profile:v baseline -preset veryfast \
# -g 50 -keyint_min 50 -sc_threshold 0 \
# -c:a aac -ar 44100 -b:a 128k \
# -f flv rtmp://192.168.8.208:1935/myapp/test

ffmpeg -stream_loop -1 -re -i live.mp4 \
  -c:v libx264 -c:a aac \
  -f flv \
  rtmp://192.168.8.208:1935/myapp/test
