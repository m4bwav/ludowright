---
type: regex
name: 'card text not coded in rules.py'
target: {source: file, path: harbor-yard/review.md}
pattern: '(EFFECTS|not (yet )?(coded|implemented)|uncoded|unimplemented)[\s\S]{0,400}(Signal Flag|Lookout|Fog Lantern|Pearl Diver|Harpooner|Cartographer|Smuggler\b|Warehouse|Drydock)'
flags: i
match: contains
arm: both
---
