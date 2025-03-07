from models.device import Device
from flask import Blueprint, render_template, redirect, url_for, request, session
from extensions import db


devices_bp = Blueprint('devices', __name__)


# @devices_bp.route('/devices')
# def list_devices():
#     if 'user_id' not in session:
#         return redirect(url_for('auth.login'))
#     return render_template('devices/list.html')

# @devices_bp.route('/devices/add', methods=['GET', 'POST'])
# def add_device():
#     if 'user_id' not in session:
#         return redirect(url_for('auth.login'))
#     if request.method == 'POST':
#         # Lógica para adicionar dispositivo
#         return redirect(url_for('devices.list_devices'))
#     return render_template('devices/add.html')

# @devices_bp.route('/devices/delete', methods=['GET', 'POST'])
# def delete_device():
#     if 'user_id' not in session:
#         return redirect(url_for('auth.login'))
#     if request.method == 'POST':
#         # Lógica para deletar dispositivo
#         return redirect(url_for('devices.list_devices'))
#     return render_template('devices/delete.html')

# @devices_bp.route('/devices/edit', methods=['GET', 'POST'])
# def edit_device():
#     if 'user_id' not in session:
#         return redirect(url_for('auth.login'))
#     if request.method == 'POST':
#         # Lógica para editar dispositivo
#         return redirect(url_for('devices.list_devices'))
#     return render_template('devices/edit.html')

@devices_bp.route('/devices', methods=['GET'])
def list_devices():
    devices = Device.query.all()
    return render_template('devices/devices.html', devices=devices)

@devices_bp.route('/devices/add', methods=['GET', 'POST'])
def add_device():
    if request.method == 'POST':
        name = request.form['name']
        new_device = Device(name=name)
        db.session.add(new_device)
        db.session.commit()
        return redirect(url_for('devices.list_devices'))
    return render_template('devices/add_device.html')


@devices_bp.route('/devices/edit/<int:device_id>', methods=['GET', 'POST'])
def edit_device(device_id):
    device = Device.query.get(device_id)
    if request.method == 'POST':
        device.name = request.form['name']
        db.session.commit() # type: ignore
        return redirect(url_for('devices.list_devices'))
    return render_template('devices/edit_device.html', device=device)

@devices_bp.route('/devices/delete/<int:device_id>', methods=['POST', 'GET'])
def delete_device(device_id):
    device = Device.query.get(device_id)
    if device:
        db.session.delete(device)
        db.session.commit()
    return redirect(url_for('devices.list_devices'))
