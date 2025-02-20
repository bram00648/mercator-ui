import pandas as pd
import duckdb
import json
import os
from flask import current_app
from flaskr.config import Config

class ParquetReader:
    @staticmethod
    def read_parquet():
        """Reads the Parquet file and returns JSON as a Python list."""
        try:
            parquet_path = Config.PARQUET_FILE_PATH
            current_app.logger.info(f"Reading Parquet files from: {parquet_path}")

            parquet_files = [f for f in os.listdir(parquet_path) if f.endswith(".parquet")]
            current_app.logger.info(f"Found files: {parquet_files}")

            dfarr = []

            for i in parquet_files:
                file_path = os.path.join(parquet_path, i)
                current_app.logger.info(f"Processing file: {file_path}")

                try:
                    duckdb_conn = duckdb.connect(":memory:")
                    duckdb_data = duckdb_conn.sql(f"SELECT fresh FROM read_parquet('{file_path}') LIMIT 1")
                    current_app.logger.info(duckdb_data) # for each column we should get the data and convert it to json manually because parquet SUCKS
                    """
                    1. we read for every column the data seperately because it is always stored in a single json or array of json objects
                    2. every column belongs to 1 parent json object which is defined by for example the visitId? i think
                    3. we should be able to construct a valid json object from this data from parquet but it will require manual work
                    4. doing this should make it possible to conver other parquet files in a similar way. this way we can always acess Json data
                    
                    """
                    with open("fs.txt", "w") as f:
                        f.write(duckdb_data.df().to_string(index=False))

                    duckdb_data = duckdb_data.to_df()

                    duckdb_data = duckdb_data.to_json()

                    current_app.logger.info(duckdb_data)

                except Exception as e:
                    current_app.logger.error(f"Error reading Parquet file {file_path}: {e}")
                    continue  # Skip problematic file

            if not dfarr:
                return {"error": "No valid data found."}

            combined_df = pd.concat(dfarr, ignore_index=True)
            json_data = json.loads(combined_df.to_json(orient="records"))

            return json_data

        except Exception as e:
            current_app.logger.error(f"Error processing parquet files: {e}")
            return {"error": str(e)}
