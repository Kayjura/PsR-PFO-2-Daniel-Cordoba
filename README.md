# Sistema de Gestión de Tareas - API Flask

Este proyecto implementa una API REST con autenticación básica y persistencia en base de datos SQLite.


## Tecnologías utilizadas

- Python
- Flask
- SQLite
- Requests (cliente)
- Werkzeug (hash de contraseñas)


## Requisitos previos

Antes de ejecutar el proyecto, asegurate de tener instalado:

* Python 3.x
* pip (gestor de paquetes)


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


## Registro de usuario

Elegir opción 1 e ingresar:

* Usuario
* Contraseña

Resultado esperado:

```
Usuario registrado correctamente
```


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
Bienvenido al sistema de tareas
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


## Flujo típico de uso

1. Ejecutar servidor
2. Ejecutar cliente
3. Registrar usuario
4. Iniciar sesión
5. Acceder a tareas


## Autor

Trabajo práctico - API Flask + SQLite
