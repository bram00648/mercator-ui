import pandas as pd
import json
from flaskr.config import Config
import os
from flask import current_app

class ParquetReader:
    @staticmethod
    def read_parquet():
        """Reads the Parquet file and returns JSON as a Python list."""
        try:
            dfarr = []
            parquet_path = Config.PARQUET_FILE_PATH
            current_app.logger.info(f"Reading Parquet files from: {parquet_path}")

            files = os.listdir(parquet_path)
            current_app.logger.info(f"Files in directory: {files}")

            for i in files:
                if i.endswith('.parquet'):
                    file_path = os.path.join(parquet_path, i)
                    current_app.logger.info(f"Reading file: {file_path}")
                    df = pd.read_parquet(file_path)
                    dfarr.append(df)
                    current_app.logger.info(df)  


            combined_df = pd.concat(dfarr, ignore_index=True)
            json_data = json.loads(combined_df.to_json(orient="records"))

            return json_data

        except Exception as e:
            current_app.logger.error(f"Error reading parquet files: {e}")
            return {"error": str(e)}