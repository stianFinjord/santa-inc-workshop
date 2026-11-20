# Cheat sheet

You only need plain SQL. The setup notebook has already put all raw files in `/Volumes/workspace/santa/raw/`.
(If the setup notebook printed a different path, use that one.)

```sql
-- 1. Raw: load a file (or a folder of files) as it is
CREATE TABLE bronze_letters AS
SELECT * FROM read_files('/Volumes/workspace/santa/raw/wishes/letters/', format => 'csv', header => true);

-- JSON files work the same way
CREATE TABLE bronze_emails AS
SELECT * FROM read_files('/Volumes/workspace/santa/raw/wishes/email/', format => 'json');

-- 2. Clean: a new table from the raw one
CREATE TABLE silver_letters AS
SELECT DISTINCT letter_id, TRIM(LOWER(toy_text)) AS toy_text, TO_DATE(scanned_date, 'dd.MM.yyyy') AS received_date
FROM bronze_letters
WHERE letter_id IS NOT NULL;

-- One row per item in a list (for nested JSON)
SELECT email_id, sender.name, w.rank, w.toy FROM bronze_emails LATERAL VIEW explode(wishes) AS w;

-- 3. Ready: combine and count
CREATE TABLE gold_shortage AS
SELECT t.toy_name, COUNT(*) AS wishes
FROM silver_wishes w JOIN silver_toys t ON w.toy_sku = t.toy_sku
GROUP BY t.toy_name;
```

**4. Serve:** create a dashboard, add your gold table, and ask Genie to build the charts and the map. Then check one number with your own SQL.
