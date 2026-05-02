from flask import Flask, request, jsonify
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
DB = "usuarios.db"


# Inicializar base de datos

def init_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


init_db()


# Registro

@app.route("/registro", methods=["POST"])
def registro():
    data = request.json
    usuario = data.get("usuario")
    password = data.get("contraseña")

    if not usuario or not password:
        return jsonify({"Error": "Faltan datos"}), 400

    password_hash = generate_password_hash(password)

    try:
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO usuarios (usuario, password) VALUES (?, ?)",
            (usuario, password_hash)
        )

        conn.commit()
        conn.close()

        return jsonify({"Mensaje": "Usuario registrado correctamente"}), 201

    except sqlite3.IntegrityError:
        return jsonify({"Error": "El usuario ya existe"}), 400


# Login

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    usuario = data.get("usuario")
    password = data.get("contraseña")

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM usuarios WHERE usuario = ?", (usuario,))
    result = cursor.fetchone()

    conn.close()

    if result and check_password_hash(result[0], password):
        return jsonify({"Mensaje": "Login exitoso"}), 200
    else:
        return jsonify({"Error": "Credenciales inválidas"}), 401


# Tareas (simple)

@app.route("/tareas", methods=["GET"])
def tareas():
    return """
    <h1>Bienvenido al sistema de tareas</h1>
    <p>Login exitoso. Aquí podrías ver tus tareas.</p>
    """


if __name__ == "__main__":
    app.run(debug=True)