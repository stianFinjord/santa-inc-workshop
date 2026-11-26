# Databricks notebook source
# MAGIC %md
# MAGIC # Step 1: load Santa's data
# MAGIC
# MAGIC Run this notebook **once**: click **Run all** at the top. It takes a minute or two.
# MAGIC
# MAGIC It creates a place for the data (a *volume*) and copies all the raw files from this repo into it.
# MAGIC When it prints **All set!**, go back to the README, create your working notebook, and open `2_TASKS.md`.

# COMMAND ----------

import os
import shutil

CATALOG = spark.sql("SELECT current_catalog()").first()[0]  # usually "workspace" in Free Edition
SCHEMA = "santa"
VOLUME = "raw"

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {CATALOG}.{SCHEMA}")
spark.sql(f"CREATE VOLUME IF NOT EXISTS {CATALOG}.{SCHEMA}.{VOLUME}")
target = f"/Volumes/{CATALOG}/{SCHEMA}/{VOLUME}"
print("The data will go to:", target)

# COMMAND ----------

# Find the data folder in this repo (it sits next to this notebook)
source = os.path.join(os.getcwd(), "data", "raw")
if not os.path.isdir(source):
    notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
    source = os.path.join("/Workspace" + os.path.dirname(notebook_path), "data", "raw")
assert os.path.isdir(source), f"Could not find the data folder. Looked in: {source}"
print("Copying from:", source)

# COMMAND ----------

copied = 0
for folder, _, files in os.walk(source):
    relative = os.path.relpath(folder, source)
    destination = target if relative == "." else os.path.join(target, relative)
    os.makedirs(destination, exist_ok=True)
    for name in files:
        shutil.copyfile(os.path.join(folder, name), os.path.join(destination, name))
        copied += 1
print(f"Copied {copied} files")

# COMMAND ----------

# Check what is in the volume now
for item in sorted(os.listdir(target)):
    path = os.path.join(target, item)
    count = sum(len(f) for _, _, f in os.walk(path)) if os.path.isdir(path) else 1
    print(f"{item:<28} {count} file(s)")

print(f"\nAll set! Use this path in your queries: {target}/")
if CATALOG != "workspace":
    print(f"Note: the README and 2_TASKS.md say /Volumes/workspace/santa/raw/. Your data is in {target}/ instead.")
