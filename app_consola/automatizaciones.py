import datetime
from utils import buscar_automatizacion_por_nombre, esta_en_rango_horario
from base_de_datos import base_de_datos
from mensajes_consola import formatear_mensaje_consola
def iniciar_automatizacion_luces_del_patio():
    automatizacion=buscar_automatizacion_por_nombre("Activar luces del Patio")
    if(automatizacion["estado"]=="inactivo"):
        formatear_mensaje_consola("La automatizacion de luces del patio esta inactiva")
        return
    automatizacion_hora_inicio=automatizacion['hora_inicio']
    automatizacion_hora_fin=automatizacion['hora_fin']
    if(esta_en_rango_horario(automatizacion_hora_inicio,automatizacion_hora_fin)):
        for dispositivo in base_de_datos['dispositivos']:
            if automatizacion['tipo'] == "iluminación" and dispositivo['ubicacion'] == "patio":
                dispositivo['estado'] = True
                formatear_mensaje_consola("Luces del patio activada")
        
            
        
    else:
        for dispositivo in base_de_datos['dispositivos']:
            if automatizacion['tipo']=="iluminación" and dispositivo['ubicacion'] == "patio":
                dispositivo['estado'] = False
                formatear_mensaje_consola(f"Dispositivo {dispositivo['nombre']}, estado actual {dispositivo['estado']} desactivado")
            
        

def cambiar_estado_automatizacion_luces_del_patio():
    automatizacion=buscar_automatizacion_por_nombre("Activar luces del Patio")
    if(automatizacion["estado"]=="activo"):
        automatizacion["estado"]="inactivo"
        formatear_mensaje_consola("La automatizacion de luces del patio esta inactiva")
    else:
        automatizacion["estado"]="activo"
        formatear_mensaje_consola("La automatizacion de luces del patio esta activa")
    
    
def cambiar_estado_automatizacion_aspiradora():
    automatizacion=buscar_automatizacion_por_nombre("activador/desactivador aspiradora")
    if(automatizacion["estado"]=="activo"):
        automatizacion["estado"]="inactivo"
        formatear_mensaje_consola("La automatizacion de aspiradora esta inactiva")
    else:
        automatizacion["estado"]="activo"
        formatear_mensaje_consola("La automatizacion de aspiradora esta activa")

def iniciar_automatizacion_aspiradora():
    automatizacion=buscar_automatizacion_por_nombre("activador/desactivador aspiradora")
    if(automatizacion["estado"]=="inactivo"):
        formatear_mensaje_consola("La automatizacion de aspiradora esta inactiva")
        return
    automatizacion_hora_inicio=automatizacion['hora_inicio']
    automatizacion_hora_fin=automatizacion['hora_fin'] 
    if(esta_en_rango_horario(automatizacion_hora_inicio,automatizacion_hora_fin)):
        for dispositivo in base_de_datos['dispositivos']:
            if automatizacion['tipo'] == "aspiradora" and dispositivo['ubicacion'] == "comedor":
                dispositivo['estado'] = True
                formatear_mensaje_consola("Aspiradora activada")
    else:
        for dispositivo in base_de_datos['dispositivos']:
            if automatizacion['tipo'] == "aspiradora" and dispositivo['ubicacion'] == "comedor":
                dispositivo['estado'] = False
                formatear_mensaje_consola("Aspiradora desactivada")
            
def consultar_automatizaciones_activas():
    for automatizacion in base_de_datos['automatizaciones']:
        if(automatizacion['estado']=="activo"):
            formatear_mensaje_consola(f"Automatizacion {automatizacion['nombre']} esta activa")
        else:
            formatear_mensaje_consola(f"Automatizacion {automatizacion['nombre']} esta inactiva")