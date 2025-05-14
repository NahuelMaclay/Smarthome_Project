# Gestión de dispositivos (agregar, listar, buscar, eliminar)

# devices.py


def agregar_dispositivo(usuario):
    print("\n--- Agregar Dispositivo ---")
    nombre = input(nombre="Nombre del dispositivo: ").strip()
    tipo = input("Nombre del dispositivo: ").strip()
    estado = input("Estado inicial (encendido/apagado): ").strip().lower()


    nuevo_dispositivo = {
        'nombre': nombre,
        'tipo': tipo,
        'estado': estado
    }


    usuario['dispositivos'].append(nuevo_dispositivo)
    print(f"✅ Dispositivo '{nombre}' agregado con éxito.")

def listar_dispositivos(usuario):
    print("\n--- Dispositivos Registrados ---")
    if not usuario["dispositivos"]:
        print("No tienes dispositivos registrados.")
        return
    for i, disp in enumerate(usuario["dispositivos"], start=1):
        print(f"{i}. {disp['nombre']} | Tipo: {disp['tipo']} | Estado: {disp['estado']}")

def buscar_dispositivo(usuario):
    print("\n--- Buscar Dispositivo ---")
    nombre = input("Ingresa el nombre del dispositivo: ").strip()

    for disp in usuario["dispositivos"]:
        if disp["nombre"].lower() == nombre.lower():
            print(f"✅ Dispositivos encontrado: {disp}")
            return
        print("❌ Dispositivo no encontrado.")

def eliminar_dispositivo(usuario):
    print("\n--- Eliminar Dispositivo ---")
    nombre = input("Nombre del dispositivo a eliminar: ").strip()

    for disp in usuario["dispositivos"]:
        if disp["nombre"].lower() == nombre.lower():
            usuario["dispositivos"].remove(disp)
            print(f"✅ Dispositivo '{nombre}' eliminado con éxito.")
            return
    print("❌ No se encontró un dispositivo con ese nombre.")

