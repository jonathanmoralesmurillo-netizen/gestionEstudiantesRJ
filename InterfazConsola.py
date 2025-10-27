

































class InterfazConsola:
    def __init__(self, gestor: GestorEstudiantes):
        self.gestor = gestor
        self.opciones: dict[str, tuple[str, Callable[[], None]]] = {
            #primaria-rita
            "1": ("Agregar estudiante", self.op_agregar),
            "2": ("Editar estudiante", self.op_editar),
            "3": ("Eliminar estudiante", self.op_eliminar),
            "4": ("Buscar por ID", self.op_buscar_id),
            "5": ("Buscar por nombre (prefijo)", self.op_buscar_nombre),
            #secundaria-john
            "6": ("Listar ordenado", self.op_listar_ordenado),
            "7": ("Clasificar (aprobado/reprobado)", self.op_clasificar),
            "8": ("Estadísticas", self.op_estadisticas),
            "9": ("Cargar desde repositorio", self.op_cargar),
            "10": ("Guardar en repositorio", self.op_guardar),
            "0": ("Salir", self.op_salir),
        }
        self._salir = False











