import pandas as pd
import duckdb
import json
import os
from flask import current_app
from flaskr.config import Config
import re
import uuid

def clean_parquet_data(data):
    """Converts tuples containing dictionaries with UUIDs into a valid JSON array."""
    cleaned_data = []

    for row in data:
        record = row[0]  # Extract the dictionary from the tuple
        cleaned_record = {k: str(v) if isinstance(v, uuid.UUID) else v for k, v in record.items()}
        cleaned_data.append(cleaned_record)

    return json.dumps(cleaned_data, indent=2)


class ParquetReader:

    
    @staticmethod
    def read_parquet():
        """Reads the Parquet file and returns JSON as a Python list."""
        try:
            parquet_path = Config.PARQUET_FILE_PATH
            current_app.logger.info(f"Reading Parquet files from: {parquet_path}" + "\n")

            parquet_files = [f for f in os.listdir(parquet_path) if f.endswith(".parquet")]
            current_app.logger.info(f"Found files: {parquet_files}" + "\n")


            for i in parquet_files:
                file_path = os.path.join(parquet_path, i)

                try:
                    duckdb_conn = duckdb.connect(":memory:")
                    column_data = duckdb_conn.sql(f"SELECT visitRequest FROM read_parquet('{file_path}') LIMIT 10").fetchall()
                    current_app.logger.info(column_data ) # for each column we should get the data and convert it to json manually because parquet
                    """
                    1. read for every column the data seperately because it is always stored in dictionary lik eojbect
                    2. every column belongs to 1 parent json object which is defined by for example the visitId? i think
                    3. construct a valid json object from this data from parquet but it will require parsing
                    4. doing this should make it possible to conver other parquet files in a similar way. this way we can always acess Json data         
                    """
                    processed_rows = []

                    clean_data = clean_parquet_data(column_data)
                    current_app.logger.info(clean_data)

                    final_column_data_json = {"visitRequest": processed_rows}

                    final_data = json.dumps(final_column_data_json, indent=2)

                    current_app.logger.info(final_data)
                
                    
                except Exception as e:
                    current_app.logger.error(f"Error reading Parquet file {file_path}: {e}")
                    continue 

            return True

        except Exception as e:
            current_app.logger.error(f"Error processing parquet files: {e}")
            return {"error": str(e)}
