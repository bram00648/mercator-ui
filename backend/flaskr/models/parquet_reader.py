import duckdb
import pandas as pd
import json
from flaskr.config import Config

class ParquetReader:
    @staticmethod
    def read_parquet():
        """Reads the Parquet file and returns JSON as a Python list."""
        try:
            df = duckdb.read_parquet(Config.PARQUET_FILE_PATH).fetchdf()

            json_data = json.loads(df.to_json(orient="records"))  

            return json_data

        except Exception as e:
            return {"error": str(e)}
