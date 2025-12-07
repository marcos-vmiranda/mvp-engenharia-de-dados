# Databricks notebook source
spark.sql("USE CATALOG mvp")
spark.sql("USE SCHEMA silver")

# COMMAND ----------

from pyspark.sql.functions import split, explode, trim, lower

df = spark.table("mvp.bronze.ind_prod_ilha")

#df_expanded = (
#    df.drop("birthYear", "deathYear")
#    .withColumn("primaryProfession", explode(split("primaryProfession", ",")))
#    .withColumn("primaryProfession", trim(lower("primaryProfession")))
#    .filter((df.primaryProfession == "actor") | (df.primaryProfession == "actress"))
#    .withColumn("knownForTitles", explode(split("knownForTitles", ",")))
#    .withColumn("knownForTitles", trim("knownForTitles"))
#    .filter(df.knownForTitles != "\\N")
#)

#Limpa os dados
df_tratado = (
    df.dropna()
)

df_tratado.write.mode("overwrite").saveAsTable("ind_prod_ilha")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM ind_prod_ilha 
# MAGIC LIMIT 10

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*)
# MAGIC FROM ind_prod_ilha
