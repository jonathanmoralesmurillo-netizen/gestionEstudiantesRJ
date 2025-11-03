import logging
import math
import csv
from Estudiante import Estudiante
from RepositorioPort import RepositorioPort

class GestorEstudiantes :
    def __init__(self, repo: RepositorioPort):
        self._estudiantes: list[Estudiante] = []
        self._repo = repo
        self._configurar_logging()



    def agregar_estudiante(self, id:int, nombre: str, nota: float) -> bool:  # crea un estudiante
        # Validación de unicidad de ID
        if any(est.id == id for est in self.estudiantes):
            raise ValueError(f"Ya existe un estudiante con id {id}")

        nuevo_estudiante = Estudiante(id,nombre,nota)
        self.estudiantes.append(nuevo_estudiante)
        return nuevo_estudiante

    def editar_estudiante(self, id, nombre, nota) -> bool:
        # Edita los datos de un estudiante existente por su ID
        # Retorna True si se actualizó, o lanza ValueError si no existe
        for est in self.estudiantes:
            if est.id == id:
                est.nombre = nombre
                est.nota = nota
                return True
        raise ValueError(f"No estudiante con id {id}")

    def eliminar_estudiante(self, id_busqueda: int) -> bool:
        # Elimina un estudiante por su ID. Retorna True si se eliminó, False si no existe.
        for est in self.estudiantes:
            if est.id == id_busqueda:
                self.estudiantes.remove(est)
                return True
        return False

    def buscar_por_id(self, id_):
        for e in self._estudiantes:
            if e.getId() == id_:
                return e
        return None



    def buscar_por_inicial(self, letra: str):
        """Devuelve una lista de estudiantes cuyo nombre empieza con la letra indicada."""
        return [e for e in self._estudiantes if e.getNombre().startswith(letra)]

    def buscar_por_nombre(self, nombre_busqueda: str) -> Estudiante:
        for est in self.estudiantes:
            if est.nombre.lower().startswith(nombre_busqueda.lower()): return est
        return None

    def listar_ordenado(self, criterio: str = "nombre") -> list[
        Estudiante]:  # Devuelve la lista ordenada, según criterio
        # devuelve la lista ordenada según el criterio: nombre, nota o id.
        # Diccionario que asocia el criterio con la clase de ordenamiento
        criterios_validos = {
            "nombre": lambda est: est.nombre,
            "nota": lambda est: est.nota,
            "id": lambda est: est.id,
        }
        # valida el criterio
        reverse = False
        if criterio not in criterios_validos:
            raise ValueError("Criterio no válido. Usa 'nombre', 'nota' o 'id'.")
        # determina el criterio ascendente o descendente, si es nota lo ordena de mayor a menor
        if criterio == "nota":
            reverse = True
        return sorted(self.estudiantes, key=criterios_validos[criterio], reverse=reverse)

    def clasificar(self, umbral: float) -> list[dict]:
          #Devuelve la lista de estudiantes indicando si están aprobados o no,
          #según el umbral de nota configurado.
        lista_clasificada = []
        for est in self.estudiantes:
            estado = "aprobado" if est.nota >= umbral else "reprobado"
            estudiante_dict = {
                "id": est.id,
                "nombre": est.nombre,
                "nota": est.nota,
                "estado": estado
            }
            lista_clasificada.append(estudiante_dict)
        return lista_clasificada

    @property
    def estudiantes(self) -> list[Estudiante]:
        # opcional, para lectura externa consistente
        return self._estudiantes

    def _configurar_logging(self) -> None:
        """Configurar el registro para el seguimiento de errores."""
        logging.basicConfig(
            filename='errores.log',
            level=logging.ERROR,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

    def agregar_estudiante(self, estudiante: Estudiante):
        self.estudiantes.append(estudiante)

    def set_estudiantes(self, estudiantes: list[Estudiante]) -> None:
        """
        Asigna una lista de objetos Estudiante al gestor.

        Args:
            estudiantes (List[Estudiante]): Lista de estudiantes a asignar.
        Raises:
            TypeError: Si algún elemento no es una instancia de Estudiante.
        """
        if not all(isinstance(e, Estudiante) for e in estudiantes):
            raise TypeError("Todos los elementos deben ser instancias de la clase Estudiante.")

        self._estudiantes = estudiantes.copy()
        print(f"✅ Se asignaron {len(estudiantes)} estudiantes correctamente.")

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
        for estudiante in self._estudiantes:
            if estudiante.getNota()>=umbral:
                listAprobados.append(estudiante)
            else:
              listReprobados.append(estudiante)
        return {
            "Aprobados": listAprobados,
            "Reprobados": listReprobados
        }
    def estadisticas(self)-> dict[str,float]:

        if not self.estudiantes:
            return{
                'promedio': 0.0,
                'maxima': 0.0,
                'minima': 0.0,
                'desviacion': 0.0,
                'total':0.00
            }
         #medida de dispersión que indica qué tan dispersos están los datos de un conjunto con respecto a su media aritmética
        notas= [estudiantes.getNota() for estudiantes in self._estudiantes]# saco las notas
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

    def distribucion_porcentual(self) ->dict:
        if not self.estudiantes:
          return  {'0-59':0.0,
                '60-79':0.0,
                '80-100':0.0
             }
        total= len(self.estudiantes)
        rango0a59 = sum(1 for est in self._estudiantes if 0 <= est.getNota()<= 59)
        rango60a79 = sum(1 for est in self._estudiantes if 60 <= est.getNota() <= 79)
        rango80a100= sum(1 for est in self._estudiantes if 80 <= est.getNota() <= 100)
        return {'0-59': round(( rango0a59/total)*100,2),
                '60-79': round((rango60a79/total)*100,2),
                '80-100': round((rango80a100/total)*100,2),
                }

    def contar_estudiantes(self) ->int :
        return len(self.estudiantes)




    def obtener_todos(self)-> list[Estudiante]:
        """.copy(): devuelve una copia superficial (shallow copy) de la lista.

    Beneficio: quien llame al método recibe otra lista;
    si añade o elimina elementos en esa lista no altera la lista interna del objeto."""
        return self._estudiantes


    def guardar(self)->None:
        try:
            self._repo.guardar(self._estudiantes)
            logging.info(f"Guardando {len(self._estudiantes)} estudiantes")
        except Exception as e:
            logging.error(e)
            raise

    def cargar(self) -> None:
        """Load students from repository."""
        try:
            self._estudiantes = self._repo.cargar()
            logging.info(f"Loaded {len(self._estudiantes)} students from repository")
        except Exception as e:
            logging.error(f"Error loading students: {e}")
            raise

    def agregar_desde_datos(self, id: int, nombre: str, nota: float) -> None:
        """Crea el Estudiante y lo agrega (la vista solo pasa los datos)."""
        from Estudiante import Estudiante
        # Validación de unicidad por id
        if any(e.id == id for e in self.estudiantes):
            raise ValueError(f"Ya existe un estudiante con id {id}")
        est = Estudiante(id, nombre, nota)
        self.agregar_estudiante(est)

