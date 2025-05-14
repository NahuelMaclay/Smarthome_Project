# Gestión de usuarios (registro e inicio de sesión)

# auth.py


from data import usuarios


def registrar_usuario():
    print("\n--- Registro de Usuario ---")
    nombre = input("Nombre de usuario: ").strip()
    if any(usuario['nombre'] == nombre for usuario in usuarios):
        print("⚠️ El nombre de usuario ya está en uso, intenta otro.")
        return
    

    contraseña = input("Contraseña: ").strip()
    usuarios.append({
        'nombre': nombre,
        'contraseña': contraseña,
        'dispositivos': [] # Lista vacía para los dispositivos del usuario
    })
    print("✅ Usuario registrado con éxito.")

def iniciar_sesion():
    print("\n--- Inicio de Sesión ---")
    nombre =input("Nombre de usuario: ").strip()
    contraseña = input("Contraseña: ").strip()


    for usuario in usuarios:
        if usuario['nombre'] == nombre and usuario['contraseña'] == contraseña:
            print(f"✅ Inicio de sesión exitoso, {nombre}!")
            return usuario  # Devuelve el diccionario del usuario
    print("❌ Credenciales incorrectas. Intenta nuevamente.")
    return None  # Si no se encuentra el usuario o la contraseña es incorrecta