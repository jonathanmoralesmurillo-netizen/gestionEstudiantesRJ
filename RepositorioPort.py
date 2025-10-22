"""

abc (Abstract Base Classes)
El módulo abc (del inglés Abstract Base Classes)
permite crear clases base que no se pueden instanciar directamente,
sino que sirven como plantillas para otras clases.

"""
from abc import ABC, abstractmethod
from Estudiante import *

class RepositorioPort(ABC):

    @abstractmethod
    def cargar(self)->list[Estudiante]:
        pass

    @abstractmethod
    def guardar(self,estudiantes: list[Estudiante]) -> None:
        pass


