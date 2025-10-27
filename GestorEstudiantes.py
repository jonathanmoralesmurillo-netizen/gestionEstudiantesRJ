
# ***Gestionar estudiantes***
from Estudiante import Estudiante
#from RepositorioPort import RepositorioPort

class GestorEstudiantes:
    def __init__(self) -> None:
        # composición: el gestor posee y administra la lista de estudiantes
        self.alumnos : list (Estudiante) = []

    def agregar_estudiante(self, id:int, nombre: str, nota: float) -> bool:  # crea un estudiante
        # Validación de unicidad de ID
        if any(est.id == id for est in self.alumnos):
            raise ValueError(f"Ya existe un estudiante con id {id}")

        nuevo_estudiante = Estudiante(id,nombre,nota)
        self.alumnos.append(nuevo_estudiante)
        return nuevo_estudiante

    def editar_estudiante(self,id,nombre, nota) -> bool:
        # Edita los datos de un estudiante existente por su ID
        # Retorna True si se actualizó, o lanza ValueError si no existe
        for est in self.alumnos:
            if est.id == id:
                est.nombre = nombre
                est.nota = nota
                return True
        raise ValueError(f"No estudiante con id {id}")

    def eliminar_estudiante(self,id_busqueda:int) -> bool:
        # Elimina un estudiante por su ID. Retorna True si se eliminó, False si no existe.
        for est in self.alumnos:
               if est.id == id_busqueda:
                   self.alumnos.remove(est)
                   return True
        return False

    def buscar_por_id(self,id_busqueda:int) -> Estudiante:
        for i, est in self.alumnos:
            if est.id == id_busqueda:
                return est
        return None

    def buscar_por_nombre(self, nombre_busqueda: str) -> Estudiante:
        for est in self.alumnos:
            if est.nombre.lower().startswith (nombre_busqueda.lower()): return est
        return None

    def listar_ordenado(self, criterio: str="nombre") -> list[Estudiante]: #Devuelve la lista ordenada, según criterio
        #devuelve la lista ordenada según el criterio: nombre, nota o id.
        #Diccionario que asocia el criterio con la clase de ordenamiento
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
        return sorted(self.alumnos, key=criterios_validos[criterio], reverse=reverse)


def clasificar(self, umbral: float) -> list[dict]:
    """
    Devuelve la lista de estudiantes indicando si están aprobados o no,
    según el umbral de nota configurado.
    """
    lista_clasificada = []

    for est in self.alumnos:
        estado = "aprobado" if est.nota >= umbral else "reprobado"
        estudiante_dict = {
            "id": est.id,
            "nombre": est.nombre,
            "nota": est.nota,
            "estado": estado
        }
        lista_clasificada.append(estudiante_dict)

    return lista_clasificada

# def estadisticas

# def cargar

#def guardar

# ***Gestionar repositorio***
#def __init__(RepositorioPort):


