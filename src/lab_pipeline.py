from pyspark.sql import DataFrame, functions as F

def optimize_events(df: DataFrame) -> DataFrame:
 """Validate, deduplicate, and enrich event data for a Delta table."""
 required={"event_id","event_ts","customer_id","value"}
 if required-set(df.columns):raise ValueError("event schema is incomplete")
 return (df.filter(F.col("value").isNotNull()).dropDuplicates(["event_id"])
   .withColumn("event_date",F.to_date("event_ts"))
   .withColumn("value_band",F.when(F.col("value")>=100,"high").otherwise("standard")))

def write_delta(df: DataFrame,path:str):
 (df.write.format("delta").mode("overwrite").partitionBy("event_date").save(path))