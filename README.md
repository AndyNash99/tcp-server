# tcp-server
Servidor tcp simple escrito en Python

Para iniciar el servidor ejecutar el archivo server.py en una terminal.
Para iniciar el cliente ejecutar el archivo client.py en una terminal distinta al servidor.

PRUEBAS:

1. Mensaje genérico:
    - Iniciar servidor.
    - Iniciar cliente.
    - Escribir un mensaje del cliente al servidor (Ejemplo: hola mundo).
    - Respuesta esperada: el mensaje original en mayúsculas. (Ejemplo: HOLA MUNDO) se muestra en la interfaz del cliente.

2. Mensaje de desconexión:
    - Iniciar servidor.
    - Iniciar cliente.
    - Escribir DESCONEXION del cliente al servidor.
    - Respuesta esperada: se cierra la conexión entre cliente y servidor. Se cierra la interfaz de linea de comandos para el cliente. El servidor sigue funciionando y escuchando otras conexiones.

