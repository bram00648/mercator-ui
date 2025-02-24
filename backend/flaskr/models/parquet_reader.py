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

    def get_file_paths():
        parquet_path = Config.PARQUET_FILE_PATH
        current_app.logger.info(f"Reading Parquet files from: {parquet_path}" + "\n")

        parquet_files = sorted([f for f in os.listdir(parquet_path) if f.endswith(".parquet")]) 

        file_paths = []

        for i in parquet_files:
            file_path = os.path.join(parquet_path, i)
            file_paths.append(file_path)

        file_paths = sorted(file_paths)
        current_app.logger.info(f"Reading files: {file_paths}" + "\n")

        return file_paths

    
    @staticmethod
    def read_all_data_parquet():
        """Reads the Parquet file and returns JSON as a Python list."""

        file_paths = ParquetReader.get_file_paths()

        SMTP = file_paths[0]
        TLS = file_paths[1]
        WEB = file_paths[2]

        try:
            duckdb_conn = duckdb.connect(":memory:")

            json_data_array = duckdb_conn.sql(f"""
                                              
            WITH joined_tls_smtp_web AS (
                    SELECT * FROM '{TLS}' tl
                    INNER JOIN '{SMTP}' sm ON tl.visitRequest.visitId = sm.visitId
                    INNER JOIN '{WEB}' w ON sm.visitId = w.visitId
                    
            )
                                              
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
            current_app.logger.error(f"Error reading Parquet file : {e}")
            traceback.print_exc()
            return {"error": str(e)}    
            

                 
        duckdb_conn.close()
        return objects

        

    def read_parquet_data_by_domain_name(domain_name):
        file_paths = ParquetReader.get_file_paths()

        SMTP = file_paths[0]
        TLS = file_paths[1]
        WEB = file_paths[2]

        duckdb_conn = duckdb.connect(":memory:")
        retrieved_domain_name = duckdb_conn.sql(f"""
SELECT domainName FROM '{WEB}' WHERE domainName = '{domain_name}';
                                                    """).fetchall()
        
        

        if retrieved_domain_name:
            current_app.logger.info(f"retrieved domain name: {retrieved_domain_name[0][0]}")
        else:
            current_app.logger.info(f"domain name not found: {domain_name}")
            return {"error": "Domain name not found"}
            
        if retrieved_domain_name[0][0] == domain_name:
            current_app.logger.info(f"found domain name"+ "\n"+ "\n"+ "\n"+ "\n"+ "\n"+ "\n" '{retrieved_domain_name}') 

            try:
                duckdb_conn = duckdb.connect(":memory:")

                json_data_array = duckdb_conn.sql(f"""
                WITH joined_tls_smtp_web AS (
                    SELECT * FROM '{TLS}' tl
                    INNER JOIN '{SMTP}' sm ON tl.visitRequest.visitId = sm.visitId
                    INNER JOIN '{WEB}' w ON sm.visitId = w.visitId
                    
                )
                                                  

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
            from joined_tls_smtp_web WHERE domainName = '{domain_name}';""").fetchall()
                

                current_app.logger.info(json_data_array )
                objects = []
                for i in json_data_array:
                    current_app.logger.info("here: " + i[0] + "\n"+ "\n"+ "\n"+ "\n"+ "\n"+ "\n") 
                            
                    objects.append(json.loads(i[0]))
                            
                objects_dumps_data = json.dumps(objects, indent=2)
                        
                current_app.logger.info(objects_dumps_data)
                duckdb_conn.close()

                return objects
                

            except Exception as e:
                current_app.logger.error(f"Error reading Parquet file : {e}")
                traceback.print_exc()
                return {"error": str(e)}
       
        return {"error": "Domain name not found"}
    

    def read_parquet_get_crawl_visit_ids_of_domain_name(domain_name):
        file_paths = ParquetReader.get_file_paths()

        SMTP = file_paths[0]
        TLS = file_paths[1]
        WEB = file_paths[2]

        duckdb_conn = duckdb.connect(":memory:")
        data = duckdb_conn.sql(f"""
SELECT visitId, domainName, crawlFinished  FROM '{WEB}' WHERE domainName = '{domain_name}';
                                                    """).fetchall()
        

        current_app.logger.info("retrieved_domain_name: " + str(data))

        result = [
            {"visitId": str(row[0]), "domainName": row[1], "crawlFinished": row[2]}
            for row in data
        ]

        return result
    




    def read_parquet_data_by_visit_id(visit_id):
        file_paths = ParquetReader.get_file_paths()

        SMTP = file_paths[0]
        TLS = file_paths[1]
        WEB = file_paths[2]

        duckdb_conn = duckdb.connect(":memory:")
        retrieved_visit_id = duckdb_conn.sql(f"""
    SELECT CAST(visitId AS VARCHAR) FROM '{WEB}' WHERE CAST(visitId AS VARCHAR) = '{visit_id}';
                                                        """).fetchall()
        
        if retrieved_visit_id:
            current_app.logger.info(f"retrieved visit id: {retrieved_visit_id[0][0]}")
        else:
            current_app.logger.info(f"visit id not found: {visit_id}")
            return {"error": "Visit ID not found"}
            
        if retrieved_visit_id[0][0] == visit_id:
            current_app.logger.info(f"found visit id: {retrieved_visit_id[0][0]}")

            try:

                json_data_array = duckdb_conn.sql(f"""
                WITH joined_tls_smtp_web AS (
                    SELECT * FROM '{TLS}' tl
                    INNER JOIN '{SMTP}' sm ON tl.visitRequest.visitId = sm.visitId
                    INNER JOIN '{WEB}' w ON sm.visitId = w.visitId
                    WHERE CAST(w.visitId AS VARCHAR) = '{visit_id}'
                )
                SELECT json(
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
                        'CrawlFinished', CrawlFinished,
                        'vatValues', vatValues,
                        'visitedUrls', visitedUrls,
                        'pageVisits', pageVisits,
                        'htmlFeatures', htmlFeatures
                    )
                ) AS result
                FROM joined_tls_smtp_web WHERE CAST(visitId AS VARCHAR) = '{visit_id}';""").fetchall()
                    

                current_app.logger.info(json_data_array)
                objects = []
                for i in json_data_array:
                    current_app.logger.info("here: " + i[0] + "\n" + "\n" + "\n" + "\n" + "\n" + "\n") 
                            
                    objects.append(json.loads(i[0]))
                            
                objects_dumps_data = json.dumps(objects, indent=2)
                        
                current_app.logger.info(objects_dumps_data)
                duckdb_conn.close()

                return objects
                

            except Exception as e:
                current_app.logger.error(f"Error reading Parquet file: {e}")
                traceback.print_exc()
                return {"error": str(e)}
    
        return {"error": "Visit ID not found"}
            
                

                
                
