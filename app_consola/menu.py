from states import states
def mostrar_opciones_principal_de_app():
    if(states['is_auth']==False):
        print("1. Registrarse")
        print("2. Iniciar sesión")
    else:
        print("3. Registrar nuevo dispositivo")
        print("4. Listar dispositivos")
        print("5. Buscar dispositivo")
        print("6. ELiminar un dispositivo")
    print("0. Salir")