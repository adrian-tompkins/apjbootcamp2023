# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC ## Prepare your lab
# MAGIC
# MAGIC Run the next 2 cells to generate some data we will be using for this lab.
# MAGIC
# MAGIC Data will be stored in a separate location

# COMMAND ----------

# MAGIC %run ../Utils/prepare-lab-environment

# COMMAND ----------

# This will take up to 2min to run
generate_sales_dataset()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ingest data from cloud storage
# MAGIC
# MAGIC If your data is already in the cloud - you can simply read it from S3/ADLS 

# COMMAND ----------

products_cloud_storage_location = f'{datasets_location}products/products.json'
df = spark.read.json(products_cloud_storage_location)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Hands On Task!
# MAGIC
# MAGIC Do you remember how to explore this dataset using notebooks?
# MAGIC
# MAGIC Hint: use `display()` or `createOrReplaceTempView()`

# COMMAND ----------

# Explore customers dataset

... # do display(<your dataframe>)

# Create a temporary view (notebook scope - only accessible in this notebok) to query it using SQL
df.createOrReplaceTempView(<your view name>)

# COMMAND ----------

# MAGIC %sql 
# MAGIC -- If you're using SQL you might want to create your 
# MAGIC SELECT * FROM <your view name>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Ingesting new files from same location
# MAGIC
# MAGIC The [`COPY INTO`](https://docs.databricks.com/sql/language-manual/delta-copy-into.html) SQL command lets you load data from a file location into a Delta table. This is a re-triable and idempotent operation; files in the source location that have already been loaded are skipped.
# MAGIC
# MAGIC `FORMAT_OPTIONS ('mergeSchema' = 'true')` - Whether to infer the schema across multiple files and to merge the schema of each file. Default = false. Enabled by default for Auto Loader when inferring the schema.
# MAGIC `COPY_OPTIONS ('mergeSchema' = 'true')` - default false. If set to true, the schema can be evolved according to the incoming data.

# COMMAND ----------

spark.sql("CREATE TABLE IF NOT EXISTS my_products;")

spark.sql(f"""
COPY INTO my_products 
FROM '{datasets_location}products/'
FILEFORMAT = json
FORMAT_OPTIONS ('mergeSchema' = 'true') -- applies schema merge accross all source files
COPY_OPTIONS ('mergeSchema' = 'true') -- applies schema merge on target table if source schema is different
""")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Hands On Task!
# MAGIC
# MAGIC We also have stores dataset available. Write COPY INTO statement for that dataset using `%sql` cell. 
# MAGIC
# MAGIC Hint: Use `dbutils.fs.ls(datasets_location)` to find sales dataset files and print that location to get full path for SQL

# COMMAND ----------

dbutils.fs.ls(f"{datasets_location}/stores")

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC -- You need to first create your table..
# MAGIC CREATE TABLE IF NOT EXISTS my_stores;
# MAGIC
# MAGIC -- You ingest data into your table from datasets_location/stores location
# MAGIC -- Exlore what is your file format.. 
# MAGIC COPY INTO my_stores
# MAGIC FROM 'TODO: <your source file path >'
# MAGIC FILEFORMAT = JSON
# MAGIC FORMAT_OPTIONS ('mergeSchema' = 'true')
# MAGIC COPY_OPTIONS ('mergeSchema' = 'true');

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Advanced Task
# MAGIC
# MAGIC What would that look using autoloader? You can find syntax for it here: https://docs.databricks.com/getting-started/etl-quick-start.html

# COMMAND ----------

# Optional: write autoloader statement to load sales records

# We need to specify checkpoint location for our autoloader metadata, let's keep it next to the table
checkpoint_path = f"{datasets_location}/checkpoints/stores"

(spark.readStream
  .format("TODO: <autoloader file format>")
  .option("cloudFiles.format", "< TODO: source file format>")
  .option("cloudFiles.schemaLocation", checkpoint_path)
  .load(f"{datasets_location}/stores") #
  .writeStream
  .option("checkpointLocation", checkpoint_path)
  .trigger(availableNow=True)
  .toTable(< TODO: your table name >))
