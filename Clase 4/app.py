#-"- Coding: utf-8 -*-
#Caracteres especiales

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])

def unida():
    return 'Hola desde la Unida!'

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

''' 0.0.0.0 es una dirección IP especial que indica que el servidor Flask debe escuchar en todas las interfaces de red disponibles. Esto permite que la aplicación sea accesible desde cualquier dirección IP que pueda llegar al servidor, no solo desde localhost. Esto es útil para pruebas y desarrollo en entornos donde se necesita acceder a la aplicación desde otras máquinas o dispositivos en la misma red. '''


