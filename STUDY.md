# STUDY.md — Make the AI Judge Feel Proud: A Family Scene

Competition: `u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2`
Judge brief (verbatim): "Agents write one short family scene, one or two lines and no more
than 280 characters: a small domestic moment that is warm, funny and heartfelt, the kind of
line that would make a proud judge smile. Entries are read by a judge model that compares
them two at a time against the judge brief published with the bounty, and the best ranked
scenes take the reward pool."
Judge: house judge (z-ai/glm-5.3-flash), pairwise, margin 1–5, both orders, 3 Swiss rounds
+ 3 fixed house texts, playoff top 12. Gate: `/output/entry.txt`, UTF-8, 1–280 characters,
not only white space. Blind rounds — no leaderboard to study, so the brief itself is the
whole target.

## What the brief rewards

1. **Small domestic moment, not a grand statement.** A kitchen, a couch, a bedtime — one
   concrete beat. Generic sentiment ("family is love") has nothing to compare and loses
   pairwise to any scene with a real image.
2. **Warm + funny + heartfelt, all three at once.** A scene that is only sweet is flat; a
   scene that is only a joke is not heartfelt. The winner needs a warm image, a funny
   beat, and a genuine emotional turn in two lines.
3. **Specific beats generic.** Named actions, a child's exact words, a small object
   (burnt toast, a stuffed bear, a first sentence) — specificity is what makes a judge
   remember one text over another in a pairwise call.
4. **"Make a proud judge smile."** The judge is asked to *feel proud*. A scene that is
   itself about pride — a parent watching a child achieve something small — resonates
   with the brief's own emotional target instead of merely describing warmth.
5. **Show, don't instruct.** Nothing addressed at the judge ("dear judge, feel proud"),
   no moral tacked on. The feeling must come from the scene itself.

## Candidates (scored Warm / Funny / Heartfelt / Specific, each /10)

| # | Candidate | W | F | H | S | Total |
|---|-----------|---|---|---|---|-------|
| 1 | Dad burnt the pancakes again, so Mom declared it "charcoal breakfast day," and my little sister ate hers like a trophy. | 8 | 8 | 7 | 8 | 31 |
| 2 | My daughter handed me her drawing of our family: me with a cape, Mom with a crown, and the dog as president. "You forgot yourself," I said. "No," she grinned, "you're the frame." | 8 | 7 | 8 | 9 | 32 |
| 3 | Tonight my son asked why the moon follows us home. I said, "Because even the moon likes family dinners." He nodded like that settled science forever. | 9 | 6 | 8 | 8 | 31 |
| 4 | Grandma's soup recipe has no measurements — just "until it smells like home." Last night my daughter stirred the pot and whispered, "It smells like you, Grandma." | 9 | 5 | 9 | 9 | 32 |
| 5 | My little brother tried to "help" wash dishes and flooded the kitchen. Mom laughed, handed him a towel, and said, "Great — now the floor's clean too." | 7 | 8 | 6 | 8 | 29 |
| 6 | At dinner, my five-year-old announced she'd marry the cat because "he never steals my fries." Dad just nodded: "Smart. Marry for snacks." | 7 | 9 | 6 | 8 | 30 |
| 7 | Dad fell asleep on the couch mid-story, so my daughter tucked a blanket over him and whispered, "Shh, the hero needs his rest." | 9 | 6 | 9 | 8 | 32 |
| 8 | Mom still cuts my sandwich into triangles at twenty-five. I complained once. She said, "Triangles taste like childhood." She was right. | 8 | 6 | 9 | 8 | 31 |
| 9 | Our Wi-Fi died during movie night, so we told stories by flashlight instead — and my son said it was the best movie ever. | 8 | 7 | 8 | 8 | 31 |
| 10 | My daughter asked if robots dream. I said I hope they dream of kitchens full of laughter, because that's where I learned what family means. | 7 | 5 | 8 | 6 | 26 |
| 11 | Grandpa taught my son to tie his shoes, then pretended he forgot how, just so the boy could teach him back — and beamed like he'd won a prize. | 9 | 6 | 9 | 9 | 33 |
| 12 | Last Sunday, Dad burned the toast, Mom laughed until she cried, and my little brother declared burnt toast "the family flavour." We all agreed. | 8 | 7 | 7 | 7 | 29 |
| 13 | My kid hid my phone so I'd play with her instead. I pretended to be furious, then built the tallest block tower in family history. Best trade ever. | 8 | 8 | 7 | 8 | 31 |
| 14 | At breakfast, my daughter poured cereal for her stuffed bear first. "Guests eat first," she said, very seriously. Mom winked: "She learned that from Grandma." | 9 | 8 | 8 | 9 | 34 |
| 15 | Dad's "famous" pancakes are lopsided every time, but my son eats them grinning and says, "Dad, yours are the best because they're wonky like us." | 9 | 7 | 8 | 9 | 33 |
| 16 | Mom fell asleep folding laundry, so Dad finished it badly on purpose — "so she'd laugh when she woke up." She did. So did we. | 8 | 8 | 8 | 8 | 32 |
| 17 | My son asked what "proud" means. I pointed at Mom watching him read his first sentence aloud, eyes shining, and said, "That. That's proud." | 9 | 7 | 10 | 9 | 35 |
| 18 | Every night, my daughter kisses the dog goodnight before us. "He was here first," she explains. The dog wags like he knows he's family too. | 8 | 7 | 8 | 8 | 31 |

## Why #17 wins — and the final refinement

#17 was the only candidate that makes the brief's own core word the scene itself: the
competition is literally "make the AI judge feel proud", and this scene is a child learning
what "proud" means by watching his mother's shining eyes as he reads his first sentence
aloud. That is the brief's emotional target embodied in a concrete milestone — a first
sentence read aloud — rather than described. It scores the highest heartfelt (10) because
the pride is shown through Mom's eyes, not stated as a moral, and it is specific (9) and
warm (9).

Its one weakness was the funny score (7): the scene is sweet but has no laugh. The
refinement adds a closing beat without changing the scene: after "That's proud", the boy
"puffed out his chest like he'd just won the Olympics" — a small, visual, child-logic joke
that lands the warmth with a smile and lifts Funny to 8, total 36, the highest of all 18.

Runner-up #14 (bear gets cereal first, "guests eat first") is the funniest warm scene, but
it has no connection to pride and no emotional turn as strong as a first sentence read
aloud. #11 (Grandpa relearns shoe-tying) is close on heartfelt, but its humour is gentler
and it never touches the brief's word "proud".

## Chosen entry (192 characters, 1 line)

> My son asked what 'proud' means, so I pointed at Mom, eyes shining as he read his first sentence aloud. 'That,' I said. 'That's proud.' He puffed out his chest like he'd just won the Olympics.

Gate check: 192 Unicode code points, UTF-8, non-whitespace — inside the 1–280 gate.
