=========================================
      PROYECTO: CHAT SEGURO CON SSL/TLS
=========================================

Este proyecto implementa un chat simple cliente-servidor en Python
que utiliza el protocolo SSL/TLS para asegurar toda la comunicación.

---------------------
TECNOLOGÍAS
---------------------
* Python 3
* Módulo `socket` para conexiones de red.
* Módulo `threading` para concurrencia.
* Módulo `ssl` para cifrado (Capa de Sockets Seguros).
* OpenSSL para la generación de certificados.

---------------------
CARACTERÍSTICAS
---------------------
* Múltiples clientes pueden conectarse simultáneamente.
* Notificaciones de conexión y desconexión de usuarios.
* Cifrado híbrido (Asimétrico para handshake, Simétrico para mensajes).
* Verificación de integridad de mensajes (incluida en SSL).

---------------------
INSTALACIÓN Y EJECUCIÓN
---------------------

1.  **Clonar el repositorio:**
    git clone [URL-DE-TU-REPO]
    cd chatEnVivo

2.  **Generar Certificados SSL (Autofirmados):**
    Antes de iniciar el servidor, debes generar los archivos `cert.pem` y `key.pem`.
    
    (Asegúrate de tener OpenSSL instalado)
    
    openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout key.pem
    
    NOTA: Cuando pregunte por "Common Name", escribe: 127.0.0.1

3.  **Configurar `.gitignore`:**
    Asegúrate de que tu archivo `.gitignore` contenga la línea:
    *.pem
    
    (Esto es CRUCIAL para no subir tu llave privada al repositorio).

4.  **Ejecutar el Servidor:**
    En una terminal, ejecuta:
    python server.py
    
    (Deberías ver "Servidor seguro escuchando en 127.0.0.1:65432...")

5.  **Ejecutar el Cliente:**
    En otra terminal (o varias), ejecuta:
    python client.py
    
    (Te pedirá un apodo y luego te conectarás de forma segura).