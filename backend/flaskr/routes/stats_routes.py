from flask import Blueprint, jsonify, request
from flaskr.models.parquet_reader import ParquetReader

stats_bp = Blueprint("stats", __name__)

@stats_bp.route("/", methods=["GET"])
def get_parquet_data():
    """Endpoint to get data from the Parquet file."""
    data = ParquetReader.read_all_data_parquet()
    return jsonify(data)


@stats_bp.route("/get_stats_by_domain_name", methods=["GET"])
def get_stats_by_domain_name():
    """Endpoint to get data from the Parquet file by domain name."""
    domain_name = request.args.get("domain_name")
    data = ParquetReader.read_parquet_data_by_domain_name(domain_name)
    return jsonify(data)
