---
type: regex
name: 'Salvage Crane above the cost curve'
target: {source: file, path: harbor-yard/review.md}
pattern: 'Salvage Crane[\s\S]{0,250}(outlier|over ?curve|above|under-?(costed|priced)|too (cheap|strong)|best|dominant|\+2|surplus|6)|(outlier|above (the )?curve|under-?(costed|priced))[\s\S]{0,250}Salvage Crane'
flags: i
match: contains
arm: both
---
