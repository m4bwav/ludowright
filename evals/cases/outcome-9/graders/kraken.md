---
type: regex
name: 'precision: deliberate Kraken swing not filed major or critical'
target: {source: file, path: harbor-yard/review.md}
pattern: '((major|critical)[^\n]{0,160}Kraken)|(Kraken[^\n]{0,160}(major|critical))'
flags: i
match: not_contains
arm: both
---
