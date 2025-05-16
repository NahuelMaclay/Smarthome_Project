# Gestión de usuarios (registro e inicio de sesión)

# auth.py



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






    # nombre = input("Nombre de usuario: ").strip()
    # if any(usuario['nombre'] == nombre for usuario in usuarios):
    #     print("⚠️ El nombre de usuario ya está en uso, intenta otro.")
    #     return
    

    # contraseña = input("Contraseña: ").strip()
    # usuarios.append({
    #     'nombre': nombre,
    #     'contraseña': contraseña,
    #     'dispositivos': [] # Lista vacía para los dispositivos del usuario
    # })
    print("✅ Usuario registrado con éxito.")

def iniciar_sesion():
    print("\n--- Inicio de Sesión ---")
    nombre = input("Nombre de usuario: ").strip()
    contraseña = input("Contraseña: ").strip()
    if nombre == usuario['nombre'] and contraseña == usuario['contraseña']:
     print(f"✅ Inicio de sesión exitoso, {nombre}!")
     
     usuario['isAuth'] = True
     return usuario  # Devuelve el diccionario del usuario 
     

    # for usuario in usuarios:
    #     if usuario['nombre'] == nombre and usuario['contraseña'] == contraseña:
    #         print(f"✅ Inicio de sesión exitoso, {nombre}!")
    #         return usuario  # Devuelve el diccionario del usuario
    # print("❌ Credenciales incorrectas. Intenta nuevamente.")
    # return None  # Si no se encuentra el usuario o la contraseña es incorrecta