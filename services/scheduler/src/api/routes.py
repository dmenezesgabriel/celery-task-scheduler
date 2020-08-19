from flask import Blueprint, jsonify
from tasks.print_arg_task import print_arg


bp = Blueprint('api', __name__)


@bp.route('/hello')
def hit_print_arg():
    print_arg('hello')
    return jsonify('printing hello')
