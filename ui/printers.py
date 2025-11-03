# ui/printers.py
"""def print_tabla_estudiantes(lista):
    if not lista:
        print("(sin registros)"); return
    print("-" * 60)
    print(f"{'ID':>5}  {'Nombre':<30}  {'Nota':>6}")
    print("-" * 60)
    # Soporta clase con getters o atributos directos
    for e in lista:
        get_id = e.getId() if hasattr(e, "getId") else getattr(e, "id", None)
        get_nombre = e.getNombre() if hasattr(e, "getNombre") else getattr(e, "nombre", "")
        get_nota = e.getNota() if hasattr(e, "getNota") else getattr(e, "nota", 0.0)
        print(f"{get_id:>5}  {str(get_nombre)[:30]:<30}  {get_nota:>6.2f}")
    print("-" * 60)"""

def print_tabla_estudiante(estudiante):
    # Si no es una secuencia (lista/tupla), lo convertimos en lista
    get_id = estudiante.getId()
    get_nombre = estudiante.getId()
    get_nota = estudiante.getId()
    print(estudiante)




def print_tabla_estudiantes(lista):
    """
    Print a formatted table of students.
    Supports objects with getters (getId/getNombre/getNota),
    plain attributes (id/nombre/nota), and dicts.
    """
    if not lista:
        print("(sin registros)")
        return

    def _to_float(x, default=0.0):
        try:
            return float(x)
        except (TypeError, ValueError):
            return default

    print("-" * 60)
    print(f"{'ID':>5}  {'Nombre':<30}  {'Nota':>6}")
    print("-" * 60)

    for e in lista:
        # ID
        if hasattr(e, "getId"):
            id_val = e.getId()
        elif hasattr(e, "id"):
            id_val = getattr(e, "id", "")
        elif isinstance(e, dict):
            id_val = e.get("id", "")
        else:
            id_val = ""

        # Nombre
        if hasattr(e, "getNombre"):
            nombre_val = e.getNombre()
        elif hasattr(e, "nombre"):
            nombre_val = getattr(e, "nombre", "")
        elif isinstance(e, dict):
            nombre_val = e.get("nombre", "")
        else:
            nombre_val = ""

        # Nota
        if hasattr(e, "getNota"):
            nota_val = e.getNota()
        elif hasattr(e, "nota"):
            nota_val = getattr(e, "nota", 0.0)
        elif isinstance(e, dict):
            nota_val = e.get("nota", 0.0)
        else:
            nota_val = 0.0

        # Coerciones seguras
        id_str = str(id_val) if id_val is not None else ""
        nombre_str = str(nombre_val) if nombre_val is not None else ""
        nota_float = _to_float(nota_val, 0.0)

        print(f"{id_str:>5}  {nombre_str[:30]:<30}  {nota_float:>6.2f}")

    print("-" * 60)


def print_tabla_estudiantes_obj(estudiantes):
    # Si no es una secuencia (lista/tupla), lo convertimos en lista

    print(estudiantes)
    if not isinstance(estudiantes, (list, tuple)):
        estudiantes = [estudiantes]

    filas = []
    for e in estudiantes:
        # Llama a los métodos si existen; si no, usa valores seguros
        get_id = getattr(e, "getId", lambda: None)
        get_nombre = getattr(e, "getNombre", lambda: None)
        get_nota = getattr(e, "getNota", lambda: None)

        filas.append((get_id(), get_nombre(), get_nota()))

    print_tabla_estudiantes(filas)





