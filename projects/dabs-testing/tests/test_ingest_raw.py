import json
import pytest
from pyspark.sql import SparkSession

from ingestion.ingest_raw import ingest_raw_files


@pytest.fixture(scope="session")
def spark():
    session = (
        SparkSession.builder.master("local[*]")
        .appName("test")
        .config("spark.sql.shuffle.partitions", "1")
        .getOrCreate()
    )
    yield session
    session.stop()


def test_ingest_raw_files(spark, tmp_path):
    # Write sample JSON records to a temp directory
    records = [
        {"id": 1, "event": "login"},
        {"id": 2, "event": "logout"},
        {"id": 3, "event": "purchase"},
    ]
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    (source_dir / "events.json").write_text("\n".join(json.dumps(r) for r in records))

    target_table = "test_ingest_raw_output"

    try:
        ingest_raw_files(spark, str(source_dir), target_table)

        df = spark.table(target_table)

        assert df.count() == 3
        assert "ingestion_timestamp" in df.columns
        assert "source_file" in df.columns
    finally:
        spark.sql(f"DROP TABLE IF EXISTS {target_table}")
