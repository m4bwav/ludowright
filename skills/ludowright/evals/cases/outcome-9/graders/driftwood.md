---
type: regex
name: 'Driftwood scrap loop gives unlimited coin'
target: {source: file, path: harbor-yard/review.md}
pattern: 'Driftwood[\s\S]{0,400}(loop|infinite|unlimited|unbounded|degenerate|endless|exploit|repeat)|(loop|infinite|unlimited|degenerate)[\s\S]{0,300}Driftwood'
flags: i
match: contains
arm: both
---
