---
type: regex
name: 'cost curve shown as a table with Bellows and other cards'
target: {source: file, path: ember-market/review.md}
pattern: '(^\|[^\n]*(Coal Cart|Trade Pass|Lantern|Smelter|Ore Cart|Guild Seal)[^\n]*\|[\s\S]{0,2000}^\|[^\n]*Bellows[^\n]*\|)|(^\|[^\n]*Bellows[^\n]*\|[\s\S]{0,2000}^\|[^\n]*(Coal Cart|Trade Pass|Lantern|Smelter|Ore Cart|Guild Seal)[^\n]*\|)'
flags: im
match: contains
arm: both
---
