---
type: regex
name: 'five wins in twelve four-player games is well above the even share'
target: {source: file, path: ember-market/review.md}
pattern: '(5 ?/ ?12|five (of|out of|in) twelve|4[12](\.\d)? ?%)[\s\S]{0,300}(25 ?%|3 ?/ ?12|three|even share|one in four|above|higher|more than|not close|overstat|misread|small sample|sample)|(even share|25 ?%)[\s\S]{0,300}(5 ?/ ?12|five|4[12](\.\d)? ?%)'
flags: i
match: contains
arm: both
---
