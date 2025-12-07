# Databricks notebook source
spark.sql("USE CATALOG mvp")
spark.sql("USE SCHEMA silver") #Após carregar as outras tabelas, trocar pra GOLD

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM ind_prod_ilha
# MAGIC LIMIT 10

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Qual foi o indicador de disponibilidade, performance e qualidade das ilhas do terminal 5012 no mês de janeiro de 2025
# MAGIC SELECT 
# MAGIC   ind.Centro,
# MAGIC   ind.Ilha,
# MAGIC   ROUND(
# MAGIC     SUM(CAST(ind.TempoProducaoReal AS DOUBLE) / CAST(ind.TempoProducaoPlan AS DOUBLE))
# MAGIC     ,2
# MAGIC   ) AS indicador_disponibilidade,
# MAGIC   ROUND(SUM(CAST(ind.QuantProducaoReal AS DOUBLE) / CAST(ind.QuantProducaoPlan AS DOUBLE)),2) AS indicador_performance,
# MAGIC   ROUND(
# MAGIC     SUM(
# MAGIC       CAST(ind.QuantProducaoBoa AS DOUBLE) / 
# MAGIC       ( CAST(ind.QuantProducaoRuim AS DOUBLE) + CAST(ind.QuantProducaoBoa As DOUBLE) )
# MAGIC     ),2
# MAGIC   ) AS indicador_qualidade,
# MAGIC   ROUND(
# MAGIC     (indicador_disponibilidade * indicador_performance * indicador_qualidade)
# MAGIC     ,2
# MAGIC     ) AS indicador_oee
# MAGIC FROM ind_prod_ilha AS ind
# MAGIC WHERE ind.Centro = 5012
# MAGIC   AND ind.Data BETWEEN '2025-11-01' AND '2025-11-30'
# MAGIC GROUP BY ind.Centro, ind.Ilha

# COMMAND ----------

# Usar a bilioteca pandas pra gerar um gráfico de barras contendo a performance de cada ilha no mês de novembro de 2025
import pandas as pd
import matplotlib.pyplot as plt
df = spark.sql("SELECT Ilha, ROUND(SUM(CAST(ind.QuantProducaoReal AS DOUBLE) / CAST(ind.QuantProducaoPlan AS DOUBLE)),2) AS indicador_performance FROM ind_prod_ilha AS ind WHERE Data >= '2025-11-01' AND Data < '2025-12-01' AND Centro=5012 GROUP BY Ilha ORDER BY Ilha")
df = df.toPandas()
df.plot.bar(x='Ilha', y='indicador_performance', rot=0, figsize=(20, 6))
plt.title('Performance de cada ilha no mês de novembro de 2025')
plt.xlabel('Ilha')
plt.ylabel('Performance')
plt.show()

