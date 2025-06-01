from states import states
from base_de_datos import base_de_datos
def login():
    if(states['is_auth']):
        print("ya estas logueado")
        return 

    nombre=input("ingrese nombre de usuario: ").strip().lower()
    contraseña=input("ingrese contraseña: ").strip().lower()
    for usuario in base_de_datos['usuarios']:
        if (usuario['nombre']==nombre and usuario['contraseña']==contraseña):
            print("se loguea un usuario. ")
            states['is_auth']=True
            states['nombre']=nombre
            states['contraseña']=contraseña
            states['Role']=usuario['Role']
            return

    else:
            print("Usuario o contraseña incorrectos")
            return


def register():
    nombre=input("ingrese nombre de usuario: ").strip().lower()
    contraseña=input("ingrese contraseña: ").strip().lower()
    for usuario in base_de_datos['usuarios']:
        if (usuario['nombre']==nombre):
            print("el usuario ya existe")
            return ""
    nuevo_usuario={
        'id':len(base_de_datos['usuarios'])+1,
        'nombre':nombre,
        'contraseña':contraseña,
        'is_auth':False,
        'Role':'estandar'
    }
    base_de_datos['usuarios'].append(nuevo_usuario)
    print("se registra un usuario. ")
    

def logout():
    print("se cierra sesion")
    states['is_auth']=False
    states['nombre']=""
    states['contraseña']=""

def verify_auth():
    if states['is_auth']:
        return True
    else:
        return False

def verify_admin():
    if states['is_auth'] and states['Role']=='admin':
        return True
    else:
        return False