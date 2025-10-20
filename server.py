# server.py
import socket
import threading
import ssl  # 1. Importar SSL

HOST = '127.0.0.1'
PORT = 65432

clients = []
nicknames = []

def broadcast(message, _client=None):
    for client_socket in clients:
        if client_socket != _client:
            try:
                client_socket.send(message)
            except:
                remove_client(client_socket)

def handle_client(client_socket):
    while True:
        try:
            message_raw = client_socket.recv(1024)
            if not message_raw:
                remove_client(client_socket)
                break
            
            index = clients.index(client_socket)
            nickname = nicknames[index]
            
            formatted_message = f"{nickname}: {message_raw.decode('utf-8')}"
            
            broadcast(formatted_message.encode('utf-8'), client_socket)
        except:
            remove_client(client_socket)
            break

def remove_client(client_socket):
    if client_socket in clients:
        index = clients.index(client_socket)
        clients.remove(client_socket)
        client_socket.close() # Es buena idea cerrar el socket explícitamente
        
        nickname = nicknames[index]
        nicknames.remove(nickname)
        broadcast(f'¡{nickname} ha abandonado el chat!'.encode('utf-8'))

def receive_connections():
    # 2. Configurar el contexto SSL del servidor
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    # Creamos el socket principal del servidor (aún no es seguro)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Servidor seguro escuchando en {HOST}:{PORT}...")

    while True:
        print("Esperando nuevas conexiones...")
        # 3. Aceptamos la conexión normal
        client_socket_raw, address = server.accept()
        
        try:
            # 4. "Envolvemos" el socket con SSL
            client_socket = context.wrap_socket(client_socket_raw, server_side=True)
            print(f"¡Conexión SSL aceptada desde {str(address)}!")

            client_socket.send('NICK'.encode('utf-8'))
            nickname = client_socket.recv(1024).decode('utf-8')

            nicknames.append(nickname)
            clients.append(client_socket)

            print(f"El apodo del cliente es {nickname}")
            broadcast(f"¡{nickname} se ha unido al chat!".encode('utf-8'), client_socket)
            client_socket.send("¡Conectado al servidor seguro con éxito!".encode('utf-8'))

            thread = threading.Thread(target=handle_client, args=(client_socket,))
            thread.start()
        
        except ssl.SSLError as e:
            print(f"Error de SSL: {e}. La conexión fue rechazada.")
            client_socket_raw.close()
        except Exception as e:
            print(f"Error: {e}")
            client_socket_raw.close()


if __name__ == "__main__":
    receive_connections() # Solo llamamos a esta función, que ahora contiene el socket