from flask import Blueprint, render_template, session, redirect, url_for
from extensions import db
from models.user import User
from models.device import IoTDevice

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
def admin_dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    user = User.query.get(session['user_id'])
    if not user.is_admin:
        return redirect(url_for('devices.index'))
    users = User.query.all()
    devices = IoTDevice.query.all()
    return render_template('admin.html', users=users, devices=devices)