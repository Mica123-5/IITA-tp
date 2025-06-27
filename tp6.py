#A Llevar regisstro de datos (npmbre, apellido, fech ncimiento, DNI,
# Tutor, TodasNotas, cant de faltas, cant. amonestaciones)
datos= { "Alumnos":[] }

def agregarAlumno():
    print("--Agregar alumno-- ")
    nombre= input("Nombre: ")
    apellido= ("Apellido: ")
    nacimiento=("Fecha de Nacimiento (dd/mm/aaaa):  ")
    dni=("DNI: ")
    tutor=("Nombre del tutor: ")
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
        "Amonestaciones": amonestaciones
    }
    
    datos["Alumnos"].append(alumno)
    print("Alumno cargado correctamente")

def registro():
    if not datos["Alumnos"]:
        print("No hay alumnos registrados")
    for i, alumno in enumerate(datos["Alumnos"]):  #enumerate da el num de indice (posicion)
        print(f"{i+1}. {alumno['Nombre']} {alumno['Apellido']} - DNI: {alumno['DNI']}")
    print()
        
def mostrarDatos():
    print("--Lista de alumnos--")
    if not datos["Alumnos"]:
        print("No hay alumnos cargados")
        return
    
    i=1
    for alumno in datos["Alumnos"]:
        print(f"{i}. {alumno['Nombre']} {alumno['Apellido']} - DNI: {alumno['DNI']}")
        i +=1
    print()

def modDatos():
    registro()
    try:  
        modif= int(input("Numero del alumno a modificar: ")) -1
        alumno = datos["Alumnos"][modif]
        print("Que dato desea modificar?")
        print(" 1.Nombre 2.Apellido 3.fecha de nacimiento 4. DNI  5. turor")
def menu():
    while True:
        print("--MENU--")
        print("")
    
#B mostrar los datos de c/u
#C modificar los datos de los alumnos
#D agregar alumnos
#E expulsar alumnos