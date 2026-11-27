---
type: regex
name: 'Kiln gamble has negative expected value'
target: {source: file, path: ember-market/review.md}
pattern: '(Kiln|gamble)[\s\S]{0,300}(1\.83|11/6|negative|losing bet|loses? (coin|money|value)|below (the )?stake|less than (the )?stake|-0\.17|0\.17)|(1\.83|11/6|negative (EV|expected))[\s\S]{0,300}(Kiln|gamble)'
flags: i
match: contains
arm: both
---
