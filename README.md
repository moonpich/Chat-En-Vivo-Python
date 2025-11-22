# 🔒 ChatDev: Sistema de Gestión Segura de Documentos y Firmas

Este repositorio contiene la lógica backend de una aplicación enfocada en la **seguridad de documentos**, **firmas digitales** y la **simulación de almacenamiento** en la nube.

Utiliza Python para manejar la lógica del negocio, bases de datos para la persistencia de metadatos y criptografía para la gestión de claves y la integridad de la información.

---

## 🌟 Características Principales

* **Firma Digital (PKI):** Implementación de lógica de firma digital utilizando claves `.pem` y `.crt` almacenadas en el directorio `keys/`.
* **Gestión de Datos:** Manejo de metadatos de documentos y transacciones a través de `database.py`.
* **Simulación de Almacenamiento:** Directorio `GOOGLE_DRIVE_SIM/` para simular la persistencia de archivos subidos.
* **Verificación de Integridad:** Uso de hashes MD5 (`generate_md5.py`) para verificar que los archivos no han sido alterados.
* **Servicio Web:** Punto de entrada principal (`main.py`) para la interacción vía web (HTML/APIs).

---

## ⚙️ Instalación y Configuración

Sigue estos pasos para configurar y ejecutar el proyecto localmente.

### 1. Requisitos

Asegúrate de tener **Python 3.10+** instalado.

### 2. Clonar el Repositorio

```bash
git clone [https://docs.github.com/es/repositories/creating-and-managing-repositories/quickstart-for-repositories](https://docs.github.com/es/repositories/creating-and-managing-repositories/quickstart-for-repositories)
cd ChatDev
