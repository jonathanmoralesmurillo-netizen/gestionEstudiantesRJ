from Estudiante import *

from RepositorioCSV import RepositorioCSV
from GestorEstudiantes import *

repo = RepositorioCSV("estudiantes.csv")
gestor = GestorEstudiantes(repo)



e1 = Estudiante(1,"Jon",66)
e2 = Estudiante(2,"beto", 70)
e3 = Estudiante(3,"maria",79)
e4 = Estudiante(4,"mario",100)
e5 = Estudiante(5,"aaron",50)

gestor.agregar_estudiante(e1)
gestor.agregar_estudiante(e2)
gestor.agregar_estudiante(e3)
gestor.agregar_estudiante(e4)
gestor.agregar_estudiante(e5)

print(gestor.estaditicas())
print(gestor.distribucion_porcentual())
print("Estudiantes ordenados por nombre:")
for e in gestor.listar_ordenado("nombre"):
    print(e)


print("Estudiantes ordenados por Nota:")
for e in gestor.listar_ordenado("nota"):
    print(e)

gestor.guardar()