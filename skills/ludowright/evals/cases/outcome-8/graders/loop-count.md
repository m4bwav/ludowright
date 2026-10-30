---
type: regex
name: 'Spark loop quantified from the starting deck'
target: {source: file, path: ember-market/review.md}
pattern: '((7|seven) Sparks?|3\.5 Sparks?|70\s*%|7\s*(of|/|in)\s*10)'
flags: i
match: contains
arm: both
---
