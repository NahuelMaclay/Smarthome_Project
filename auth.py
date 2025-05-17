
from states import usuario 


def registrar_usuario():
    print("\n--- Registro de Usuario ---")
    usuario['nombre'] = input("Nombre de usuario: ").strip()
    if usuario['nombre'] == "":
        print("⚠️ El nombre de usuario no puede estar vacío.")
        usuario['nombre'] = input("Nombre de usuario: ").strip()
    usuario['contraseña'] = input("Contraseña: ").strip()
    if usuario['contraseña'] == "":
        print("⚠️ La contraseña no puede estar vacía.")
        usuario['contraseña'] = input("Contraseña: ").strip()
    print(f"✅ Usuario {usuario['nombre']} registrado con éxito.")
    print("✅ Usuario registrado con éxito.")


def iniciar_sesion():
    print("\n--- Inicio de Sesión ---")
    nombre = input("Nombre de usuario: ").strip()
    contraseña = input("Contraseña: ").strip()
    if nombre == usuario['nombre'] and contraseña == usuario['contraseña']:
     print(f"✅ Inicio de sesión exitoso, {nombre}!")
     usuario['is_auth'] = True
     
     return usuario  