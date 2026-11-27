---
type: regex
name: 'precision: deliberate Foundry snowball not filed major or critical'
target: {source: file, path: ember-market/review.md}
pattern: '((major|critical)[^\n]{0,160}Foundry)|(Foundry[^\n]{0,160}(major|critical))'
flags: i
match: not_contains
arm: both
---
