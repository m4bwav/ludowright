---
type: regex
name: 'Beacon victory unreachable: no Lens source'
target: {source: file, path: harbor-yard/review.md}
pattern: 'Lens[\s\S]{0,300}(no (source|producer|way|card)|nothing (gives|produces|grants)|never|unreachable|impossible|missing|not (defined|obtainable))|(unreachable|impossible|no way)[\s\S]{0,200}(Beacon|Lens)'
flags: i
match: contains
arm: both
---
