import csv
import logging
from typing import List
from abc import ABC
from Estudiante import Estudiante
from RepositorioPort import *
import csv
import logging
from abc import ABC, abstractmethod
from Estudiante import Estudiante  # Asegúrate de tener esta clase definida en otro archivo


class RepositorioCSV(ABC):
    """
    Inicializar el repositorio CSV.

    Args:
        ruta (str): Ruta del archivo CSV
    """

    _ruta: str

    def __init__(self, ruta: str):
        self._ruta = ruta
        self._configurar_logging()

    def _configurar_logging(self) -> None:
        """Configurar el registro para el seguimiento de errores."""
        logging.basicConfig(
            filename='errores.log',
            level=logging.ERROR,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

    def cargar(self) -> list[Estudiante]:
        """
        Cargar estudiantes desde un archivo CSV.

        Returns:
            list[Estudiante]: Lista de estudiantes cargados.

        Raises:
            Excepción: Si falla la lectura del archivo.
        """
        lista_estudiantes = []
        try:
            with open(self.ruta, 'r', newline='', encoding='utf-8') as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    try:
                        id_estudiante = int(fila['id'])
                        nombre_estudiante = fila['nombre']
                        nota_estudiante = float(fila['nota'])
                        estudiante = Estudiante(id_estudiante, nombre_estudiante, nota_estudiante)
                        lista_estudiantes.append(estudiante)
                    except ValueError as e:
                        logging.error(f"Error en datos de fila: {fila} - {e}")
        except FileNotFoundError:
            logging.error(f"No existe el archivo: {self.ruta}")
            self._crear_archivo_vacio()
        except Exception as e:
            logging.error(f"Error al cargar el archivo: {self.ruta} - {e}")
            raise
        return lista_estudiantes

    def _crear_archivo_vacio(self) -> None:
        """Crear el archivo vacío."""
        try:
            with open(self.ruta, 'w', newline='', encoding='utf-8') as archivo:
                campos = ['id', 'nombre', 'nota']
                escritor = csv.DictWriter(archivo, fieldnames=campos)
                escritor.writeheader()
        except Exception as e:
            logging.error(f"Error al crear el archivo vacío {self.ruta}: {e}")
            raise

    def guardar(self, estudiantes: List[Estudiante]) -> None:
        """
        Save students to CSV file.

        Args:
            estudiantes (List[Estudiante]): lista de estudiantes guardados

        Raises:
            Exception: If file writing fails
        """
        try:
            with open(self._ruta, 'w', newline='', encoding='utf-8') as archivo:
                if estudiantes:
                    campos = ['id', 'nombre', 'nota']
                    escritor = csv.DictWriter(archivo, fieldnames=campos)
                    escritor.writeheader()

                    for estudiante in estudiantes:
                        escritor.writerow(estudiante.to_dict())
                else:
                    # Si no hay estudiantes, crear archivo con solo el header
                    campos = ['id', 'nombre', 'nota']
                    escritor = csv.DictWriter(archivo, fieldnames=campos)
                    escritor.writeheader()
        except Exception as e:
            logging.error(f"Error saving CSV file {self._ruta}: {e}")
            raise

    def cargar(self) -> List[Estudiante]:
        """
        Load students from CSV file.

        Returns:
            List[Estudiante]: List of loaded students

        Raises:
            Exception: If file reading fails
        """
        estudiantes = []
        try:
            with open(self._ruta, 'r', newline='', encoding='utf-8') as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    try:
                        id_estudiante = int(fila['id'])
                        nombre = fila['nombre']
                        nota = float(fila['nota'])
                        estudiante = Estudiante(id_estudiante, nombre, nota)
                        estudiantes.append(estudiante)
                    except (ValueError, KeyError) as e:
                        logging.error(f"Error parsing row {fila}: {e}")
                        continue
        except FileNotFoundError:
            # Si el archivo no existe, crear uno vacío
            logging.info(f"CSV file {self._ruta} not found, creating empty file")
            self._crear_archivo_vacio()
        except Exception as e:
            logging.error(f"Error loading CSV file {self._ruta}: {e}")
            raise

        return estudiantes


"""   class RepositorioCSV {
        -ruta: str listo
        +__init__(ruta: str) listo 
        +cargar() list[Estudiante]
        +guardar(estudiantes: list[Estudiante]) void
        -_configurar_logging() void listo
        -_crear_archivo_vacio() void listo 
    }
"""

"""| Marcador        | Significado                                                                         | Ejemplo                                |
                    | --------------- | ----------------------------------------------------------------------------------- | -------------------------------------- |
                    | `%(asctime)s`   | Fecha y hora en que ocurrió el evento                                               | `2025-10-22 04:31:05,348`              |
                    | `%(name)s`      | Nombre del *logger* (por defecto, el nombre del módulo)                             | `__main__` o `GestorEstudiantes`       |
                    | `%(levelname)s` | Nivel del log (ERROR, WARNING, INFO, etc.)                                          | `ERROR`                                |
                    | `%(message)s`   | El mensaje que tú escribes en el `logging.error(...)`, `logging.warning(...)`, etc. | `Error al conectar a la base de datos` |
                    """

