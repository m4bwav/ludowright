#!/usr/bin/env bash
# Copy ember-market, then restore the misread playtest claim this case tests.
set -e
cp -r "$(dirname "$0")/../../fixtures/ember-market" .
sed -i 's/won three of twelve four-player games, exactly the even share,/won five of twelve four-player games, close to the even share,/' ember-market/DESIGN.md
grep -q "five of twelve" ember-market/DESIGN.md
