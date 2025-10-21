import math

from Estudiante import Estudiante

class GestorEstudiantes :






































































































    estudiantes: list[Estudiante]
    def __init__(self):
        self.estudiantes: list[Estudiante] = []

    def agregar_estudiante(self, estudiante: Estudiante):
        self.estudiantes.append(estudiante)

    def listar_ordenado(self,orden: str = "nombre")-> list[Estudiante]:
        if orden == "nombre":
            return sorted(self.estudiantes, key=lambda estudiante: estudiante.getNombre())
        elif orden == "nota":
            return sorted(self.estudiantes, key=lambda estudiante: estudiante.getNota())
        else:
            raise ValueError("los criterios no son ni nombre ni nota")
    def  clasificar(self, umbral: float = 70.0)-> dict:
        listReprobados =[]
        listAprobados = []
        for estudiante in self.estudiantes:
            if estudiante.getNota()>=umbral:
                listAprobados.append(estudiante)
            else:
              listReprobados.append(estudiante)
        return {
            "Aprobados": listAprobados,
            "Reprobados": listReprobados
        }

    def estaditicas(self)-> dict[str,float]:

        if not self.estudiantes:
            return{
                'promedio': 0.0,
                'maxima': 0.0,
                'minima': 0.0,
                'desviacion': 0.0,
                'total':0.00
            }
         #medida de dispersión que indica qué tan dispersos están los datos de un conjunto con respecto a su media aritmética
        notas= [estudiantes.getNota() for estudiantes in self.estudiantes]# saco las notas
        promedio= sum(notas)/len(notas)
        maxima= max(notas)
        minima= min(notas)
        varianza = sum((nota-promedio)**2 for nota in notas)/len(notas)
        desviacion= math.sqrt(varianza)
        return {
            "promedio": round(promedio,2),
            "maxima": maxima,
            "minima": minima,
            "desviacion": round(desviacion,2),
            "total": len(self.estudiantes)
        }


"""
#1 Rita
-estudiantes: list[Estudiante]
- repo: RepositorioPort
+ __init__(repo: RepositorioPort)
+agregar_estudiante(est: Estudiante) void
+ editar_estudiante(id: int, nombre: str = None, nota: float = None) void
+ eliminar_estudiante(id: int) void
+ buscar_por_id(id: int) Estudiante
+ buscar_por_nombre(prefijo: str) list[Estudiante]

2
Jon
+ listar_ordenado(criterio: str = "nombre") list[Estudiante]
listo 
+ clasificar(umbral: float = 70.0) dict
listo 

+ estadisticas() ->dict estudiantes
+ distribucion_porcentual() ->dict
+ cargar() void
+ guardar() void
+ obtener_todos()
list[Estudiante]
+ contar_estudiantes()->int

"""
