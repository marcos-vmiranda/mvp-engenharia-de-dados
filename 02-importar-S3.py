# Databricks notebook source
# MAGIC %sql
# MAGIC USE CATALOG mvp;
# MAGIC USE SCHEMA staging;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE VOLUME IF NOT EXISTS volume01;

# COMMAND ----------

dbutils.fs.cp("s3a://pos-puc-mvp/ind-prod-ilha.csv", "dbfs:/Volumes/mvp/staging/volume01/ind-prod-ilha.csv")

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW VOLUMES
