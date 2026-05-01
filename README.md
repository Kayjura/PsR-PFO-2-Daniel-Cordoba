# Sistema de Gestión de Tareas - API Flask

Este proyecto implementa una API REST con autenticación básica y persistencia en base de datos SQLite.

---

## Tecnologías utilizadas

- Python
- Flask
- SQLite
- Requests (cliente)
- Werkzeug (hash de contraseñas)

---

## Requisitos previos

Antes de ejecutar el proyecto, asegurate de tener instalado:

* Python 3.x
* pip (gestor de paquetes)

---

## Instalación

1. Clonar el repositorio o descargar los archivos

2. Crear entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
```

Activar entorno virtual:

* Windows:

```bash
venv\Scripts\activate
```

* Linux/Mac:

```bash
source venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install flask requests werkzeug
```

---

## Ejecución del proyecto

## 1. Iniciar el servidor

En una terminal:

```bash
python servidor.py
```

El servidor se ejecutará en:

```
http://127.0.0.1:5000
```

## 2. Ejecutar el cliente

En otra terminal (sin cerrar el servidor):

```bash
python cliente.py
```

##  Uso del sistema

Al ejecutar el cliente, verás un menú:

```
1. Registrarse
2. Login
3. Salir
```

---

## Registro de usuario

Elegir opción 1 e ingresar:

* Usuario
* Contraseña

Resultado esperado:

```
Usuario registrado correctamente
```
---

## Login

Elegir opción 2 e ingresar credenciales.

Si son correctas:

```
Login exitoso
```

Luego se mostrará la página de tareas.

---

## Visualización de tareas

Después del login, el sistema mostrará:

```
¡ACCESO CORRECTO! Bienvenido al sistema de tareas
```

(Actualmente es una vista HTML simple de prueba)

---

## Endpoints disponibles

## POST /registro

Registra un nuevo usuario

```json
{
  "usuario": "nombre",
  "contraseña": "1234"
}
```

## POST /login

Autentica un usuario

```json
{
  "usuario": "nombre",
  "contraseña": "1234"
}
```
---

## GET /tareas

Devuelve una página HTML de bienvenida.

---

## Posibles errores comunes

* "El usuario ya existe" → intentar con otro nombre
* "Credenciales inválidas" → revisar usuario/contraseña
* Error de conexión → verificar que el servidor esté corriendo

---

## Estructura del proyecto

```
/proyecto
│
├── servidor.py
├── cliente.py
├── usuarios.db (se crea automáticamente)
└── README.md
```

## Notas importantes

* Las contraseñas se almacenan de forma segura (hasheadas)
* La base de datos se crea automáticamente al ejecutar el servidor
* No es necesario instalar SQLite manualmente

---

## Flujo típico de uso

1. Ejecutar servidor
2. Ejecutar cliente
3. Registrar usuario
4. Iniciar sesión
5. Acceder a tareas

---

## Capturas de pruebas

## Inicializaciones de cliente.py y servidor.py

<img width="886" height="206" alt="image" src="https://github.com/user-attachments/assets/fda79357-3a7f-4d78-89a9-a7a0ac0cd2ea" />
<img width="886" height="331" alt="image" src="https://github.com/user-attachments/assets/9a6d6a2b-dfda-498c-9218-a3a966de005c" />


## Pruebas en terminal cliente.py

Registro incompleto y registro completo:
<img width="886" height="451" alt="image" src="https://github.com/user-attachments/assets/27a5115a-7db4-4a34-94ea-a33a0ca5d8f4" />

Ingreso incorrecto (sin clave), ingreso correcto e ingreso incorrecto (clave errónea):
<img width="656" height="739" alt="image" src="https://github.com/user-attachments/assets/9377abc8-583f-4158-9766-ab85fd3f839f" />


## Terminal servidor.py
<img width="886" height="448" alt="image" src="https://github.com/user-attachments/assets/900e3ee9-2d92-4ef5-9bf2-6f9cc8a12cb9" />

---

## Respuesta conceptual: ¿Por qué hashear contraseñas?

Las contraseñas se hashean para proteger la información del usuario. Si la base de datos es comprometida, las contraseñas no quedan expuestas en texto plano.
El hash es irreversible, lo que significa que no se puede recuperar la contraseña original. Esto aumenta significativamente la seguridad del sistema.

---

## Ventajas de usar SQLite en este proyecto
•	No requiere instalación de servidor 
•	Es liviano y fácil de usar 
•	Ideal para proyectos pequeños o educativos 
•	Permite persistencia real de datos 
•	Se integra fácilmente con Python

---

## Información académica

**Instituto de Formación Técnica Superior N° 29**  
Tecnicatura Superior en Desarrollo de Software - Daniel Cordoba - 3°A - 
**Año 2026**
