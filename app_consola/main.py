
from dispositivos import buscar_dispositivo, eliminar_dispositivo, listar_dispositivos, nuevo_dispositivo
from menu import mostrar_opciones_principal_de_app
from automatizaciones import activar_automatizacion_luces_del_patio
import datetime
from auth import login, logout, register
from states import states
def main():
    print(f"----BIENVENIDO A SMART HOME SOLUTIONS----{datetime.datetime.now().strftime("%H:%M")}")
    activar_automatizacion_luces_del_patio()
    #  mostrar_opciones_principal_de_app()
    # if(states['is_auth']==False):
    #     print("1. Registrarse")
    #     print("2. Iniciar sesión")
    # else:
    #     print("3. Registrar nuevo dispositivo")
    #     print("4. Listar dispositivos")
    #     print("5. Buscar dispositivo")
    #     print("6. ELiminar un dispositivo")
    # print("0. Salir")
    while True:
        mostrar_opciones_principal_de_app()
        opcion=input('Ingrese una opcion: ')
        if opcion == '1':
            register()
        elif(opcion == '2'):
            login()
        if (states['is_auth']):
            if(opcion == '3'):
                nuevo_dispositivo()
            elif(opcion == '4'):
                listar_dispositivos()
            elif(opcion == '5'):
                buscar_dispositivo()
            elif(opcion == '6'):
                eliminar_dispositivo()
            elif(opcion == '0'):
             print("Gracias vuelva pronto")
             break
        elif(opcion == '0'):
             print("Gracias vuelva pronto")
             logout()
             break
       

if __name__ == "__main__":
    main()

