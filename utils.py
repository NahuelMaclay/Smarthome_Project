# Funciones auxiliares (validaciones, menús, etc.)

#utils.py


def mostrar_menu_principal():
    print("\n--- SmartHome Solutions ---")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    return input("Elige una opción: ")

def mostrar_menu_principal_de_usuario_autenticado():
    print("\n--- SmartHome Solutions ---")
    print("1. Registrar nuevo dispositivo")
    print("2. Listar dispositivos")
    # print("3. Buscar dispositivo")
    print("3. Salir")
    return input("Elige una opción: ")