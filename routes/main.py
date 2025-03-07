from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/sobre')
def sobre():
    return render_template('sobre.html')

@main_bp.route('/noticias')
def noticias():
    return render_template('noticias.html')
