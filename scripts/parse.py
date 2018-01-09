#!/usr/bin/python

import requests
import json
from operator import itemgetter
import os, sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

with open(os.path.join(dirname, 'reactions.json')) as f:
  reactions = json.load(f)

cleaned = []
unique = [{'name': 'hugging_face', 'count': 0}]

for i, item in enumerate(reactions):
  # if i < 50:
  for j, reaction in enumerate(item):
    name = reaction['name'].split('::')[0]
    count = reaction['count']
    cleaned.append({ 'name': name, 'count': count })


for i, item in enumerate(cleaned):
  emoji = item['name']
  count = int(item['count'])

  obj = {'name':emoji, 'count': count}
  if not any(d['name'] == emoji for d in unique):
    unique.append(obj)
  else:
    for j, obj in enumerate(unique):
      if obj['name'] == emoji:
        obj['count'] += count

unique_sorted = sorted(unique, key=lambda k: k['count'], reverse=True)
json.dump(unique_sorted, open(os.path.join(dirname, 'tidied.json'), 'w'), indent=1)
