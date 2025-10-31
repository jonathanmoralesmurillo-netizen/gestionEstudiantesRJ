# ui/printers.py
def print_tabla_estudiantes(lista):
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
    print("-" * 60)