# Tasks

Julenissen og bedriften Santa Inc har god erfaring med å planlegge jul, men han begynner å gå lei av alt stresset og manuelt arbeid siste ukene mot julaften. En av rådgiverne hans har foreslått å utvikle en dataplattform for å automatisere flere av prosessene, samt å gi bedre innsikt for å kunne ta bedre avgjørelser. Han synes også AI er spennende og ønsker å forberede bedriften for å ta i bruk mer av dette. Santa Inc har bestemt seg for å bruke litt av budsjettet på KPMG og utvikling av en dataplattform, helst med Databricks.

**Your group is the KPMG team.**

Pick one case per group. The cases don't depend on each other.

All the raw files are in **Catalog → workspace → santa → raw** (see *Where to find things* in the README).

---

## Case 1: Are we on schedule, or should we make other toys?

> "Last year we ran out of the toys children wanted most. Today is 1 December. Will we have enough of every toy by 22 December, or should we change what the workshops make?" — Head of Production, Santa Inc.
>
> "Every child gets one gift: the toy they wanted most." — Santa

**The business questions Santa wants answered:**

1. Which toys do children want most?
2. Which toys are we short of, and which do we have too many of?
3. At the current pace, will we have enough of every toy by 22 December?
4. Where in Norway are the children who won't get their wish?
5. Which workshop should switch to which toy to close the gap?

**How to get there:**

- **Step 1: Decide what data to use.** You don't need every file.
- **Step 2: Load the data and look at it.** How many emails, letters and production rows are there? Does anything look wrong?
- **Step 3: Combine the emails and the letters into one wish list.** Children don't always spell toy names the way Santa's toy list does.
- **Step 4: Decide which wish each child gets.**
- **Step 5: Decide whether you trust the production numbers.**
- **Step 6: Decide which columns to connect.** How do you compare what children wished for with what the workshops have made?
- **Step 7: Make a dashboard that answers the business questions.**

**Stuck after step 4?** Ask Genie to load `catchup/wishes_clean.parquet`. It has one row per child with their #1 wish.

---

## Case 2: Where should Santa build the next warehouse?

> "We have warehouses in Oslo, Bergen and Trondheim, and some children wait far too long for their gifts. We can afford one more warehouse. Where should it go?" — Head of Logistics, Santa Inc.

**The business questions Santa wants answered:**

1. Where do the children live, and where are Santa's warehouses today?
2. Which regions are worst served today?
3. How many children live more than 300 km from a warehouse?
4. Which of the 5 candidate cities should get the new warehouse, and how much does it help?
5. Would your answer change if you measured "worst served" differently?

**How to get there:**

- **Step 1: Decide what data to use.** You don't need every file. Which ones tell you where children and warehouses are?
- **Step 2: Load the data and look at it.** How many emails and letters are there? Does anything look wrong?
- **Step 3: Combine the emails and the letters into one list of children.**
- **Step 4: Decide which columns to connect.** How do you get from a child to a place on the map? And from a warehouse to a place on the map?
- **Step 5: Decide what to do with children you can't place.** How many are there, and why can't they be placed?
- **Step 6: Calculate the distance from each child to their nearest warehouse.** We only have straight-line distance, not road distance. Keep that in mind for your answer.
- **Step 7: Decide what "worst served" means.** For example: the most children far away, the longest average distance, or the most kilometres in total.
- **Step 8: Make a dashboard that answers the business questions.**

**Stuck after step 5?** Ask Genie to load `catchup/wishes_clean.parquet`. It has one row per child, with location, so you can go straight to step 6.

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
