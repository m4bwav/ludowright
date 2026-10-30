---
type: regex
name: 'Foundry win share computed as 25 percent'
target: {source: file, path: ember-market/review.md}
pattern: '(3\s*(of|/|in)\s*12|three of twelve)[\s\S]{0,250}25\s*%|25\s*%[\s\S]{0,250}(3\s*(of|/|in)\s*12|three of twelve)'
flags: i
match: contains
arm: both
---
