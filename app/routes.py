from app import bp
from flask import jsonify


@bp.route("/index",method=["GET"])
def home():
    return jsonify(
        "hello world from blueprint"
    )
