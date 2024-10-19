# Databricks notebook source
current_user_id = dbutils.notebook.entry_point.getDbutils().notebook().getContext().userName().get()

# COMMAND ----------

database_name = current_user_id.split('@')[0].replace('.','_')+'_bootcamp'
spark.sql(f'drop database if exists {database_name} cascade;')
