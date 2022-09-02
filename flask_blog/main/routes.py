from flask import render_template, Blueprint
from flask_blog.models import User

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    return render_template('index.html')


@main.route('/contacts')
def contacts():
    return render_template('contact.html')
