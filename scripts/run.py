#!/usr/bin/python

import requests
import json
import os, sys
from operator import itemgetter

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

with open(os.path.join(dirname, 'data.json')) as f:
  data = json.load(f)

reactions = []

for i, item in enumerate(data):
  if 'reactions' in item:
    reactions.append(item['reactions'])

json.dump(reactions, open(os.path.join(dirname, 'reactions.json'), 'w'), indent=1)

# part 2

with open(os.path.join(dirname, 'reactions.json')) as f:
  reactions = json.load(f)

cleaned = []
unique = [{'text': 'hugging_face', 'value': 0}]

for i, item in enumerate(reactions):
  for j, reaction in enumerate(item):
    name = reaction['name'].split('::')[0]
    count = reaction['count']
    cleaned.append({ 'text': name, 'value': count })


for i, item in enumerate(cleaned):
  emoji = item['text']
  count = int(item['value'])

  obj = {'text':emoji, 'value': count}
  if not any(d['text'] == emoji for d in unique):
    unique.append(obj)
  else:
    for j, obj in enumerate(unique):
      if obj['text'] == emoji:
        obj['value'] += count

unique_sorted = sorted(unique, key=lambda k: k['value'], reverse=True)[0:30]

src_dirname = os.path.dirname(os.path.dirname(__file__))
json.dump(unique_sorted, open(os.path.join(src_dirname, 'src/tidied.json'), 'w'), indent=1)
