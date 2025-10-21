from Estudiante import *
from GestorEstudiantes import *
gestor = GestorEstudiantes()
listaEstudiantes = []

e1 = Estudiante(1,"Jon",1)
e2 = Estudiante(2,"beto",2)
e3 = Estudiante(3,"maria",3)
e4 = Estudiante(4,"mario",4)
e5 = Estudiante(5,"aaron",5)


gestor.agregar_estudiante(e2)
gestor.agregar_estudiante(e3)
gestor.agregar_estudiante(e4)
gestor.agregar_estudiante(e5)

print("Estudiantes ordenados por nombre:")
for e in gestor.listar_ordenado("nombre"):
    print(e)


print("Estudiantes ordenados por Nota:")
for e in gestor.listar_ordenado("nota"):
    print(e)