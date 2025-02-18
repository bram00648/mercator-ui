import os

class Config:
    """Configuration settings for Flask app."""
    DEBUG = os.getenv("FLASK_DEBUG", True) 

    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
    PARQUET_FILE_PATH = os.getenv("PARQUET_FILE_PATH", os.path.join(BASE_DIR, "data/technology_analyzer_web_crawl_result.parquet"))

    S3_BUCKET = os.getenv("S3_BUCKET", None)  # If using S3
