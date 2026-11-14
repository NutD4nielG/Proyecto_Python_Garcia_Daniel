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
