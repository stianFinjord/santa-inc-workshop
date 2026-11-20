# Step 0 (cases 1 and 2): one wish list

Children sent their wishes in two ways: by email, and by paper letter that the elves scanned. Before you can answer anything, you need **one clean wish list**.

**Files:** `wishes/email/*.json`, `wishes/letters/scanned_letters.csv`, `toys.parquet`, `postcodes.csv`

1. Load the email files and the letter file into two raw tables.
2. An email can hold several wishes. Turn it into one row per wish.
3. Make the two tables look the same: same column names, same date format.
4. Match the toy names children wrote to the official toy list. Children don't spell well.
5. Stack the two tables into one, with a column saying where each wish came from.
6. Some children sent both an email and a letter. Santa gives each child **one** gift: their #1 wish. Keep one row per child.
7. The email data contains personal ID numbers. Should they be in your final table?

Stuck after 40 minutes? Load `catchup/wishes_clean.parquet` and move on to your case.
