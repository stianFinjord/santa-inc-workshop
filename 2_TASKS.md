# Tasks

Pick one case per group. Cases 1 and 2 both start with **Step 0**. Case 3 starts straight away.

All the raw files are in **Catalog → workspace → santa → raw** (see *Where to find things* in the README).

---

## Step 0 (cases 1 and 2): one wish list

Children sent their wishes in two ways: by email, and by paper letter that the elves scanned. Before you can answer anything, you need **one clean wish list**.

**Files:** all files in the `wishes/email` folder, `wishes/letters/scanned_letters.csv`, `toys.parquet`, `postcodes.csv`

1. Find the files in **Catalog → workspace → santa → raw → wishes**. Ask Genie to load the emails and the letters into two raw tables, and look at a few rows of each.
2. An email can hold several wishes. Turn it into one row per wish.
3. Make the two tables look the same: same column names, same date format.
4. Match the toy names children wrote to the official toy list. Children don't spell well.
5. Stack the two tables into one, with a column saying where each wish came from.
6. Some children sent both an email and a letter. Santa gives each child **one** gift: their #1 wish. Keep one row per child.
7. The emails contain personal ID numbers. Should they be in your final table?

Stuck after 40 minutes? Ask Genie to load `catchup/wishes_clean.parquet` and move on to your case.

---

## Case 1: Are we on schedule, or should we make other toys?

> "Last year we ran out of the toys children wanted most. Today is 1 December. Will we have enough of every toy by 22 December, or should we change what the workshops make?" — Head of Production, Santa Inc.

**Files:** your wish list from step 0, all files in the `production` folder, `workshops.csv`, `toys.parquet`

1. Load and clean the production data. Is every row really one day, one workshop, one toy?
2. Count #1 wishes per toy, and toys made so far per toy.
3. Compare them: which toys are short, and which do we have too many of?
4. Dashboard: shortage per toy, and a map of where the unfulfilled wishes are.
5. Pitch: is Santa on schedule? What should change?

**Going further**

- At the current production rate, which toys will still be short on 22 December?
- Each toy takes a set number of minutes to make. Which workshop should switch to which toy to close the gap?

---

## Case 2: Where should Santa build the next warehouse?

> "We have warehouses in Oslo, Bergen and Trondheim, and some children wait far too long for their gifts. We can afford one more warehouse. Where should it go?" — Head of Logistics, Santa Inc.

**Files:** your wish list from step 0, `warehouses.csv`, `candidate_cities.csv`, `postcodes.csv`

1. Give every wish a location by joining it to the postcode list. Do all postcodes match?
2. Put the #1 wishes and the three warehouses on one map.
3. For each region, count wishes and find how far away the nearest warehouse is.
4. Dashboard: map of wishes and warehouses, and a ranking of the regions that are worst served.
5. Pitch: where should the new warehouse go, and why?

**Going further**

- Calculate each child's distance to their nearest warehouse, and add it up per region.
- Test the 5 candidate cities: which one cuts the total distance the most?

---

## Case 3: Are our elves staffed right for the Christmas peak?

> "Some workshops have high sick leave and huge overtime bills. One workshop spends Fridays on teambuilding and seems to make fewer toys. Should we cut costs, hire more, or use more consultant elves?" — Head of People, Santa Inc.

**Files:** `elves.csv` (HR system), all files in the `shifts` folder (time clock), `workshops.csv`, `pay_rates.csv`, `satisfaction_survey.csv`

1. Load the HR file and the time clock files. Do the elf IDs and workshop names match between them?
2. Clean the shifts: status values, missing hours, missing toy counts. What does a missing value actually mean here?
3. Per workshop: number of elves, sick leave %, overtime hours, toys per hour worked.
4. Add pay rates and calculate the cost per toy for each workshop.
5. Dashboard: map of the workshops plus the key numbers side by side.
6. Pitch: what should Santa do about staffing before Christmas?

**Going further**

- Compare the cost of overtime, consultant elves and permanent hires, month by month. When does each make sense?
- Does satisfaction relate to sick leave or output? Show the survey in a way that never exposes a single elf.

---

## Before you pitch

Be ready to answer three questions about your work:

1. **Which files did you use**, and which did you leave out?
2. **How did you clean the data**, and why?
3. **What did you do with personal data?**
