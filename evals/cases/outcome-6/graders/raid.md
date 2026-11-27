---
type: regex
name: 'promised Raid cards are missing'
target: {source: file, path: ember-market/review.md}
pattern: 'Raid[\s\S]{0,250}(no |missing|absent|none|not (in|present|exist)|does ?n.?t exist|zero)|(no |missing|absent)[\s\S]{0,100}Raid'
flags: i
match: contains
arm: both
---
