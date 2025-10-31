from ui.io import leer_int, leer_float, leer_texto, leer_texto_opcional, leer_float_opcional, leer_criterio
from ui.printers import print_tabla_estudiantes

class InterfazConsola:
    def __init__(self, gestor):
        self.gestor = gestor
        self._salir = False
        # Diccionario básico: clave = número, valor = (texto, función)
        self.opciones = {
            "1": ("Agregar estudiante", self.op_agregar),
            "2": ("Editar estudiante", self.op_editar),
            "3": ("Eliminar estudiante", self.op_eliminar),
            "4": ("Buscar por ID", self.op_buscar_id),
            "5": ("Buscar por nombre (prefijo)", self.op_buscar_nombre),
            "6": ("Listar ordenado", self.op_listar_ordenado),
            "7": ("Clasificar (aprobado/reprobado)", self.op_clasificar),
            "8": ("Estadísticas", self.op_estadisticas),
            "9": ("Cargar desde repositorio", self.op_cargar),
            "10": ("Guardar en repositorio", self.op_guardar),
            "0": ("Salir", self.op_salir),
        }
    def mostrar_menu(self) -> None:
        print("\n" + "=" * 60)
        print("   GESTIÓN DE ESTUDIANTES — Interfaz de Consola")
        print("=" * 60)
        # imprimimos directamente desde el diccionario para que nunca se desincronicen
        for k in sorted(self.opciones, key=lambda x: int(x) if x.isdigit() else 999):
            etiqueta, _ = self.opciones[k]
            print(f"{k:>2}) {etiqueta}")
        print("-" * 60)

    def ejecutar(self) -> None:
        while not self._salir:
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ").strip()
            action = self.opciones.get(opcion)
            if action:
                try:
                    action[1]() # llamamos directamente la función
                except Exception as e:
                    print(f"⚠️  Error: {e}")
            else:
                print("❌ Opción inválida.")
            if not self._salir:
                input("\nPulsa Enter para continuar...")

    # ------- Acciones del menú -------
    def op_agregar(self):
        print("\n➕ Agregar estudiante")
        id_ = leer_int("ID (entero ≥ 1): ", minimo=1)
        nombre = leer_texto("Nombre: ")
        nota = leer_float("Nota (0-100): ", minimo=0, maximo=100)
        self.gestor.agregar_desde_datos(id_, nombre, nota)
        print(f"✅ Agregado: id={id_}, nombre={nombre}, nota={nota:.2f}")

    def op_editar(self):
        print("\n✏️  Editar estudiante")
        id_ = leer_int("ID a editar (≥1): ", minimo=1)
        print("Deja vacío para no cambiar ese campo.")
        nombre = leer_texto_opcional("Nuevo nombre: ")
        nota   = leer_float_opcional("Nueva nota (0-100): ", minimo=0, maximo=100)
        self.gestor.editar_estudiante(id_, nombre=nombre, nota=nota)
        print("✅ Estudiante actualizado.")

    def op_eliminar(self):
        print("\n🗑️  Eliminar estudiante")
        id_ = leer_int("ID a eliminar (≥1): ", minimo=1)

        # Confirmación previa
        confirmar = input(f"¿Seguro que desea eliminar el estudiante con ID {id_}? (s/N): ").strip().lower()
        if confirmar != "s":
            print("↩️  Operación cancelada.")
            return

        eliminado = self.gestor.eliminar_estudiante(id_)
        if eliminado:
            print("✅ Estudiante eliminado correctamente.")
        else:
            print("⚠️  No existe un estudiante con ese ID.")

    def op_buscar_id(self): print("→ Buscar por ID (siguiente paso).")


    def op_buscar_nombre(self): print("→ Buscar por nombre (siguiente paso).")


    def op_listar_ordenado(self):
        print("\n📋 Listar ordenado")
        orden = leer_criterio(
            "Orden (nombre/nota) [default nombre]: ",
            validos={"nombre", "nota"},
            por_defecto="nombre"
        )
        lista = self.gestor.listar_ordenado(orden)
        print_tabla_estudiantes(lista)

    def op_clasificar(self): print("→ Clasificar (siguiente paso).")


    def op_estadisticas(self): print("→ Estadísticas (siguiente paso).")


    def op_cargar(self): print("→ Cargar (siguiente paso).")


    def op_guardar(self): print("→ Guardar (siguiente paso).")


    def op_salir(self):
        self._salir = True
        print("👋 Saliendo...")










