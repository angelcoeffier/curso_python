from flask import Blueprint, Flask, request, jsonify

logout = Blueprint('Logout', __name__)

@logout.route('/logout', methods=['POST'])

def llamarServicioSet():
    user = request.json.get('user')
    password = request.json.get('password')

    print("Usuario enviado: ", user, ". Contraseña enviada: ", password)
