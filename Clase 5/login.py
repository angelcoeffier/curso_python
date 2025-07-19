from flask import Blueprint, Flask, request, jsonify

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])

def llamarServicioSet():
    user = request.json.get('user')
    password = request.json.get('password')
    print("Usuario enviado: ", user, ". Contraseña enviada: ", password)

    codRes, menRes, accion, rol = inicializarVariables(user, password)

    salida = {
        "codRes": codRes,
        "menRes": menRes,
        "accion": accion,
        "rol": rol
    }

    return jsonify(salida)

def inicializarVariables(user, password):
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    accion = 'Login exitoso'
    rol = 'Admin'
    userLocal = 'Angel'
    passLocal = 'Unida123'

    try:
        if user == userLocal and password == passLocal:
            print("Login exitoso")
            accion = 'Login exitoso'
        else:
            codRes = 'ERROR'
            menRes = 'Usuario o contraseña incorrectos'
            accion = 'Login fallido'
            rol = 'N/A'
            user = 'N/A'

    except Exception as e:
        print("Error en el login: ", e)
        codRes = 'ERROR'
        menRes = 'Msg: ' + str(e)
        accion = 'Error en el login'
        rol = 'N/A'
        user = 'N/A'

        return codRes, menRes, accion, rol, user
    return codRes, menRes, accion, rol