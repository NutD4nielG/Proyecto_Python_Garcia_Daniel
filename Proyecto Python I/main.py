import modulo1Login
import modulo2RegUsu
import modulo3RegPx
import modulo4JSON
from datetime import date

datos = modulo4JSON.cargueDat("clinica_ACME.json")

lst_usu = datos["Usuarios"]
if len(lst_usu) == 0:
    lst_usu.append(modulo2RegUsu.primer_usuario())
    modulo4JSON.guardarDat(datos,"clinica_ACME.json")

lst_Pxs = datos["Pacientes"]
lst_Histo = datos["Historias"]

while True:
    modulo1Login.menu() #Menú 1
    opcion = int(input("\n\tIngrese opción: "))
    match opcion:
        case 1: #Iniciar sesión
            login = modulo1Login.login(lst_usu)
            if login:
                while True:
                    modulo1Login.menu2(login["Nombres"]) #Menú 2
                    opcion2 = int(input("\n\tIngrese opción: "))
                    match opcion2:
                        
                        case 1: # Registrar usuario
                                        regi_usu = modulo2RegUsu.registro_usu()
                                        lst_usu.append(regi_usu)
                                        print("\t\tUsuario Registrado")
                                        modulo4JSON.guardarDat(datos,"clinica_ACME.json")

                        case 2: #Registrar paciente
                            regi_px = modulo3RegPx.regPx()
                            lst_Pxs.append(regi_px)
                            modulo4JSON.guardarDat(datos,"clinica_ACME.json")
                            print("\t\tPaciente registrado")

                        case 3: #Diligenciar HC
                            print("="*50)
                            documento = input("Identificación:")
                            print("="*50)
                            busca_px = modulo3RegPx.buscarPx(documento,lst_Pxs)
                            if busca_px == None:
                                print("\tSin coincidencias")
                            else:
                                histopx1 = modulo3RegPx.historia1(busca_px)
                                histopx2 = modulo3RegPx.historia2()
                                dicc_histo = {"Historia":histopx1,"Historia2":histopx2,"Identificación": documento,"Médico": login["Nombres"],"Fecha de atención": str(date.today())}
                                lst_Histo.append(dicc_histo)
                                modulo4JSON.guardarDat(datos,"clinica_ACME.json")
                                prescripcion = {"Fecha":dicc_histo["Fecha de atención"],"Médico":dicc_histo["Médico"],"Paciente":dicc_histo["Identificación"],"Examen físico":dicc_histo["Historia"][2] ,"Plan de manejo":dicc_histo["Historia2"]}
                                modulo4JSON.guardarDat(prescripcion, "Prescripción_" + documento + "_" + dicc_histo["Fecha de atención"] + ".json")

                        case 4: # Buscar HC
                            documento = input("Identificación:")
                            busca_px = modulo3RegPx.buscarPx(documento,lst_Pxs)
                            if busca_px == None:
                                print("Sin coincidencias")
                            else:
                                for consulta in lst_Histo:
                                    if documento == consulta["Identificación"]:
                                        print("="*50)
                                        print("\tHISTORIA CLINICA - CLÍNICA ACME")
                                        print("="*50)
                                        print(f"Médico tratante: {consulta["Médico"]} | Fecha de atención: {consulta["Fecha de atención"]}")
                                        print("="*50)
                                        for seccion in consulta["Historia"]:
                                            for seccion2 in seccion:
                                                print(f"{seccion2}: {seccion[seccion2]}")
                                        print("="*50)
                                        print("\t\tPlan de manejo")
                                        print("="*50)
                                        for seccion3 in consulta["Historia2"]:
                                            for seccion4 in seccion3:
                                                for seccion5 in seccion4:
                                                    print(f"{seccion5}: {seccion4[seccion5]}")
                                                print("-"*50)

                        case 5: #Cerrar sesión
                            print("\t\t¿Desea Cerrar sesión?")
                            print("\t\t\tY/N")
                            salida = input("").upper()
                            if salida == "Y":
                                print("="*50)
                                print("\tHa cerrado sesión satisfactoriamente")
                                print("="*50)
                                break

        case 2: #Cerrar sistema
                    print("="*50)
                    print("\tHa cerrado el sistema correctamente")
                    print("="*50)
                    break
