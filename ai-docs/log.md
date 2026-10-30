# Log

## [2026-10-29] start | name, inventory, research, ldw.py
Name check, book inventory (Lemarchand found; Carillo, Gupta, Baldwin, Steele, Game AI Pro 1/2/4 missing), two research notes, ldw.py with 13 tests. Readers launched.

## [2026-10-29] reading | balance books done
Romero and Schreiber, Adams and Dormans, Clark notes written. Gaps: Game Balance ch. 7 (trading), ch. 14 (matchmaking), the spreadsheet chapters and the analysing-existing-games pages; Adams and Dormans ch. 9-12. Reader note for readwright: in big PDFs rw.py section numbers drift from the printed chapters and neighbouring sections repeat text, so cite chapters, not section numbers.

## [2026-10-29] reading | Swink and Gibson Bond done (partial)
Swink: principles and metrics read; case-study chapters 12-16 (Asteroids, Mario, Bionic Commando, Mario 64, Raptor Safari) only from the toc, so the game-juice PR still needs a read of them for the measured cases. Gibson Bond Part I read in the main; the probability maths in ch. 11 and the group-testing half of ch. 10 only from the toc.

## [2026-10-29] reading | Schell, Koster, Sylvester done (partial)
Schell: about 70 of the 112 lenses (questions only), ch. 13 balance, ch. 14 puzzles, ch. 16 interest curves opening, ch. 27 playtesting. Koster: read by per-page excerpts, not word for word; ch. 7 list cut off and not recorded. Sylvester: ch. 2, 3, 5, 6, 11, 13 and emergent story; ch. 7 (game theory, yomi) and ch. 8 (reinforcement schedules) worth a second pass for uncertainty and ai-npc.

## [2026-10-29] reading | Fullerton, Salen and Zimmerman, Elias et al. done (partial)
About 25-30k words read per book. Fullerton: ch. 5, 9, 10, 11 in large part; dilemmas, accessibility and AI-in-the-creative-process seen as headings only. Salen and Zimmerman: meaningful play, choice, rules, emergence, uncertainty, information, feedback, conflict, rule-breaking; Units 3-4 unread. Elias et al.: cited by epub section (s4.2), no page numbers.

## [2026-10-29] reading | game AI technique books done (partial)
Millington (ch. 2, parts of 5-7 and 11, most of ch. 14), Buckland, Bourg and Seemann, Game AI Pro 3 (ch. 1, 4, 33 in full; 13, 31, 32 partial), Aversa (pointers to unity-agent). Highest value: Millington ch. 14, Game AI Pro 3 ch. 4 and 33. Small-sample caveats flagged in the notes.

## [2026-10-29] reading | production books done
Lemarchand (most of the production chapters), Hackett (full), Schreier (sampled, about a third to half per chapter: check case details against the book before quoting), Wyman (thin: PDF text is one long line per section), Nystrom (design-relevant patterns only). Parallel readers overwrote each other in the shared scratchpad; next time give each reader its own scratch subfolder in the brief.

## [2026-10-29] reading | Sellers, Costikyan, Hodent done (partial)
Sellers ch. 4-10 and 12 in part (analytical balance and telemetry unread). Costikyan ch. 3, 5 (all eleven uncertainty sources), 6. Hodent application sections of ch. 3-8, usability heuristics and pillars, onboarding plan; dark patterns and AI sections half read.

## [2026-10-29] reading | level design and procgen books done; all nine groups in
Totten, Bauer, Short and Adams, Shaker-Togelius-Nelson written, each compared with the Level Up! distillation. 27 notes files in books/plugin-learnings/round3-game-design/. Next: step 4 synthesis into kb/.

## [2026-10-29] review | first real-game run: SpaceDeckBuilder2 (read-only)
Review (13 findings, validate OK) and improve list (10) in ai-docs/reviews/ (gitignored), with ldw-xp-sim, ldw-deck-growth, ldw-energy and ldw-buildings-curve tables. Top: Shuttle win unreachable (no Fuel Cell / Spacecraft Component producer), Launchpad-then-wait wins at turn 30, 70 of 82 reward cards uncoded. Skill gaps seen: no step for "doc and code disagree on the clock", rubric lacks an "implemented vs authored" check, curve needs multi-resource costs declared by hand, economy has no fractional/policy guidance, improve.md ids get renumbered by the md sort.

## [2026-10-29] evals | salt-road fixture, outcome A/B, tidy
Harder fixture salt-road plus outcome-3/-4; outcome cases seeded by case.yaml scaffolds. plugin eval on Windows: no shell grant possible, so the skill arm hand-counts and loses on last-message grading (T-20261029-2, L-20261029-1, about $17 of eval runs). skill-tidy: description cut under 1024 chars; ST021 nested kb links kept by design. Repo m4bwav/ludowright still absent; evergreen-protocol#34 open, no comments.

## [2026-10-29] release | public repo, v0.1.0, wiki; review reaction routed
Mark OK'd the public repo and objected to no review finding (unbuilt items are just not built yet). Created m4bwav/ludowright, PR #1 (banner, CI: no Python 3.9 on Ubuntu 26.04) and PR #2 (contract 1.1 `stage`/`built`, rubric R-53, L-20261029-2, package.py) merged, v0.1.0 released with the zip, wiki pushed after a browser click created it, social preview uploaded, installed from mark-local. Bash heredocs with apostrophes broke again; wiki pages written with Write.
