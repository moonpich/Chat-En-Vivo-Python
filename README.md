# 🚀 Chat Seguro en Python con SSL/TLS

Este es un proyecto de un chat en vivo multicliente, programado en Python, que utiliza la biblioteca `ssl` para asegurar toda la comunicación.

El chat implementa un **cifrado híbrido** (asimétrico para el *handshake* inicial y simétrico para los mensajes) para garantizar la confidencialidad, integridad y autenticidad de la conexión.

---

## 🛠️ Características

* **Chat Multicliente:** Múltiples usuarios pueden conectarse y chatear simultáneamente.
* **Seguridad SSL/TLS:** Toda la comunicación está cifrada.
    * **Cifrado Asimétrico (RSA):** Se usa para el *handshake* inicial y la negociación segura de la clave de sesión.
    * **Cifrado Simétrico (AES):** Se usa para cifrar todos los mensajes del chat una vez la conexión es segura.
* **Manejo de Apodos (Nicknames):** Cada usuario se identifica con un apodo único.
* **Notificaciones de Sistema:** Mensajes automáticos cuando un usuario se une o abandona el chat.
* **Multihilo (Threading):** El servidor usa hilos para manejar a cada cliente de forma independiente, y el cliente usa hilos para escuchar y escribir al mismo tiempo.

---

## 💻 Tecnologías Utilizadas

* **Python 3**
* **Módulo `socket`:** Para las conexiones de red base.
* **Módulo `threading`:** Para la concurrencia.
* **Módulo `ssl`:** Para "envolver" los sockets con cifrado.
* **OpenSSL:** Para la generación de los certificados (llave pública/privada).

---

## ⚙️ Instalación y Puesta en Marcha

Sigue estos pasos para ejecutar el proyecto en tu máquina local.

### 1. Prerrequisitos

* Tener **Python 3** instalado.
* Tener **OpenSSL** instalado (viene por defecto en Linux/macOS; en Windows puedes usar Git Bash o WSL).

### 2. Clonar el Repositorio

```bash
git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
cd TU_REPOSITORIO
