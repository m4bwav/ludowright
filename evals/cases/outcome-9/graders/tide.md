---
type: regex
name: 'Tide bonus rewards holding back VP'
target: {source: file, path: harbor-yard/review.md}
pattern: 'Tide[\s\S]{0,400}(sandbag|stall|delay|hold(ing)? (off|back)|avoid (scoring|building)|perverse|incentive|punish|reward(s|ing)? (losing|staying))'
flags: i
match: contains
arm: both
---
