import os.path
import yaml
from flask import render_template, request, Blueprint, flash, redirect, url_for

main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
@main.route("/home", methods=['GET', 'POST'])
def home():
    path = os.path.dirname(__file__)
    filename = os.path.join(path, 'messages.yml')
    with open(filename) as file:
        messages = yaml.full_load(file)

    return render_template('home.html', messages=messages)
