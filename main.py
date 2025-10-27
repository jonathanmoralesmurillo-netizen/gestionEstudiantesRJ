from Estudiante import *
from GestorEstudiantes import *
g1 = GestorEstudiantes()
g1.agregar_estudiante (1,"Jon",60)
g1.agregar_estudiante (2,"Rita",100)
print(f" Mis estudiantes: {g1.listar_ordenado()} ")

