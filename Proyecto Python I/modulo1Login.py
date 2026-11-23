#Login de la clínica
def menu():
    print("="*50)
    print("\tACME Clinic\tBienvenido")
    print("="*50)
    print("""
    \t\t1.Iniciar sesión
    \t\t2.Cerrar el sistema""")

#Menú después de iniciar sesión

def menu2(doctor):
    print("="*50)
    print(f"\tACME Clinic\tBienvenido Dr.{doctor}")
    print("="*50)
    print("""
    \t\t1.Registrar Usuario
    \t\t2.Registrar paciente
    \t\t3.Diligenciar historia clínica
    \t\t4.Buscar historia
    \t\t5.Generar reporte
    \t\t6.Cerrar sesión""")

#Inicio de sesión
def login(lst_usu):
    while True:
        print("="*50)
        print("Ingrese su usuario y contraseña para iniciar sesión")
        print("="*50)
        e_mail = input("\tIngrese el email: ")
        contra = input("\tIngrese la contraseña: ")
        for i in lst_usu:
            if e_mail == i["e_mail"] and contra == i["Contraseña"]:
                print("\tHa iniciado sesión correctamente")
                return i
        else:
            print("Usuario o contraseña no válida,Vuelva a intentar")
            continue



