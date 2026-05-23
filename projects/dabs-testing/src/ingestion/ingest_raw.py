from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp, input_file_name


def ingest_raw_files(spark: SparkSession, source_path: str, target_table: str) -> None:
    """Read JSON files from source_path and append them to a Delta table.

    Adds two metadata columns to every row:
    - ingestion_timestamp: when this batch was ingested
    - source_file: the S3 path of the file each row originated from

    Args:
        spark: active SparkSession
        source_path: S3 path (or glob) to read JSON files from, e.g. "s3://bucket/raw/events/"
        target_table: fully-qualified table name to append into, e.g. "catalog.schema.events_raw"
    """
    (
        spark.read.format("json")
        .load(source_path)
        .withColumn("ingestion_timestamp", current_timestamp())
        .withColumn("source_file", input_file_name())
        .write.mode("append")
        .saveAsTable(target_table)
    )
