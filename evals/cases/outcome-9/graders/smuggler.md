---
type: regex
name: 'Smugglers Run is a losing bet'
target: {source: file, path: harbor-yard/review.md}
pattern: '(Smuggler.?s Run|gamble|bet)[\s\S]{0,300}(negative|losing|loses?|EV of 2|returns? 2|2 coin|-1|below (the )?stake|less than (the )?stake|1/3)'
flags: i
match: contains
arm: both
---
