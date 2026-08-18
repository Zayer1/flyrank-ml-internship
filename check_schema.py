import duckdb
import os

con = duckdb.connect()
con.execute("INSTALL httpfs; LOAD httpfs;")
hf_token = "YOUR_HF_TOKEN"
con.execute(f"CREATE SECRET (TYPE HUGGINGFACE, TOKEN '{hf_token}');")

query = """
DESCRIBE SELECT * FROM 'hf://datasets/FlyRank/internship-warehouse/fact_content_daily_performance/month=2026-03/*.parquet' LIMIT 1
"""
print(con.execute(query).df())
