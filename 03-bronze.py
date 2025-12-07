# Databricks notebook source
spark.sql("USE CATALOG mvp")
spark.sql("USE SCHEMA bronze")

# COMMAND ----------

df = spark.read.option("header", True).option("sep", ";").csv("dbfs:/Volumes/mvp/staging/volume01/ind-prod-ilha.csv")
display(df.limit(10))

# COMMAND ----------

df.write.format("delta").mode("overwrite").saveAsTable("ind_prod_ilha")

# COMMAND ----------

spark.sql("""
  COMMENT ON TABLE mvp.bronze.ind_prod_ilha IS 
  'Contém informação sobre os indicadores de disponibilidade, performance e qualidade das ilhas dos terminais.'
""")
spark.sql("""
  COMMENT ON COLUMN mvp.bronze.ind_prod_ilha.Centro IS 'Primary Key do terminal'
""")
spark.sql("""
  COMMENT ON COLUMN mvp.bronze.ind_prod_ilha.DATA IS 'Data do indicador no formato AAAA-MM-DD'
""")
spark.sql("""
  COMMENT ON COLUMN mvp.bronze.ind_prod_ilha.Ilha IS 'Nome da ilha'
""")
spark.sql("""
  COMMENT ON COLUMN mvp.bronze.ind_prod_ilha.TempoProducaoReal IS 'Tempo de produção real da ilha'
""")
spark.sql("""
  COMMENT ON COLUMN mvp.bronze.ind_prod_ilha.TempoProducaoPlan IS 'Tempo de produção planejado da ilha'
""")
spark.sql("""
  COMMENT ON COLUMN mvp.bronze.ind_prod_ilha.QuantProducaoReal IS 'Quantidade de produção real da ilha'
""")
spark.sql("""
  COMMENT ON COLUMN mvp.bronze.ind_prod_ilha.QuantProducaoPlan IS 'Quantidade de produção planejada da ilha'
""")
spark.sql("""
  COMMENT ON COLUMN mvp.bronze.ind_prod_ilha.QuantProducaoRuim IS 'Quantidade de produção ruim da ilha'
""")
spark.sql("""
  COMMENT ON COLUMN mvp.bronze.ind_prod_ilha.QuantProducaoBoa IS 'Quantidade de produção boa da ilha'
""")

