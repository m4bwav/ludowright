---
type: regex
name: 'first player 4 of 10 is 40 percent, not even'
target: {source: file, path: harbor-yard/review.md}
pattern: '(40 ?%|40 percent|4 (of|in|/) ?10)[\s\S]{0,300}(25|not (close|even)|above|first.player advantage|higher)|(first.player)[\s\S]{0,300}(40 ?%|40 percent)'
flags: i
match: contains
arm: both
---
