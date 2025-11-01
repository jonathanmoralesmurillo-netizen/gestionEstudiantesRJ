def leer_int(mensaje, minimo=None, maximo=None):
    while True:
        texto = input(mensaje).strip()
        try:
            valor = int(texto)
            if minimo is not None and valor < minimo:
                print(f"❌ Debe ser ≥ {minimo}."); continue
            if maximo is not None and valor > maximo:
                print(f"❌ Debe ser ≤ {maximo}."); continue
            return valor
        except ValueError:
            print("❌ Debes digitar un número entero.")

def leer_float(mensaje, minimo=None, maximo=None):
    while True:
        texto = input(mensaje).strip()
        try:
            valor = float(texto)
            if minimo is not None and valor < minimo:
                print(f"❌ Debe ser ≥ {minimo}."); continue
            if maximo is not None and valor > maximo:
                print(f"❌ Debe ser ≤ {maximo}."); continue
            return valor
        except ValueError:
            print("❌ Debes digitar un número (puede tener decimales).")

def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("❌ El texto no puede estar vacío.")

def leer_texto_opcional(mensaje):
    s = input(mensaje).strip()
    return s if s else None

def leer_float_opcional(mensaje, minimo=None, maximo=None):
    s = input(mensaje).strip()
    if s == "": return None
    try:
        v = float(s)
        if minimo is not None and v < minimo:
            print(f"❌ Debe ser ≥ {minimo}."); return leer_float_opcional(mensaje, minimo, maximo)
        if maximo is not None and v > maximo:
            print(f"❌ Debe ser ≤ {maximo}."); return leer_float_opcional(mensaje, minimo, maximo)
        return v
    except ValueError:
        print("❌ Debes digitar un número (puede tener decimales).")
        return leer_float_opcional(mensaje, minimo, maximo)

def leer_criterio(mensaje, validos: set[str], por_defecto: str):
    while True:
        s = input(mensaje).strip().lower()
        if s == "": return por_defecto
        if s in validos: return s
        print(f"❌ Debe ser uno de: {', '.join(sorted(validos))}")