from flask import Blueprint, jsonify
from flaskr.models.parquet_reader import ParquetReader

stats_bp = Blueprint("stats", __name__)

@stats_bp.route("/", methods=["GET"])
def get_parquet_data():
    """Endpoint to get data from the Parquet file."""
    data = ParquetReader.read_parquet()
    return jsonify(data)
