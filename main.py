# Archivo principal (punto de entrada del programa)

# main.py


from auth import registrar_usuario, iniciar_sesion
from utils import monstras_menu_principal


def main():
    while true:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            usuario = iniciar_sesion()
            if usuario:
                print(f"Bienvenido, {usuario['nombre']} (Menú de usuario próximamente...)")
        elif opcion == "3":
            print("saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

# main.py

from auth import registrar_usuario, iniciar_sesion
from utils import mostrar_menu_principal, mostrar_menu_usuario
from devices import agregar_dispositivo, listar_dispositivos, buscar_dispositivo, eliminar_dispositivo

def main():
    while True:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            usuario = iniciar_sesion()
            if usuario:
                while True:
                    op = mostrar_menu_usuario()
                    if op == "1":
                        agregar_dispositivo(usuario)

