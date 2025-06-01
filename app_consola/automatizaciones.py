import datetime
from base_de_datos import base_de_datos
def activar_automatizacion_luces_del_patio():
    hora=datetime.datetime.now().strftime("%H")
    if(int(hora)>=20 or int(hora)<=6):
        for dispositivo in base_de_datos['dispositivos']:
            if dispositivo['tipo'] == "iluminación" and dispositivo['ubicacion'] == "patio":
                dispositivo['estado'] = True
                print(f"Dispositivo {dispositivo['nombre']},estado actual {dispositivo['estado']} activado")
            else:
                print(f'no se encontraron dispositivos de iluminacion en el patio')
        
    else:
        for dispositivo in base_de_datos['dispositivos']:
            if dispositivo['tipo'] and dispositivo['ubicacion'] == "Patio":
                dispositivo['estado'] = False
                print(f"Dispositivo {dispositivo['nombre']}, estado actual {dispositivo['estado']} desactivado")
            else:
                print(f'no se encontraron dispositivos de iluminacion en el patio')
        
