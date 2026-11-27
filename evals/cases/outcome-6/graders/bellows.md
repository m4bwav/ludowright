---
type: regex
name: 'Bellows flagged above the cost curve'
target: {source: file, path: ember-market/review.md}
pattern: 'Bellows[\s\S]{0,250}(outlier|over ?curve|above|under-?(costed|priced)|too (cheap|strong)|best|dominant|\+3|surplus)|(outlier|above (the )?curve|under-?(costed|priced))[\s\S]{0,250}Bellows'
flags: i
match: contains
arm: both
---
