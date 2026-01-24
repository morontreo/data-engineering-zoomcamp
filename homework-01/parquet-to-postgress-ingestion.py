import pandas as pd
from sqlalchemy import create_engine
from tqdm import tqdm

# 1. Load data
df = pd.read_parquet('green_tripdata_2025-11.parquet')
table_name = 'green_tripdata'
chunksize = 10000  # Number of rows per batch

engine = create_engine('postgresql://YOUR_USER:YOUR_PWD@localhost:YOUR_PORT/ny_taxi')

# 2. Use a progress bar
with tqdm(total=len(df), desc="Uploading to Postgres") as pbar:
    for i, chunk in enumerate(range(0, len(df), chunksize)):
        replace_mode = 'replace' if i == 0 else 'append'
        
        df.iloc[chunk:chunk + chunksize].to_sql(
            table_name, 
            engine, 
            if_exists=replace_mode, 
            index=False
        )
        pbar.update(len(df.iloc[chunk:chunk + chunksize]))

print("Upload complete!")