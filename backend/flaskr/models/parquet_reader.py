import pandas as pd
import duckdb
import json
import os
from flask import current_app
from flaskr.config import Config
import re
import uuid
import traceback
class ParquetReader:

    
    @staticmethod
    def read_parquet():
        """Reads the Parquet file and returns JSON as a Python list."""
        try:
            parquet_path = Config.PARQUET_FILE_PATH
            current_app.logger.info(f"Reading Parquet files from: {parquet_path}" + "\n")

            parquet_files = sorted([f for f in os.listdir(parquet_path) if f.endswith(".parquet")]) 

            
            current_app.logger.info(f"Found files: {parquet_files}" + "\n")
            file_paths = []

            for i in parquet_files:
                file_path = os.path.join(parquet_path, i)
                file_paths.append(file_path)

            file_paths = sorted(file_paths)
            current_app.logger.info(f"Reading files: {file_paths}" + "\n")

            SMTP = file_paths[0]
            TLS = file_paths[1]
            WEB = file_paths[2]

            try:
                duckdb_conn = duckdb.connect(":memory:")
                duckdb_conn.execute(f"""
                    CREATE TABLE joined_tls_smtp_web as select * from '{TLS}' tl
                    INNER JOIN '{SMTP}' sm ON tl.visitRequest.visitId = sm.visitId
                    INNER JOIN '{WEB}' w on sm.visitId = w.visitId;
                                    """)
                json_data_array = duckdb_conn.sql(f"""
                select json(
                    json_object(
                        'visitRequest', visitRequest,
                        'fullScanEntity', fullScanEntity,
                        'certificateChain', certificateChain,
                        'peerCertificate', peerCertificate,
                        'fresh', fresh,
                        'visitId', visitId,
                        'domainName', domainName,
                        'timestamp', timestamp,
                        'numConversations', numConversations,
                        'hosts', hosts,
                        'crawlStatus', crawlStatus,
                        'web_visitId', visitId_1,
                        'web_domainName', domainName_1,
                        'startUrl', startUrl,
                        'matchingUrl', matchingUrl,
                        'crawlStarted', crawlStarted,
                        'CrawlFinished', crawlFinished,
                        'vatValues', vatValues,
                        'visitedUrls', visitedUrls,
                        'pageVisits', pageVisits,
                        'htmlFeatures', htmlFeatures
                    )
                ) as result
            from joined_tls_smtp_web;""").fetchall()
                current_app.logger.info(json_data_array )
                objects = []
                for i in json_data_array:
                    current_app.logger.info("here: " + i[0] + "\n"+ "\n"+ "\n"+ "\n"+ "\n"+ "\n") 
                        
                    objects.append(json.loads(i[0]))
                        
                objects_dumps_data = json.dumps(objects, indent=2)
                    
                current_app.logger.info(objects_dumps_data)
                    

                    
            except Exception as e:
                current_app.logger.error(f"Error reading Parquet file {file_path}: {e}")
                traceback.print_exc()
                return {"error": str(e)}    
            

                 

            return objects

        except Exception as e:
            current_app.logger.error(f"Error processing parquet files: {e}")
            return {"error": str(e)}
