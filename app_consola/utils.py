from datetime import datetime
from base_de_datos import base_de_datos
def esta_en_rango_horario(hora_inicio, hora_fin):
    hora_actual = datetime.now().time()
    hora_inicio = datetime.strptime(hora_inicio, "%H:%M").time()
    hora_fin = datetime.strptime(hora_fin, "%H:%M").time()

    if hora_inicio < hora_fin: 
        return hora_inicio <= hora_actual <= hora_fin
    else:  
        return hora_actual >= hora_inicio or hora_actual <= hora_fin

def buscar_automatizacion_por_tipo(tipo):
    for automatizacion in base_de_datos['automatizaciones']:
        if automatizacion['tipo'] == tipo:
            return automatizacion
    return None

def buscar_automatizacion_por_nombre(nombre):
    for automatizacion in base_de_datos['automatizaciones']:
        if automatizacion['nombre'] == nombre:
            return automatizacion
    return None