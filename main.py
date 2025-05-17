

from utils import listar_dispositivos,mostrar_menu_principal_de_dispositivo, nuevo_dispositivo,buscar_dispositivo,eliminar_dispositivo
import datetime

#menu principal
#1 nuevo dispositivo 
#2 listar dispositivos
#3 buscar dispositivo
# 0 volver al menu prinpal
#
#
#
def main():
    print(f"----BIENVENIDO A SMART HOME SOLUTIONS----{datetime.datetime.now().strftime("%H:%M")}")
    hora=datetime.datetime.now().strftime("%H")
    if(int(hora)>=20):
        print("AUTOMATIZACION DE LUCES ACTIVADA")
    elif(int(hora)<=20):
        print("AUTOMATIZACION DE LUCES DESACTIVADA")
    while True:
       
       mostrar_menu_principal_de_dispositivo()
       opcion = input("Seleccione una opción: ")
       if(opcion=="1"):
        print("Elegiste opcion 1 . NUEVO DISPOSITIVO")
        nuevo_dispositivo()
       elif (opcion=="2"):
        print("Elegiste opcion 2. LISTAR DISPOSITIVOS")
        listar_dispositivos()
       elif (opcion=="3"):
        print("Elegiste opcion 3 . BUSCAR DISPOSITIVO")
        buscar_dispositivo()
       elif (opcion=="4"):
        print("Elegiste opcion 4 . ELIMINAR DISPOSITIVO")
        eliminar_dispositivo()
       elif (opcion=="5"):
        print("GRACIAS VUELVA PRONTO!!")
        break
       

if __name__ == "__main__":
    main()

