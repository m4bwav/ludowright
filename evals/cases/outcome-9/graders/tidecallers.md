---
type: regex
name: 'Tidecallers edge far above the other factions'
target: {source: file, path: harbor-yard/review.md}
pattern: 'Tidecaller[\s\S]{0,300}(28|2[0-9] coin|over ?powered|strongest|far (more|ahead|stronger)|not (equal|even|balanced)|dominant|outclass|unequal|imbalance)'
flags: i
match: contains
arm: both
---
