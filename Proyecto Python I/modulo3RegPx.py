#Función de registro de paciente
def regPx():
    print("="*50)
    print("\t\tRegistro de Paciente")
    print("\t\tClínica ACME")
    print("="*50) # Diccionario de datos personales
    diccRegPx = {
        "Identificación": input("No. Identificación: "),
        "Tipo de identificación": input("Tipo de identifiación: "),
        "Nombres": input("Nombres: "),
        "Apellidos": input("Apellidos: "),
        "Género": input("Género: "),
        "Fecha de nacimiento": input("Fecha de nacimiento: "),
        "No De Teléfono": input("Número de teléfono: "),
        "Entidad": input("Entidad: "),
        "e_mail": input("E-mail: "),
        "Dirección": input("Dirección: "),
        "Estado civil": input("Estado Civil: ")
        }
    print("="*50)
    return diccRegPx

#Función de historis clinica parte uno
def historia1(histo):
    print("="*50)
    print("\tHISTORIA CLINICA - CLÍNICA ACME")
    print("="*50)
    print("\t\tDatos Personales")
    print("="*50) #Diccionario de datos personales
    diccDatosP = {"Nombre Paciente": histo["Nombres"], 
                "Fecha de nacimiento": histo["Fecha de nacimiento"],
                "Dirección": histo["Dirección"],
                "Entidad": histo["Entidad"],
                "Tipo de identificación": histo["Tipo de identificación"],
                "Identificación": histo["Identificación"],
                "Género": histo["Género"]
                }
    print(diccDatosP)
    print("="*50)
    print("\t\tDatos de ingreso")
    print("="*50) #Diccionario de Antecedentes
    diccDatosAnt = {"Antecedentes": input("Antecedentes: ")}
    print("="*50)
    print("\t\tExámen Físico")
    print("="*50) #Diccionario de examen físico
    diccExFisico = {"Frecuencia cardiaca": input("Frecuencia cardiaca: "),
                    "Frecuencia respiratoria": input("Frecuencia respiratoria: "),
                    "Peso": input("Peso: "),
                    "Talla": input("Talla(Cms): "),
                    "Temperatura": input("Temperatura: "),
                    "Glasgow": input("Glasgow:"),
                    "Descripción": input("Descripción: "),
                    "Síntomas": input("Síntomas: "),
                    "Diágnostico": input("Diágnostico: "),
                    }
    return diccDatosP,diccDatosAnt,diccExFisico

def historia2():
    print("="*50)
    print("\t\tPlan de manejo") #Medicamentos
    print("="*50)
    lstPlanMan = [] #Lista de plan manejo que se agrega desde el diccionario del ciclo
    while True:
        try:
            diccPlanMan = {
            "Cantidad": int(input("Cantidad: ")),
            "Descripción": input("Descripción: "),
            "Vía de administración": input("Vía de administración: "),
            "Posología": input("Posología: "),
            "Días de tratamiento": input("Días de tratamiento: ")
            }
            lstPlanMan.append(diccPlanMan)
            print("\t\t¿Desea agregar más medicamentos?")
            print("\t\t\tY/N")
            salida = input("").upper()
            if salida == "N":
                break
            else:
                continue
        except ValueError:
            print("Dato no válido")
    print("="*50)
    print("\t\tSolicitud de Exámenes") #---
    print("="*50)    
    lstExams = [] #Lista de exámenes que se agrega desde el diccionario de examenes
    while True:
        try:
            diccSoldExamCantObser = {
            "Cantidad": int(input("Cantidad: ")),
            "Descripción": input("Descripción: "),
            "Observaciones": input("Observaciones: ")
            }
            lstExams.append(diccSoldExamCantObser)
            print("\t\t¿Desea agregar más exámenes?")
            print("\t\t\tY/N")
            salida = input("").upper()
            if salida == "N":
                break
            else:
                continue
        except ValueError:
            print("Dato no válido")
    return lstPlanMan, lstExams

def buscarPx(documento,listaPxs):
    print("="*50)
    print("\t\tBúsqueda de paciente")
    print("="*50)   
    for i in listaPxs:
        if documento == i["Identificación"]:
            return i
    return None
