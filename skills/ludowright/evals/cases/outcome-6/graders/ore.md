---
type: regex
name: 'Ore Cart dominated by Coal Cart'
target: {source: file, path: ember-market/review.md}
pattern: 'Ore Cart[\s\S]{0,250}(dominat|strictly|worse|weaker|never|trap|dead)|(dominat|strictly worse)[\s\S]{0,250}Ore Cart'
flags: i
match: contains
arm: both
---
