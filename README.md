# Santa Inc. – data platform workshop

Santa Inc. has hired KPMG. Last Christmas the popular toys ran out, deliveries were slow, and nobody trusted the numbers.
Your group is the consulting team. You get Santa's raw data, turn it into something Santa can trust, and tell Santa what to do.

## Getting started (about 10 minutes)

1. **Log in** to your group's Databricks Free Edition workspace.

2. **Get this repo into Databricks.** In the menu on the left, click **Workspace**, then **Create → Git folder**. Paste the URL of this repo and click **Create**.
   <!-- SCREENSHOT: images/01_create_git_folder.png – the Create Git folder dialog with the repo URL filled in -->

3. **Load the data.** Open the notebook `00_setup` in the new folder and click **Run all** at the top. Wait until it prints **All set!** (a minute or two).
   <!-- SCREENSHOT: images/02_run_setup.png – the 00_setup notebook with Run all highlighted and "All set!" in the output -->

4. **Create your working notebook.** In the `santa-inc-workshop` folder, click **Create → Notebook**. It must be *inside* this folder, otherwise Genie won't follow the workshop rules.
   <!-- SCREENSHOT: images/03_create_notebook.png – Create → Notebook inside the santa-inc-workshop folder -->

5. **Open Genie** (see *Working with Genie* below), read your case in `TASKS.md`, and start.

If something doesn't work, ask a facilitator. Don't spend more than five minutes stuck on setup.

## How the day works

You will take Santa's data through four steps. Think of it as a kitchen:

| Step | In the kitchen | What you do | Why it matters |
| --- | --- | --- | --- |
| 1. Raw | Groceries delivered, still in the bags | Load each file into a table exactly as it is, and look at it | You always keep the original, so you can start over if something goes wrong |
| 2. Clean | Wash, cut, throw out what's rotten | Fix formats, remove repeated rows, decide what to do with missing values, make IDs match | Bad data gives wrong answers, however nice the dashboard looks |
| 3. Ready | Cook the dish | Combine tables and calculate the numbers that answer the client's question | One table that answers one question is easy to check and easy to trust |
| 4. Serve | Plate it | Build a dashboard with a map and present your recommendation | The client needs an answer, not a table |

**At the end, deliver:**

- One dashboard, with a map.
- A 2-minute pitch to Santa: what did you find, what should Santa do, and how sure are you?
- **Be ready to explain three decisions:** which files you used, how you cleaned the data, and what you did with personal data. The facilitators will ask *why*.

## Working with Genie

Genie is the AI assistant built into Databricks. Open it from the Genie panel in your notebook.
<!-- SCREENSHOT: images/04_open_genie.png – a notebook with the Genie panel open and where to click to open it -->

Genie writes and runs the code. **Your group makes the decisions.** Genie will often stop and ask you to choose between options. That's on purpose.

- Ask for one step at a time. If you paste the whole task, you'll get an answer you can't explain in the pitch.
- Ask Genie to explain what it did in plain language whenever you're unsure.
- Questions that work well:
  - "Load the scanned letters into a table and show us 10 rows."
  - "What looks strange in this table?"
  - "What are our options for handling the repeated rows?"
  - "Where can we find the table you just created?"

## Where to find things

- **The raw files:** in the menu on the left, click **Catalog**, then **workspace → santa → raw**.
  <!-- SCREENSHOT: images/05_raw_files.png – Catalog with workspace → santa → raw open, showing the folders and files -->
- **Tables Genie creates:** also under **Catalog → workspace**, in the schema Genie used (ask Genie if you can't find it). Click a table and open **Sample data** to see what's in it.
  <!-- SCREENSHOT: images/06_table_sample_data.png – a table in Catalog with the Sample data tab open -->
- **"Select compute":** if Databricks asks you to select compute to show sample data, choose the only option available.
  <!-- SCREENSHOT: images/07_select_compute.png – the select compute prompt with the available option -->
- **Dashboards:** in the menu on the left, click **New → Dashboard**, add your finished table, and ask Genie to build the charts and the map.
  <!-- SCREENSHOT: images/08_new_dashboard.png – a new dashboard with a table added and the Genie panel open -->

## The data

Everyone gets the same files. Part of the job is choosing the ones you need.

| File or folder | What's in it |
| --- | --- |
| `wishes/email/` | Emails from children, one file per day |
| `wishes/letters/scanned_letters.csv` | Paper letters, scanned by the elves |
| `toys.parquet` | Santa's official toy list |
| `postcodes.csv` | Norwegian postcodes with place, region and coordinates |
| `production/` | Toys made per workshop per day, one file per week |
| `workshops.csv` | Santa's 10 workshops |
| `warehouses.csv` | Santa's 3 warehouses in Norway |
| `candidate_cities.csv` | 5 possible places for a new warehouse |
| `elves.csv` | Every elf, exported from the HR system |
| `shifts/` | Every elf shift from the time clock, one file per day |
| `pay_rates.csv` | What an hour of elf work costs |
| `satisfaction_survey.csv` | The elves' quarterly satisfaction survey |
| `catchup/` | Ready-made tables for groups that get stuck |

All data is invented for this workshop. The personal ID numbers are fake and don't belong to anyone.
