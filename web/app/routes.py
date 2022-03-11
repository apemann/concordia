import os
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    a = str(os.environ.get('DATABASE_URL'))
    return a