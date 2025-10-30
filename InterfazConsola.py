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

    def _leer_int(self, mensaje, minimo=None, maximo=None):
        while True:
            texto = input(mensaje).strip()
            try:
                valor = int(texto)
                if minimo is not None and valor < minimo:
                    print(f"❌ Debe ser ≥ {minimo}.");
                    continue
                if maximo is not None and valor > maximo:
                    print(f"❌ Debe ser ≤ {maximo}.");
                    continue
                return valor
            except ValueError:
                print("❌ Debes digitar un número entero.")

    def _leer_float(self, mensaje, minimo=None, maximo=None):
        while True:
            texto = input(mensaje).strip()
            try:
                valor = float(texto)
                if minimo is not None and valor < minimo:
                    print(f"❌ Debe ser ≥ {minimo}.");
                    continue
                if maximo is not None and valor > maximo:
                    print(f"❌ Debe ser ≤ {maximo}.");
                    continue
                return valor
            except ValueError:
                print("❌ Debes digitar un número (puede tener decimales).")

    def _leer_texto(self, mensaje):
        while True:
            texto = input(mensaje).strip()
            if texto:
                return texto
            print("❌ El texto no puede estar vacío.")
    # ------- Acciones del menú -------
    def op_agregar(self):
        print("\n➕ Agregar estudiante")
        id_ = self._leer_int("ID (entero ≥ 1): ", minimo=1)
        nombre = self._leer_texto("Nombre: ")
        nota = self._leer_float("Nota (0-100): ", minimo=0, maximo=100)
        self.gestor.agregar_desde_datos(id_, nombre, nota)
        print(f"✅ Agregado: id={id_}, nombre={nombre}, nota={nota:.2f}")

    def op_editar(self): print("→ Editar (siguiente paso).")


    def op_eliminar(self): print("→ Eliminar (siguiente paso).")


    def op_buscar_id(self): print("→ Buscar por ID (siguiente paso).")


    def op_buscar_nombre(self): print("→ Buscar por nombre (siguiente paso).")


    def op_listar_ordenado(self): print("→ Listar ordenado (siguiente paso).")


    def op_clasificar(self): print("→ Clasificar (siguiente paso).")


    def op_estadisticas(self): print("→ Estadísticas (siguiente paso).")


    def op_cargar(self): print("→ Cargar (siguiente paso).")


    def op_guardar(self): print("→ Guardar (siguiente paso).")


    def op_salir(self):
        self._salir = True
        print("👋 Saliendo...")










