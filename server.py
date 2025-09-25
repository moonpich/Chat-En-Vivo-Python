# 1. Importar las "herramientas" necesarias
import socket  # La herramienta principal para crear las conexiones de red (sockets)
import threading # La herramienta para contratar "empleados" (hilos) que atiendan a cada cliente

# 2. Configuración inicial
HOST = '127.0.0.1'  # La dirección IP de esta misma computadora
PORT = 65432        # El número de la oficina a la que se conectarán

# 3. Listas para llevar un registro de quién está conectado
clients = []      # La lista de conexiones de los clientes (los "cables" conectados)
nicknames = []    # La lista de apodos de los clientes, en el mismo orden

# 4. Función "El Pregonero": Envía un mensaje a todos
def broadcast(message, _client=None):
    # Recorre cada "cable" de cliente que tenemos conectado
    for client_socket in clients:
        # Si el cliente no es el que originalmente envió el mensaje...
        if client_socket != _client:
            try:
                # ...le enviamos el mensaje.
                client_socket.send(message)
            except:
                # Si falla (ej: el cliente se desconectó de golpe), lo eliminamos.
                remove_client(client_socket)

# 5. Función "El Empleado Dedicado": Atiende a un solo cliente
def handle_client(client_socket):
    # Este bucle se ejecuta infinitamente mientras el cliente esté conectado
    while True:
        try:
            # Espera y recibe un mensaje del cliente (hasta 1024 bytes)
            message = client_socket.recv(1024)
            # Si el mensaje está vacío, el cliente se desconectó
            if not message:
                remove_client(client_socket)
                break
            # Llama al "pregonero" para que envíe el mensaje a todos los demás
            broadcast(message, client_socket)
        except:
            # Si hay algún error, significa que el cliente se desconectó.
            remove_client(client_socket)
            break

# 6. Función para eliminar a un cliente que se ha ido
def remove_client(client_socket):
    if client_socket in clients:
        # Busca la posición del cliente en la lista
        index = clients.index(client_socket)
        # Elimina su "cable" de la lista de clientes
        clients.remove(client_socket)
        # Usa la misma posición para encontrar y eliminar su apodo
        nickname = nicknames[index]
        nicknames.remove(nickname)
        # Avisa a todos los demás que este usuario se ha ido
        broadcast(f'¡{nickname} ha abandonado el chat!'.encode('utf-8'))

# 7. Función "El Recepcionista": Acepta nuevas conexiones
def receive_connections():
    # Este bucle se ejecuta infinitamente para aceptar siempre nuevos clientes
    while True:
        print("Esperando nuevas conexiones...")
        # El programa se detiene aquí hasta que alguien intenta conectarse
        client_socket, address = server.accept()
        print(f"¡Conexión aceptada desde {str(address)}!")

        # Le pedimos al nuevo cliente su apodo
        client_socket.send('NICK'.encode('utf-8'))
        nickname = client_socket.recv(1024).decode('utf-8')

        # Guardamos al nuevo cliente en nuestras listas
        nicknames.append(nickname)
        clients.append(client_socket)

        # Imprimimos en la consola del servidor quién se unió
        print(f"El apodo del cliente es {nickname}")
        # Avisamos a todos los demás que alguien nuevo ha llegado
        broadcast(f"¡{nickname} se ha unido al chat!".encode('utf-8'), client_socket)
        # Le damos la bienvenida al nuevo cliente
        client_socket.send("¡Conectado al servidor con éxito!".encode('utf-8'))

        # Ahora, creamos un "empleado" (hilo) para que atienda exclusivamente a este cliente
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start() # El empleado empieza a trabajar

# 8. El "Interruptor Principal" para encender el servidor
if __name__ == "__main__":
    # Creamos el socket principal del servidor
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Le asignamos la dirección y el puerto que definimos
    server.bind((HOST, PORT))
    # Ponemos al servidor en modo "escucha", listo para recibir conexiones
    server.listen()
    print(f"Servidor escuchando en {HOST}:{PORT}...")
    # Llamamos al "recepcionista" para que empiece a aceptar clientes
    receive_connections()