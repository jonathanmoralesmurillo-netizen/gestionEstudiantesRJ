# main.py
from RepositorioCSV import RepositorioCSV
from GestorEstudiantes import GestorEstudiantes
from InterfazConsola import InterfazConsola

if __name__ == "__main__":
    # esqueleto del menú
    repo = RepositorioCSV("estudiantes.csv")
    gestor = GestorEstudiantes(repo)

    ui = InterfazConsola(gestor)
    ui.ejecutar()