import pandas as pd
import duckdb
import json
import os
from flask import current_app
from flaskr.config import Config
import re


def fix_invalid_json(json_str):
    uuid_pattern = r'(?<!["\'])\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b(?!["\'])'
    fixed_json_str = re.sub(uuid_pattern, r'"\g<0>"', json_str)   
    return fixed_json_str

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
                    collumn1 = duckdb_conn.sql(f"SELECT visitRequest FROM read_parquet('{file_path}') LIMIT 2")
                    current_app.logger.info(collumn1) # for each column we should get the data and convert it to json manually because parquet SUCKS
                    """
                    1. we read for every column the data seperately because it is always stored in a single json or array of json objects
                    2. every column belongs to 1 parent json object which is defined by for example the visitId? i think
                    3. we should be able to construct a valid json object from this data from parquet but it will require manual work
                    4. doing this should make it possible to conver other parquet files in a similar way. this way we can always acess Json data
                    
                    """

                    """this part will convert the json string in that collumn back to a correct json"""
                    stringcolumn = collumn1.df().to_string(index=False).lstrip() # remove trailing whitespace
                    raw_column_string = stringcolumn.replace("visitRequest","")# TODO: remove hardcoding of column name make it iterable later
                    print(raw_column_string, flush=True)
                    fixed_uuid_column_string = fix_invalid_json(raw_column_string)
                    fixed_json = fixed_uuid_column_string.replace("'", '"')
                    parsed_data = json.loads(fixed_json)
                    final_column_data_json = {"visitRequest": parsed_data}

                    final_data = json.dumps(final_column_data_json, indent=2)

                    current_app.logger.info(final_data)
                
                    
                except Exception as e:
                    current_app.logger.error(f"Error reading Parquet file {file_path}: {e}")
                    continue 
            if not dfarr:
                return {"error": "No valid data found."}

            combined_df = pd.concat(dfarr, ignore_index=True)
            json_data = json.loads(combined_df.to_json(orient="records"))

            return json_data

        except Exception as e:
            current_app.logger.error(f"Error processing parquet files: {e}")
            return {"error": str(e)}
