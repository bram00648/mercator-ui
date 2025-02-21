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
                    json_data_array = duckdb_conn.sql(f"""
                                                  
                                                  SELECT json(
                                                  json_object(
                                                    'vistId', visitId,
                                                    'domainName', domainName,
                                                    'timestamp', timestamp,
                                                    'numConversations', numConversations,
                                                    'hosts', hosts,
                                                    'crawlStatus', crawlStatus
                                                    )
                                                  ) as result
                                                    FROM '{file_path}'
                                                  
                                                  """).fetchall(    )
                    current_app.logger.info(json_data_array ) # for each column we should get the data 
                    objects = []
                    for i in json_data_array:
                        current_app.logger.info("here: " + i[0] + "\n"+ "\n"+ "\n"+ "\n"+ "\n"+ "\n") 
                        
                        objects.append(json.loads(i[0]))
                        
                    objects_dumps_data = json.dumps(objects, indent=2)
                    current_app.logger.info(objects_dumps_data)
                    
                    #clean_data = clean_parquet_data(column_data)
                    #current_app.logger.info(clean_data)

                    #final_column_data_json = {"visitRequest": processed_rows}

                    #final_data = json.dumps(final_column_data_json, indent=2)

                    #current_app.logger.info(final_data)
                
                    
                except Exception as e:
                    current_app.logger.error(f"Error reading Parquet file {file_path}: {e}")
                    continue 

            return True

        except Exception as e:
            current_app.logger.error(f"Error processing parquet files: {e}")
            return {"error": str(e)}
