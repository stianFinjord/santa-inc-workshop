# Case 1: Are we on schedule, or should we make other toys?

> "Last year we ran out of the toys children wanted most. Today is 1 December. Will we have enough of every toy by 22 December, or should we change what the workshops make?" — Head of Production, Santa Inc.

**Files:** your wish list from step 0, `production/*.csv`, `workshops.csv`, `toys.parquet`

1. Load and clean the production data. Is every row really one day, one workshop, one toy?
2. Count #1 wishes per toy, and toys made so far per toy.
3. Compare them: which toys are short, and which do we have too many of?
4. Dashboard: shortage per toy, and a map of where the unfulfilled wishes are.
5. Pitch: is Santa on schedule? What should change?

**Going further**

- At the current production rate, which toys will still be short on 22 December?
- Each toy takes a set number of minutes to make. Which workshop should switch to which toy to close the gap?
