from Estudiante import *

from RepositorioCSV import RepositorioCSV
from GestorEstudiantes import *
from RepositorioCSV import *

repo = RepositorioCSV("estudiantes.csv")
gestor = GestorEstudiantes(repo)
gestor.set_estudiantes(repo.cargar())
gestor.obtener_Todos()
"""holA #12 """

print(gestor.estaditicas())
print(gestor.distribucion_porcentual())
print("Estudiantes ordenados por nombre:")
for e in gestor.listar_ordenado("nombre"):
    print(e)


print("Estudiantes ordenados por Nota:")
for e in gestor.listar_ordenado("nota"):
    print(e)

gestor.guardar()