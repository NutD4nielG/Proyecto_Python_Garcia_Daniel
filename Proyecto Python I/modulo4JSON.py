import json

ruta = "D:\\CAMPUSLANDS\\VsC\\Proyecto Python I//"

def cargueDat(archivo):
    try:
        clinica_Acme = ruta + archivo
        with open(clinica_Acme,"r",encoding="utf-8") as acme:
            lista = json.load(acme)
    except FileNotFoundError:
        print("="*50)
        print("No se ha encontrado archivo para leer")
        print("="*50)
        lista = {"Usuarios": [],"Pacientes": [], "Historias": []}
    return lista

def guardarDat(lista,archivo):
    clinica_Acme = ruta + archivo
    with open(clinica_Acme,"w",encoding="utf-8") as acme:
        json.dump(lista,acme,indent=4,ensure_ascii=False)

def reporte_anual():
    datos = cargueDat("clinica_ACME.json")
    soloanio = []
    for reporte in datos["Historias"]:
        fecha = reporte["Fecha de atención"]
        anios = fecha[0:4]
        if anios.isdigit():
            if anios not in soloanio:
                soloanio.append(anios)
        else:
            print("Fecha inválida")
    print(soloanio)
    reportej = {"años":{}}
    for un_anio in soloanio:
        total = 0
        suma_sintomas = 0
        medicos = []
        pacientes = []
        for reporte in datos["Historias"]:
            fecha = reporte["Fecha de atención"]
            if fecha[0:4] == un_anio:
                total += 1
                sintomas = reporte["Historia"][2]["Síntomas"]
                suma_sintomas += len(sintomas.split(","))
                if reporte["Médico"] not in medicos:
                    medicos.append(reporte["Médico"])
                if reporte["Identificación"] not in pacientes:
                    pacientes.append(reporte["Identificación"])
    promedio_sintomas = suma_sintomas / total
    reportej["años"][un_anio] = {"total_diagnosticos": total,
                        "medicos_participantes": len(medicos),
                        "pacientes_atendidos": len(pacientes),
                        "promedio_sintomas": promedio_sintomas}
    print(un_anio,total,len(medicos),len(pacientes),promedio_sintomas)
    guardarDat(reportej,"reporte_anual.json")
    print("Reporte generado")


#test = reporte_anual()

