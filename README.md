# Proyecto_Python_Garcia_Daniel

## Clínica ACME - Sistema de diágnosticos

Programa modular realizado en Python para sistematizar el proceso de diagnostico de los pacientes de la clínica ACME, que hasta el momento, lo realizaban manualmente.

---
## Funcionalidades
-*Login:* Acceso al sistema con e-mail corporativo y contraseña.

-*Registro de usuarios:* Médicos y administrativos de la clínica (Sólo un usuario con sesión iniciada puede registrar a otro)

-*Registro de pacientes:* Datos personales del paciente, como: Identificación, nombres, apellidos, teléfono. e-mail, dirección, género, estado civil... Etc..

-*Diligenciar historia clínica:* Busca el paciente por su número de identificación y registra la consulta
  -Antecedentes y exámen físico
  -Síntomas y diagnóstico.
  - Plan de manejo (Medicamentos, cantidad, vía de administración, posología y días de tratamiento)
  - Solicitud de exámenes
  - Cada consulta queda asociada a una fecha, un paciente y un médico.
-*Buscar historia clínica:* Muestra los datos del paciente como encabezado y sus consultas registradas.
---  
## Estructura del proyecto

```
├── main.py            # Archivo principal de ejecución (menús)
├── modulo1Login.py    # Menús e inicio de sesión
├── modulo2RegUsu.py   # Registro de usuarios y administrador inicial
├── modulo3RegPx.py    # Registro de pacientes, historia clínica y búsqueda de pacientes
├── modulo4JSON.py     # Carga y guardado de datos en JSON
└── datos.json         # Persistencia de la información del programa
```
