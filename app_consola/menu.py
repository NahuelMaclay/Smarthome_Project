from mensajes_consola import formatear_mensaje_consola
from automatizaciones import cambiar_estado_automatizacion_aspiradora, cambiar_estado_automatizacion_luces_del_patio, iniciar_automatizacion_luces_del_patio
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
        print("7. Cerrar sesión")
        print("8. Consultar Perfil")
        print("9. Cambiar Rol")
        print("10. Activar/desactivar automatizaciones")
        print("11. Listar Usuarios")
        print("12. Consultar automatizaciones activas")
    print("0. Salir")


def menu_automatizaciones():
    while True:
        print("1. Activar/desactivar automatizacion de luces del patio")
        print("2. Activar/desactivar aspiradora salon")
        print("0. Salir de automatizaciones")
        opcion2 = input("Ingrese una opcion: ")
        
        if(opcion2 == '1'):
            cambiar_estado_automatizacion_luces_del_patio()
        elif(opcion2 == '2'):
            cambiar_estado_automatizacion_aspiradora()
        elif(opcion2 == '0'):
            formatear_mensaje_consola("Saliste del menu automatizaciones")
            break