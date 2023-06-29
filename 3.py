import random

vehiculos = []

def grabar():
    tipo = input("Ingrese el tipo de vehículo: ")
    patente = input("Ingrese la patente del vehículo: ")
    marca = input("Ingrese la marca del vehículo: ")
    precio = float(input("Ingrese el precio del vehículo: "))

    if len(patente) != 6:
        print("Error: La patente debe tener 6 caracteres.")
        return
    if not 2 <= len(marca) <= 15:
        print("Error: La marca debe tener entre 2 y 15 caracteres.")
        return
    if precio <= 5000000:
        print("Error: El precio debe ser mayor a $5.000.000.")
        return

    multas = []
    while True:
        monto = float(input("Ingrese el monto de una multa (0 para terminar): "))
        if monto == 0:
            break
        fecha = input("Ingrese la fecha de la multa: ")
        multas.append((monto, fecha))

    fecha_registro = input("Ingrese la fecha de registro del vehículo: ")
    nombre_dueno = input("Ingrese el nombre del dueño: ")

    vehiculo = {
        "tipo": tipo,
        "patente": patente,
        "marca": marca,
        "precio": precio,
        "multas": multas,
        "fecha_registro": fecha_registro,
        "nombre_dueno": nombre_dueno
    }

    vehiculos.append(vehiculo)
    print("Vehículo registrado correctamente.")

def buscar():
    patente = input("Ingrese la patente del vehículo a buscar: ")
    encontrado = False
    
    for vehiculo in vehiculos:
        if vehiculo["patente"] == patente:
            print("Información del vehículo:")
            print("Tipo:", vehiculo["tipo"])
            print("Patente:", vehiculo["patente"])
            print("Marca:", vehiculo["marca"])
            print("Precio:", vehiculo["precio"])
            print("Multas:", vehiculo["multas"])
            print("Fecha de registro:", vehiculo["fecha_registro"])
            print("Dueño:", vehiculo["nombre_dueno"])
            encontrado = True
            break
    
    if not encontrado:
        print("No se encontró ningún vehículo con esa patente.")

def imprimir_certificados():
    for vehiculo in vehiculos:
        certificados = [
            {"nombre": "Emisión de contaminantes", "valor": random.randint(1500, 3500)},
            {"nombre": "Anotaciones vigentes", "valor": random.randint(1500, 3500)},
        ]
        for multa in vehiculo["multas"]:
            certificados.append({"nombre": "Multa", "valor": multa[0]})
        
        print("Certificados del vehículo:", vehiculo["patente"])
        print("Dueño:", vehiculo["nombre_dueno"])
        
        for certificado in certificados:
            print("Nombre:", certificado["nombre"])
            print("Valor:", certificado["valor"])
    
        print()

def salir():
    print("¡Hasta luego!")

while True:
    print("----- Auto Seguro -----")
    print("1. Grabar vehículo")
    print("2. Buscar vehículo")
    print("3. Imprimir certificados")
    print("4. Salir")
    
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        grabar()
    elif opcion == "2":
        buscar()
    elif opcion =="3":
        imprimir_certificados()
    elif opcion == "4":
        salir()
        break
    else:
        print("Opción inválida. Intente nuevamente.")
