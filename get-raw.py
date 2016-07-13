#!/usr/bin/env python3


import json
import os
from   pprint import pprint
import shutil
import sys
import time
import urllib.request


def get_stickers(json_filename, destination_set):
  with open(json_filename) as json_file:
    data = json.load(json_file)

    # Query Number (based on # requests?)
    query_key = list(data)[0]

    # GraphQL ID for sticker set (typename: StickerPack)
    stickerset_id = list(data[query_key]['response'])[0]

    # Lets get sticker list key
    for key in list(data[query_key]['response'][stickerset_id]):
      if key.startswith('_stickers'):
        stickers_key = key

    # Finally, array of stickers
    stickers = data[query_key]['response'][stickerset_id][stickers_key]['edges']

    for sticker in stickers:
      sticker = sticker['node']

      for key in list(sticker):
        if key.startswith('_image'):
          grab_sticker(sticker, key, destination_set, 'single')
        elif key.startswith('_sprite'):
          grab_sticker(sticker, key, destination_set, 'sprite')
        elif key.startswith('_padded'):
          grab_sticker(sticker, key, destination_set, 'padded_sprite')


def grab_sticker(sticker, key, destination_set, image_type):
  sticker_id = sticker['id']
  frame_count = sticker['frame_count']
  frame_rate = sticker['frame_rate']
  columns = sticker['frames_per_column']
  rows = sticker['frames_per_row']

  base_filename = '%s-%sx%s-%sx%s' % (sticker_id, frame_count, frame_rate, columns, rows)

  print(base_filename)

  dest = 'raw/%s/%s-%s.png' % (destination_set, base_filename, image_type)

  # Only if the file doesn't already exist
  if os.path.isfile(dest):
    print('Already exists! Skipping!')

  # Download
  else:
    parts = sticker[key]['uri'].split('/')
    # get rid of the size part
    del(parts[-2])
    url = '/'.join(parts)
    print('Downloading... %s' % url)
    with urllib.request.urlopen(url) as response, open(dest, 'wb') as out_file:
      shutil.copyfileobj(response, out_file)
    print('OK')
    time.sleep(1)


if __name__ == '__main__':
  get_stickers('graphql-pusheen.json', 'pusheen')
  get_stickers('graphql-pusheen-eats.json', 'pusheen-eats')
