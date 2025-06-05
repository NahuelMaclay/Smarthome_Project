
from auth import verify_admin
from base_de_datos import base_de_datos
from mensajes_consola import formatear_mensaje_consola



def nuevo_dispositivo():
    if(verify_admin()==False):
        formatear_mensaje_consola("No tiene permisos para realizar esta acción")
        return
    else:    
        formatear_mensaje_consola("--- Registro de Dispositivo ---")
        nombre = input("Ingrese Nombre del dispositivo: ").strip().lower()
        tipo = input("Tipo de dispositivo: ").strip().lower()
        ubicacion = input("Ubicación del dispositivo: ").strip().lower()
        nuevo_dispositivo = {
            'id':len(base_de_datos['dispositivos'])+1,
            'nombre': nombre,
            'tipo': tipo,
            'ubicacion': ubicacion,
            'estado': False,
        }
        base_de_datos['dispositivos'].append(nuevo_dispositivo)
        formatear_mensaje_consola(f"✅ Dispositivo {nombre} registrado con éxito.")




def listar_dispositivos():
    formatear_mensaje_consola("--- Lista de Dispositivos ---")
    if(len(base_de_datos['dispositivos'])==0):
        formatear_mensaje_consola("No hay dispositivos registrados")
    else:
        for dispositivo in base_de_datos['dispositivos']:
            formatear_mensaje_consola(f"id: {dispositivo['id']} ,Nombre: {dispositivo['nombre']}, Tipo: {dispositivo['tipo']}, Ubicación: {dispositivo['ubicacion']}, Estado: {dispositivo['estado']}")
    
    


def buscar_dispositivo():
    formatear_mensaje_consola("--- Buscar Dispositivo ---")
    nombre = input("Ingrese Nombre del dispositivo: ").strip().lower()
    for dispositivo in base_de_datos['dispositivos']:
        if nombre in dispositivo['nombre'] :
            print(f"id: {dispositivo['id']} ,Nombre: {dispositivo['nombre']}, Tipo: {dispositivo['tipo']}, Ubicación: {dispositivo['ubicacion']}, Estado: {dispositivo['estado']}")
            
            
        else :
            formatear_mensaje_consola(f"Dispositivo {nombre} no encontrado.")
        
        
def eliminar_dispositivo():
    if(verify_admin()==False):
        formatear_mensaje_consola("No tiene permisos para realizar esta acción")
        
        return
    else:
        formatear_mensaje_consola("--- Eliminar Dispositivo ---")
        nombre = input("Ingrese Nombre del dispositivo: ").strip()
        for dispositivo in base_de_datos['dispositivos']:
            if dispositivo['nombre'] == nombre:
                base_de_datos['dispositivos'].remove(dispositivo)
                formatear_mensaje_consola(f"Dispositivo {nombre} eliminado con éxito.")
            else:
                formatear_mensaje_consola(f"Dispositivo {nombre} no encontrado.")

