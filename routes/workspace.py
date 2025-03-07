from flask import Blueprint, render_template, session, redirect, url_for

workspace_bp = Blueprint('workspace', __name__)

@workspace_bp.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('workspace.workspace'))
    return redirect(url_for('auth.login'))  # Garante que o login seja a primeira tela

@workspace_bp.route('/workspace')
def workspace():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    return render_template('workspace.html')