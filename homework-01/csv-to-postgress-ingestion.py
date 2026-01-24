import pandas as pd
from sqlalchemy import create_engine
import os

# 1. Setup Configuration
file_path = 'taxi_zone_lookup.csv'
table_name = 'taxi_zone_lookup'
db_url = 'postgresql://YOUR_USER:YOUR_PWD@localhost:YOUR_PORT/ny_taxi'
chunk_size = 10000 

engine = create_engine(db_url)

try:
    # 2. Check file size for logging
    file_size = os.path.getsize(file_path) / (1024 * 1024)
    print(f"Starting import: {file_path} ({file_size:.2f} MB)")

    # 3. Read and upload in chunks
    # We use a context manager for the reader to handle memory efficiently
    with pd.read_csv(file_path, chunksize=chunk_size) as reader:
        for i, chunk in enumerate(reader):
            # On the first chunk, 'replace' the table. 
            # On subsequent chunks, 'append' the data.
            mode = 'replace' if i == 0 else 'append'
            
            chunk.to_sql(table_name, engine, if_exists=mode, index=False)
            
            rows_processed = (i + 1) * chunk_size
            print(f"Logged: Processed {rows_processed} rows...")

    print(f"Successfully imported {table_name} to Postgres.")

except Exception as e:
    print(f"An error occurred: {e}")