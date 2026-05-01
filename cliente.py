import requests

BASE_URL = "http://127.0.0.1:5000"


def registrar():
    usuario = input("Usuario: ")
    password = input("Contraseña: ")

    res = requests.post(
        f"{BASE_URL}/registro",
        json={"usuario": usuario, "contraseña": password}
    )

    print(res.json())


def login():
    usuario = input("Usuario: ")
    password = input("Contraseña: ")

    res = requests.post(
        f"{BASE_URL}/login",
        json={"usuario": usuario, "contraseña": password}
    )

    print(res.json())

    if res.status_code == 200:
        tareas()


def tareas():
    res = requests.get(f"{BASE_URL}/tareas")
    print(res.text)


def menu():
    while True:
        print("\n1. Registrarse")
        print("2. Login")
        print("3. Salir")

        opcion = input("Elegir opción: ")

        if opcion == "1":
            registrar()
        elif opcion == "2":
            login()
        elif opcion == "3":
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()