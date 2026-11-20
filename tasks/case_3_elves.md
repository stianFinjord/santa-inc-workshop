# Case 3: Are our elves staffed right for the Christmas peak?

> "Some workshops have high sick leave and huge overtime bills. One workshop spends Fridays on teambuilding and seems to make fewer toys. Should we cut costs, hire more, or use more consultant elves?" — Head of People, Santa Inc.

**Files:** `elves.csv` (HR system), `shifts/*.json` (time clock), `workshops.csv`, `pay_rates.csv`, `satisfaction_survey.csv`

1. Load the HR file and the time clock files. Do the elf IDs and workshop names match between them?
2. Clean the shifts: status values, missing hours, missing toy counts. What does a missing value actually mean here?
3. Per workshop: number of elves, sick leave %, overtime hours, toys per hour worked.
4. Add pay rates and calculate the cost per toy for each workshop.
5. Dashboard: map of the workshops plus the key numbers side by side.
6. Pitch: what should Santa do about staffing before Christmas?

**Going further**

- Compare the cost of overtime, consultant elves and permanent hires, month by month. When does each make sense?
- Does satisfaction relate to sick leave or output? Show the survey in a way that never exposes a single elf.
