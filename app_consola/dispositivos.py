
from auth import verify_admin
from base_de_datos import base_de_datos





def nuevo_dispositivo():
    if(verify_admin()==False):
        print("No tiene permisos para realizar esta acción")
        return
    else:    
        print("\n--- Registro de Dispositivo ---")
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
        print(f"✅ Dispositivo {nombre} registrado con éxito.")




def listar_dispositivos():
    print("\n--- Lista de Dispositivos ---")
    if(len(base_de_datos['dispositivos'])==0):
        print("No hay dispositivos registrados")
    else:
        for dispositivo in base_de_datos['dispositivos']:
            print(f"id: {dispositivo['id']} ,Nombre: {dispositivo['nombre']}, Tipo: {dispositivo['tipo']}, Ubicación: {dispositivo['ubicacion']}, Estado: {dispositivo['estado']}")
    print('\n--------------')
    


def buscar_dispositivo():
    print("\n--- Buscar Dispositivo ---")
    nombre = input("Ingrese Nombre del dispositivo: ").strip().lower()
    for dispositivo in base_de_datos['dispositivos']:
        if nombre in dispositivo['nombre'] :
            print(f"id: {dispositivo['id']} ,Nombre: {dispositivo['nombre']}, Tipo: {dispositivo['tipo']}, Ubicación: {dispositivo['ubicacion']}, Estado: {dispositivo['estado']}")
            
            print('\n--------------')
        else :
            print(f"Dispositivo {nombre} no encontrado.")
            print('\n--------------')
        
def eliminar_dispositivo():
    if(verify_admin()==False):
        print("No tiene permisos para realizar esta acción")
        print('\n--------------')
        return
    else:
        print("\n--- Eliminar Dispositivo ---")
        nombre = input("Ingrese Nombre del dispositivo: ").strip()
        for dispositivo in base_de_datos['dispositivos']:
            if dispositivo['nombre'] == nombre:
                base_de_datos['dispositivos'].remove(dispositivo)
                print(f"Dispositivo {nombre} eliminado con éxito.")
            else:
                print(f"Dispositivo {nombre} no encontrado.")

