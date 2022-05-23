from flask import Blueprint
import json

api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/api')
def index():
    
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.com'})