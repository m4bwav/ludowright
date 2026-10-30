# Balance: answer a numbers question by counting

Load [../kb/balance-and-economy.md](../kb/balance-and-economy.md) for the principles and [../kb/balance-tables.md](../kb/balance-tables.md) for the table shapes.

## Steps

1. **Turn the question into a measurement.** "Is this card overpowered" is a cost-curve question within its family; "does gold pile up" is an economy question; "how long until X" is a walk simulation; "is this drop fair" is an EV and spread question. Say which in one line.
2. **Declare the table from the game's real data,** never from memory: read the card list, unit stats or economy rules and copy the numbers into the table shape. Note the file each number came from. Name the player policy the table assumes.
3. **Run** `LDW ev|curve|economy|sim <table>` (seeded sims: keep the default seed, or state the seed used). Save the table as `ldw-<topic>.json` beside the answer.
4. **Read the result as a designer.** A curve outlier is a question (is the cost wrong, or does the item carry a benefit the columns miss?). A leak matters only if the resource is meant to stay scarce. A long tail in a sim matters if the p05 or p95 player has a bad time. Check the answer against a second policy when the first one is an assumption.
5. **Answer** in a few lines: the number, what it means for players, the change you would make and by how much, and what the counting cannot see (interaction, skill, metagame). When the question was about an existing game, add the result as a finding (`category: balance`, `dominant-strategy` or `economy-leak`) in that game's findings file.
