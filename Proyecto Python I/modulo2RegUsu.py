#Registro de usuarios de la clínica

def registro_usu(): #Función de registro de usuarios
        print("="*50)
        print("\tHa accedido al registro de usuario")
        print("\tDiligencie la siguiente información")
        print("="*50)
        diccRegUsu = {
                "No.Identificación": input("Número de identificación: "),
                "Nombres": input("Nombres: "),
                "Apellidos": input("Apellidos: "),
                "No De Teléfono": input("Número de teléfono: "),
                "e_mail": input("E-mail(Corporativo): "),
                "Dirección": input("Dirección: "),
                "Contraseña": input("Contraseña: "),
                "Rol": rol()
                }
        print("="*50)
        return diccRegUsu

guard_usu = []

def primer_usuario(): #Función del admin
    usuprime = {
        "No.Identificación": "0000",
        "Nombres": "Admin",
        "Apellidos": "Administrador",
        "No De Teléfono": "555000111",
        "e_mail": "admin@acmeclinic.com",
        "Dirección": "Cl 185 # 26-85",
        "Contraseña": "010203"
        }
    return usuprime

def prim_contrasena(): #Función de generar primera contraseña
    import random
    contrasena = random.sample(range(1,11),5)
    resutlado = "".join(map(str,contrasena))
    return resutlado

def rol():
    tipo_rol = input("Rol: ").capitalize()
    try:
        if tipo_rol == "Médico" or tipo_rol == "Administrativo":
            return rol
    except NameError:
            print("Rol válido")


# reg = registro_usu()
# contrasena = ""
# print(reg)
# guard_usu.append(primer_usuario())
# guard_usu.append(registro_usu())
# print(guard_usu)
