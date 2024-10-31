print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Definimos una lista con las asignaturas del curso
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Inicializamos un diccionario para almacenar las notas
notas = {}

# Iteramos sobre cada asignatura para preguntar la nota al usuario
for asignatura in asignaturas:
    # Pedimos al usuario que ingrese la nota
    nota = float(input(f"Ingrese la nota que sacaste en {asignatura}: "))
    # Almacenamos la nota en el diccionario
    notas[asignatura] = nota

# Mostramos las asignaturas y las notas
for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado {nota}.")
