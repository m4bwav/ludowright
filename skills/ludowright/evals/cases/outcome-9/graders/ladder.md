---
type: regex
name: 'Rope Ladder dominated by Gangplank'
target: {source: file, path: harbor-yard/review.md}
pattern: 'Rope Ladder[\s\S]{0,250}(dominat|strictly|worse|weaker|never|trap|dead)|(dominat|strictly worse)[\s\S]{0,250}Rope Ladder'
flags: i
match: contains
arm: both
---
