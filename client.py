# client.py
import socket
import threading
import ssl  # 1. Importar SSL

NICKNAME = input("Elige tu apodo: ")

# 2. Configurar el contexto SSL del cliente
context = ssl.create_default_context()
# ¡¡ADVERTENCIA!! Esto es necesario para un cert autofirmado
# En un entorno real, NUNCA harías esto.
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

HOST = '127.0.0.1'
PORT = 65432

# 3. Creamos el socket normal
client_raw = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 4. "Envolvemos" el socket con SSL ANTES de conectarnos
# server_hostname debe coincidir con el "Common Name" que pusiste en el cert
client = context.wrap_socket(client_raw, server_hostname=HOST)

try:
    # 5. Nos conectamos con el socket seguro
    client.connect((HOST, PORT))
except ConnectionRefusedError:
    print("Error: No se pudo conectar. Asegúrate de que el servidor esté encendido.")
    exit()
except ssl.SSLError as e:
    print(f"Error de SSL al conectar: {e}")
    print("Asegúrate de que el servidor esté usando un certificado válido.")
    exit()

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(NICKNAME.encode('utf-8'))
            else:
                print(message)
        except:
            print("¡Se ha perdido la conexión con el servidor!")
            client.close()
            break

def write_messages():
    while True:
        message = input("")
        try:
            client.send(message.encode('utf-8'))
        except:
            print("Error al enviar el mensaje.")
            break

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_thread = threading.Thread(target=write_messages)
write_thread.start()