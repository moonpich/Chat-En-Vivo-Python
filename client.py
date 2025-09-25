import socket  # Herramienta para crear la conexión
import threading # Herramienta para hacer dos cosas a la vez: escuchar y escribir

# 1. Pedimos al usuario que elija un apodo antes de conectarse
NICKNAME = input("Elige tu apodo: ")

# 2. Creamos el socket del cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Intentamos conectarnos a la "dirección de la oficina de correos"
try:
    client.connect(('127.0.0.1', 65432))
except ConnectionRefusedError:
    print("Error: No se pudo conectar. Asegúrate de que el servidor esté encendido.")
    exit()

# 3. Función "El Oído": Se dedica solo a escuchar mensajes del servidor
def receive_messages():
    while True:
        try:
            # Espera a recibir un mensaje del servidor
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                # Si el servidor nos pide el apodo, se lo enviamos
                client.send(NICKNAME.encode('utf-8'))
            else:
                # Si es un mensaje normal, lo imprimimos en la pantalla
                print(message)
        except:
            # Si hay un error, es que nos desconectamos del servidor
            print("¡Se ha perdido la conexión con el servidor!")
            client.close()
            break

# 4. Función "La Boca": Se dedica solo a enviar los mensajes que escribimos
def write_messages():
    while True:
        # Espera a que el usuario escriba algo y presione Enter
        message = f'{NICKNAME}: {input("")}'
        try:
            # Envía el mensaje formateado al servidor
            client.send(message.encode('utf-8'))
        except:
            # Si falla el envío, salimos del bucle
            print("Error al enviar el mensaje.")
            break

# 5. Creamos y encendemos los dos "empleados" (hilos) del cliente
# Uno para escuchar y otro para escribir. Así podemos hacer ambas cosas a la vez.

# Creamos el hilo "Oído"
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start() # El oído empieza a escuchar

# Creamos el hilo "Boca"
write_thread = threading.Thread(target=write_messages)
write_thread.start() # La boca está lista para que escribas