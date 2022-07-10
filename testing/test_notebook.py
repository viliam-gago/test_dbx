# Databricks notebook source
df = spark.read.parquet("dbfs:/mnt/formula1dlvg/processed/races/")

# COMMAND ----------

display(df)

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /mnt/formula1dlvg/processed/circuits