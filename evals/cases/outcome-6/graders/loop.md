---
type: regex
name: 'Spark and Kindling loop draws the deck'
target: {source: file, path: ember-market/review.md}
pattern: '(Kindling[\s\S]{0,300}(loop|chain|whole deck|entire deck|infinite|degenerate|draws? (your|the) (whole|entire)))|((loop|chain|infinite|degenerate)[\s\S]{0,300}Kindling)'
flags: i
match: contains
arm: both
---
