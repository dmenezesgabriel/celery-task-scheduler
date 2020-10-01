from flask import Blueprint, jsonify

bp = Blueprint("api", __name__)


@bp.route("/hello")
def hello():
    return jsonify("Hello")
