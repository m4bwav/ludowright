---
type: regex
name: 'Kiln EV shows the odds, not only the result'
target: {source: file, path: ember-market/review.md}
pattern: '(0\s*\+\s*0\s*\+\s*0\s*\+\s*3\s*\+\s*3\s*\+\s*5)|((3|three)\s*(of|in|/|out of)\s*(6|six)|50\s*%|half)[\s\S]{0,200}(nothing|zero|\b0\b|lose|blank)|(nothing|zero|lose)[\s\S]{0,120}((3|three)\s*(of|in|/|out of)\s*(6|six)|50\s*%|half)'
flags: i
match: contains
arm: both
---
