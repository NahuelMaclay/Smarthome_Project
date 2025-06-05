from states import states
from base_de_datos import base_de_datos
from mensajes_consola import formatear_mensaje_consola
def login():
    if(states['is_auth']):
        formatear_mensaje_consola("ya estas logueado")
        return 

    nombre=input("ingrese nombre de usuario: ").strip().lower()
    contraseña=input("ingrese contraseña: ").strip().lower()
    for usuario in base_de_datos['usuarios']:
        if (usuario['nombre']==nombre and usuario['contraseña']==contraseña):
            
            states['is_auth']=True
            states['nombre']=nombre
            states['contraseña']=contraseña
            states['Role']=usuario['Role']
            
            formatear_mensaje_consola(f"Se loguea el usuario.{usuario['nombre']};role:{usuario['Role']}")
           
            return

    else:
            
            formatear_mensaje_consola("Usuario o contraseña incorrectos")
            
            return


def register():
    nombre=input("ingrese nombre de usuario: ").strip().lower()
    contraseña=input("ingrese contraseña: ").strip().lower()
    for usuario in base_de_datos['usuarios']:
        if (usuario['nombre']==nombre):
           
            formatear_mensaje_consola("Usuario ya existe.")
           
            return 
    nuevo_usuario={
        'id':len(base_de_datos['usuarios'])+1,
        'nombre':nombre,
        'contraseña':contraseña,
        'is_auth':False,
        'Role':'estandar'
    }
    base_de_datos['usuarios'].append(nuevo_usuario)
 
    formatear_mensaje_consola("se registra un usuario")
  
    

def logout():
    states['is_auth']=False
    states['nombre']=""
    states['contraseña']=""
    states['Role']=""
    formatear_mensaje_consola("se cierra sesion")
   

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

def consultar_perfil():
    if(verify_auth()):
        
        formatear_mensaje_consola(f"Usuario: {states['nombre']}, Role: {states['Role'] }")
        
    else:
        formatear_mensaje_consola(" no estas logueado ")
        return


def cambiar_rol():
    if(verify_admin()==False):
        formatear_mensaje_consola("No tiene permisos para realizar esta acción")
        return
    nombre=input("ingrese nombre de usuario: ").strip().lower()
    if(nombre=="admin"):
        formatear_mensaje_consola("No se puede cambiar el rol de admin")
        return
    if(nombre==states['nombre']):
        formatear_mensaje_consola("No se puede cambiar el rol de usted mismo")
        return
    for usuario in base_de_datos['usuarios']:
        if (usuario['nombre']==nombre and usuario["Role"]=='estandar') :
            usuario['Role']='admin'
            formatear_mensaje_consola(f"se cambia el rol de {usuario['nombre']} a admin")
        elif (usuario['nombre']==nombre and usuario["Role"]=='admin'):
            usuario['Role']='estandar'
            formatear_mensaje_consola(f"se cambia el rol de {usuario['nombre']} a estandar")
        else:
            formatear_mensaje_consola("Usuario no encontrado")
   
        
           
        
def listar_usuarios():
    if(verify_admin()==False):
        formatear_mensaje_consola("No tiene permisos para realizar esta acción")
        return
    for usuario in base_de_datos['usuarios']:
        formatear_mensaje_consola(f"Usuario: {usuario['nombre']}, Role: {usuario['Role'] }")
            
            
          
            