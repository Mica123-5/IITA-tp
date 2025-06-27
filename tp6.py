#A Llevar regisstro de datos (npmbre, apellido, fech ncimiento, DNI,
# Tutor, TodasNotas, cant de faltas, cant. amonestaciones)
datos= { "Alumnos":[] }
def registro():
    print("--Registro de Alumnos--")
    if not datos["Alumnos"]:
        print("no hay alumnos cargados")
        return
    for i, alumno in enumerate(datos["Alumnos"],1):
        print(f"{i}. {alumno['Nombre']} {alumno['Apellido']}")
    print()

def agregarAlumno():
    print("--Agregar alumno nuevo-- ")
    nombre= input("Nombre: ")
    apellido= input("Apellido: ")
    nacimiento=input("Fecha de Nacimiento (dd/mm/aaaa):  ")
    dni=input("DNI: ")
    tutor=input("Nombre del tutor: ")
    notas= []
    faltas=0
    amonestaciones=0
    
    alumno= {
        "Nombre": nombre,
        "Apellido": apellido,
        "Fecha de nacimiento": nacimiento,
        "DNI": dni,
        "Tutor": tutor,
        "Notas": notas,
        "Faltas": faltas,
        "Amonestaciones": amonestaciones
    }
    
    datos["Alumnos"].append(alumno)
    print("Alumno cargado correctamente\n")

def mostrarDatos():
    registro()
    if not datos["Alumnos"]:
        print("No hay alumnos cargados")
        return
    
    try:
        mostrar= int(input("Numero del alumno a mostrar: "))-1
        alumno= datos["Alumnos"][mostrar]
        print("--Datos Completos del alumno--")
        for clave, valor in alumno.items():   #recorre el diccionario alumno  # .items() convierte el diccionario en pares
            print(f"{clave}: {valor}")      #clave va a ser nombre y apellido y valor Mica, Juarez, etc
        print()
    except (ValueError, IndexError):
        print("Numero invalido")

def modDatos():
    registro()
    try:  
        modif= int(input("Numero del alumno a modificar: ")) -1
        alumno = datos["Alumnos"][modif]
        print("Que dato desea modificar?")
        print(" 1)Nombre 2)Apellido\n 3)Fecha de nacimiento\n 4) DNI\n  5) Tutor\n  6)Notas\n7) Faltas\n8)Amonestaciones")
        opcion= int(input("Opcion: "))
        nuevo=input("Nuevo: ")
        
        if opcion== 1:
            alumno["Nombre"]= nuevo
        elif opcion ==2:
            alumno["Apellido"]=nuevo
        elif opcion==3:
            alumno["Fecha de nacimiento"]=nuevo
        elif opcion==4:
            alumno["DNI"]=nuevo
        elif opcion==5:
            alumno["Tutor"]=nuevo
        elif opcion==6:
            alumno["Notas"]=nuevo
        elif opcion==7:
            alumno["Faltas"]=nuevo
        elif opcion==8:
            alumno["Amonestaciones"]=nuevo 
        else:
            print("Opcion invalida")
            return
        print("dato modificado")
    except (IndexError, ValueError):
        print("Entrada invalida")
        
def expulsar():
    registro()
    if not datos["Alumnos"]:
        return
    try:
        num= int(input("Numero del alumno a expulsar: "))-1
        alumno= datos["Alumnos"].pop(num)
        print(f"Alumno{alumno['Nombre']} {alumno['Apellido']} EXPULSADO\n")
    except (IndexError, ValueError):
        print("Numero invalido")
    
def menu():
    while True:
        print("--MENU--")
        print("a. Ver el registro de alumnos")
        print("b. Mostrar datos de un alumno")
        print("c.Modificar los datos de un alumno")
        print("d.Agregar alumno")
        print("e. Expulsar alumno")
        print("f. salir")
        opcion=input("Ingrese una opcion: ")
        if opcion== "a":
            registro()
        elif opcion=="b":
            mostrarDatos()
        elif opcion=="c":
            modDatos()
        elif opcion=="d":
            agregarAlumno()
        elif opcion == "e":
            expulsar()
        elif opcion=="f":
            print("Saliendo...")
            break
        else:
            print("opcion invalida")
menu()
        
#B mostrar los datos de c/u
#C modificar los datos de los alumnos
#D agregar alumnos
#E expulsar alumnos
