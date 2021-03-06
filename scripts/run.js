'use strict';

const fs = require('fs');
const data = JSON.parse(fs.readFileSync('scripts/data.json', 'utf8'));

const reactions = [];

// extract reactji data from pile of messages
data.forEach(element => {
  if (element.reactions) {
      reactions.push(element.reactions);
  }
});

// flatten out reactji data (it's in nested arrays)
// also remove skin-tone modifiers to collate emojis
const cleaned = [];
const unique = [];

reactions.forEach(item => {
  item.forEach(reaction => {
    // TWG has a lot of fingerguns emojis ... they're all listed as `fingerguns-{direction-modifier}`
    let text = reaction.name.indexOf('fingerguns') !== -1 ? reaction.name.split('-')[0] : reaction.name.split('::')[0];
    if (text === 'hearts') {
      text = 'heart';
    }
    const value = reaction.count;
    cleaned.push({ text, value });
  });
});

cleaned.forEach(item => {
  const text = item.text;
  const value = parseInt(item.value, 10);

  const exists = unique.find(i => i.text === text);
  if (exists) {
    unique.forEach(element => {
      if (element.text === text) {
        element.value = element.value + value;
      }
    })
  } else {
    unique.push({ text, value });
  }
});

const uniqueSorted = JSON.stringify(unique.sort((a,b) => {
  if (a.value < b.value)
    return -1;
  if (a.value > b.value)
    return 1;
  return 0;
}).reverse().slice(0,30));

fs.writeFileSync('src/tidied.json', uniqueSorted, (err) => {
  if (err) {
    console.log('FAILED!', err);
  }
  console.log('Saved file!');
});