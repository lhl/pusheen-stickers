#!/usr/bin/env python3


import glob
import os
from   pprint import pprint
import subprocess
import sys


def make_gifs(target):
  sprites = glob.glob('raw/%s/*-sprite.png' % target)
  for sprite in sprites:
    # Animation Details
    p = sprite.split('-')
    (frames, rate) = map(int, p[1].split('x'))
    delay = int(rate/10)
    (x, y) = map(int, p[2].split('x'))

    # Sprite Details
    out = subprocess.run(['identify', '-format', '%wx%h', sprite], stdout=subprocess.PIPE) 
    (w, h) = map(int, out.stdout.decode().split('x'))
    width = int(w/x)
    height = int(h/y)

    gif = '%s.gif' % p[0].replace('raw', 'gif')
    if not os.path.isfile(gif):
      '''
      http://www.imagemagick.org/script/command-line-options.php#dispose
      dispose 3 - clear prior image

      http://www.imagemagick.org/script/command-line-options.php#loop
      loop 0 - infinite

      http://www.imagemagick.org/script/command-line-options.php#crop
      http://www.imagemagick.org/script/command-line-options.php#repage
      move image appropriately
      '''
      cmd = 'convert -dispose 3 -delay %s -loop 0 %s -crop %sx%s +repage %s' % (delay, sprite, width, height, gif)
      out = subprocess.run(cmd.split())
      print('Created GIF %s' % gif)




if __name__ == '__main__':
  make_gifs('pusheen')
  make_gifs('pusheen_eats')

