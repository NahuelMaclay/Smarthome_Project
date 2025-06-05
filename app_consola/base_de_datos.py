
base_de_datos={
    
    "automatizaciones":[
      {
        'id':1,
        'nombre': "Activar luces del Patio",
        "hora_inicio":"19:00",
        "hora_fin":"06:00",
        "tipo":"iluminación",
        "dispositivo":"luz",
        "estado":"activo"
      } ,
      {
        'id':2,
        'nombre': "activador/desactivador aspiradora",
        "hora_inicio":"10:00",
        "hora_fin":"12:00",
        "tipo":"aspiradora",
        "dispositivo":"aspiradora",
        "estado":"activo"
      }  

        
    ],
    "dispositivos":[
        {
        'id':1,
        'nombre': "luz",
        'tipo': "iluminación",
        'ubicacion': "patio",
        'estado': False,
    },
    {
        'id':2,
        "nombre": "aire acondicionado",
        "tipo": "aire acondicionado",
        "ubicacion": "habitación",
        "estado": False,
    },
    {
        'id':3,
        "nombre": "aspiradora",
        "tipo": "aspiradora",
        "ubicacion": "comedor",
        "estado": False
    }
    ],
    "usuarios":[
    {
     id:1,
     "nombre":"admin",
     "contraseña":"admin",
     
     "Role":"admin"   
    },
    {
        id:2,
        "nombre":"usuario1",
        "contraseña":"usuario1",

        "Role":"estandar"
    }
]

}