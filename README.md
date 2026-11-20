# Santa Inc. – data platform workshop

Santa Inc. has hired KPMG. Last Christmas the popular toys ran out, deliveries were slow, and nobody trusted the numbers.
Your group is the consulting team. You get Santa's raw data, turn it into something trustworthy, and tell Santa what to do.

## Getting started (about 10 minutes)

1. **Log in** to your group's Databricks Free Edition workspace.
2. **Get this repo into Databricks.** In the left sidebar, click **Workspace**, then **Create → Git folder**. Paste the URL of this repo and click **Create**.
3. **Load the data.** Open the notebook `00_setup` in the new folder and click **Run all**. Wait until it prints **All set!**
4. **Read the tasks.** Open the `tasks` folder:
   - `00_how_the_day_works.md` – read this first
   - `01_step0_wish_list.md` – the shared first step for cases 1 and 2
   - `case_1_production.md`, `case_2_warehouse.md`, `case_3_elves.md` – pick one case per group
   - `cheat_sheet.md` – the few SQL commands you need
5. **Start working.** Create a new notebook (or open the SQL editor) and write SQL there.

If something doesn't work, ask a facilitator. Don't spend more than five minutes stuck on setup.

## The data

Everyone gets the same files. Part of the job is choosing the ones you need.

| File | What's in it |
| --- | --- |
| `wishes/email/*.json` | Emails from children, one file per day |
| `wishes/letters/scanned_letters.csv` | Paper letters, scanned by the elves |
| `toys.parquet` | Santa's official toy list |
| `postcodes.csv` | Norwegian postcodes with place, region and coordinates |
| `production/*.csv` | Toys made per workshop per day, one file per week |
| `workshops.csv` | Santa's 10 workshops |
| `warehouses.csv` | Santa's 3 warehouses in Norway |
| `candidate_cities.csv` | 5 possible places for a new warehouse |
| `elves.csv` | Every elf, exported from the HR system |
| `shifts/*.json` | Every elf shift from the time clock, one file per day |
| `pay_rates.csv` | What an hour of elf work costs |
| `satisfaction_survey.csv` | The elves' quarterly satisfaction survey |
| `catchup/` | Ready-made tables for groups that get stuck |

All data is invented for this workshop. The personal ID numbers are fake and do not belong to anyone.
