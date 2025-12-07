# Databricks notebook source
spark.sql("USE CATALOG mvp")
spark.sql("USE SCHEMA gold")

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Cria uma view acrescentando o nome do centro e da ilha
# MAGIC CREATE OR REPLACE TABLE ind_prod_ilha_completa AS 
# MAGIC SELECT centro.Nome, 
# MAGIC   ilha.Nome,
# MAGIC   NB.primaryProfession,
# MAGIC   TB.tconst,
# MAGIC   TB.originalTitle,
# MAGIC   TB.primaryTitle
# MAGIC FROM mvp.silver.ind_prod_ilha as ind
# MAGIC INNER JOIN mvp.silver.ilha as ilha
# MAGIC   ON ind.Ilha = ilha.id
# MAGIC INNER JOIN mvp.silver.centro as centro
# MAGIC   ON ind.Centro = centro.id

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM name_title_basics
# MAGIC LIMIT 10
