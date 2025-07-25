from flask import Blueprint, Flask, jsonify, request

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['POST'])

def llamarCliente():
    
    ci_cliente = request.json.get('ci')
    print('Cedula del cliente: ' + ci_cliente)

    codRes, menRes, accion, nombre, apellido = inicializarVariables(ci_cliente)

    if codRes == 'SIN_ERROR':
        salida = {
            'accion':accion,
            'codRes':codRes,
            'menRes':menRes,
            'ci':ci_cliente,
            'Nombre':nombre,
            'Apellido':apellido
        }
    elif codRes == 'ERROR_CONEXION':
        salida = {
            'codRes':codRes,
            'menRes':menRes,
            'accion':accion
        }
    elif codRes == 'ERROR':
        salida = {
            'codRes':codRes,
            'menRes':menRes,
            'accion':accion
        }

    return jsonify(salida)

def inicializarVariables(ci_cliente):
    try:
        if ci_cliente == '4862365':
            print('Cedula ingresada correcta: ' + ci_cliente)
            codRes = 'SIN_ERROR'
            menRes = 'Cedula correcta'
            accion = 'Success'
            nombre = 'Angel'
            apellido = 'Coeffier'
            return codRes, menRes, accion, nombre, apellido
        else:
            print('Cedula ingresada es incorrecta.')
            codRes = 'ERROR'
            menRes = 'Cedula incorrecta'
            accion = 'Acceso denegado'
            nombre = 'N/A'
            apellido = 'N/A'
            return codRes, menRes, accion, nombre, apellido
    except Exception as e:
        print('Error en la conexión: ' + e)
        codRes = 'ERROR_CONEXION'
        menRes = 'Error de conexión'
        accion = 'Acceso denegado'
        nombre = 'N/A'
        apellido = 'N/A'
    
    return codRes, menRes, accion, nombre, apellido