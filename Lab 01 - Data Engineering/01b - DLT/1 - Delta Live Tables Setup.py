# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC ## Introduction

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Delta Live Tables (DLT) makes it easy to build and manage reliable data pipelines that deliver high quality data on Delta Lake. 
# MAGIC
# MAGIC DLT helps data engineering teams simplify ETL development and management with declarative pipeline development, automatic data testing, and deep visibility for monitoring and recovery.
# MAGIC
# MAGIC <img src="https://databricks.com/wp-content/uploads/2021/09/Live-Tables-Pipeline.png" width=1012/>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Set up Environment

# COMMAND ----------

# MAGIC %run ../Utils/prepare-lab-environment-mini

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Setup Pipeline
# MAGIC
# MAGIC Setup your serverless DLT pipeline from 'Data Engineering -> Delta Live Tables' section on the left menu.
# MAGIC When configuring the pipeline; set the following configuration options
# MAGIC  - Serverless turned on
# MAGIC  - "Triggered" mode
# MAGIC  - Use the `2 - Transform` notebook
# MAGIC  - Under destination, write to Unity Catalog, using the `datafoundations_sandpit` catalog, and your bootcamp schema
# MAGIC  - Under `Advanced -> Configuration` add a new configuration key `source_volume` with your volume's path ie `/Volumes/datafoundations_sandpit/<bootcamp_schema>/bootcamp`
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Create and Run your Pipeline NOW
# MAGIC
# MAGIC It will take some time for pipeline to start. While waiting - explore `02 - Transform` notebook to see the actual code used to create it.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Incremental Updates

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC Simulate new batch files being uploaded to cloud location. You can run it multiple times - it will generate a sample of orders for randomly selected store.
# MAGIC
# MAGIC If pipeline is running in continuous mode - files will be processed as soon as they are uploaded. Otherwise new files will be picked up on the next run.

# COMMAND ----------

generate_more_orders()
