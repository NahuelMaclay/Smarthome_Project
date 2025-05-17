
from states import usuario



def mostrar_menu_principal_de_dispositivo():
    print("\n--- SmartHome Solutions ---")
    print("1. Registrar nuevo dispositivo")
    print("2. Listar dispositivos")
    print("3. Buscar dispositivo")
    print("4. ELiminar un dispositivo")
    print("5. Salir")

def nuevo_dispositivo():
    print("\n--- Registro de Dispositivo ---")
    nombre = input("Ingrese Nombre del dispositivo: ").strip()
    tipo = input("Tipo de dispositivo: ").strip()
    ubicacion = input("Ubicación del dispositivo: ").strip()
    nuevo_dispositivo = {
        'id':len(usuario['dispositivos'])+1,
        'nombre': nombre,
        'tipo': tipo,
        'ubicacion': ubicacion,
        'estado': False,


    }
    usuario['dispositivos'].append(nuevo_dispositivo)

    print(f"✅ Dispositivo {nombre} registrado con éxito.")

def listar_dispositivos():
    print("\n--- Lista de Dispositivos ---")
    if(len(usuario['dispositivos'])==0):
        print("No hay dispositivos registrados")
    else:
        for dispositivo in usuario['dispositivos']:
            print(f"id: {dispositivo['id']} ,Nombre: {dispositivo['nombre']}, Tipo: {dispositivo['tipo']}, Ubicación: {dispositivo['ubicacion']}, Estado: {dispositivo['estado']}")



def buscar_dispositivo():
    print("\n--- Buscar Dispositivo ---")
    nombre = input("Ingrese Nombre del dispositivo: ").strip()
    for dispositivo in usuario['dispositivos']:
        if dispositivo['nombre'] == nombre:
            print(f"id: {dispositivo['id']} ,Nombre: {dispositivo['nombre']}, Tipo: {dispositivo['tipo']}, Ubicación: {dispositivo['ubicacion']}, Estado: {dispositivo['estado']}")
        
def eliminar_dispositivo():
    print("\n--- Eliminar Dispositivo ---")
    nombre = input("Ingrese Nombre del dispositivo: ").strip()
    for dispositivo in usuario['dispositivos']:
        if dispositivo['nombre'] == nombre:
            usuario['dispositivos'].remove(dispositivo)
            print(f"Dispositivo {nombre} eliminado con éxito.")
        else:
            print(f"Dispositivo {nombre} no encontrado.")