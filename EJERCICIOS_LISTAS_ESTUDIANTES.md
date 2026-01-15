# Ejercicios de Listas Enlazadas en C++

## Instrucciones Generales

Este documento contiene 40 ejercicios sobre listas enlazadas en C++ que cubren desde operaciones básicas hasta implementaciones avanzadas. Cada ejercicio debe resolverse implementando las clases y métodos necesarios.

**Requisitos:**
- Implementar todas las clases en archivos separados (.h y .cpp)
- Usar encapsulación adecuada (atributos privados)
- Implementar constructores y destructores cuando sea necesario
- Liberar correctamente la memoria dinámica
- Incluir validaciones de punteros NULL cuando sea apropiado
- Manejar casos especiales (lista vacía, un elemento, etc.)

---

## PARTE I: OPERACIONES BÁSICAS (Ejercicios 1-10)

### Ejercicio 1: Lista de Enteros Básica
Crea una clase `ListaEnteros` que implemente una lista enlazada simple de enteros. Implementa:
- Constructor y destructor
- `bool vacia()`: retorna `true` si la lista está vacía
- `void agregarInicio(int valor)`: agrega un elemento al inicio
- `void agregarFinal(int valor)`: agrega un elemento al final
- `bool eliminaInicio()`: elimina el primer elemento
- `bool eliminaFinal()`: elimina el último elemento
- `string toString()`: retorna una representación en string de la lista
- `int getCantidad()`: retorna el número de elementos

### Ejercicio 2: Lista con Contador
Extiende la clase del Ejercicio 1 con:
- `int obtenerPrimero()`: retorna el valor del primer elemento
- `int obtenerUltimo()`: retorna el valor del último elemento
- `int sumarElementos()`: retorna la suma de todos los elementos
- `double promedio()`: retorna el promedio de los elementos
- `int encontrarMaximo()`: retorna el valor máximo
- `int encontrarMinimo()`: retorna el valor mínimo

### Ejercicio 3: Búsqueda en Lista
Crea una clase `ListaBusqueda` con:
- `bool buscar(int valor)`: retorna `true` si el valor existe
- `int contarApariciones(int valor)`: cuenta cuántas veces aparece un valor
- `int obtenerPosicion(int valor)`: retorna la posición (índice) de un valor, -1 si no existe
- `bool eliminarPorValor(int valor)`: elimina la primera ocurrencia de un valor
- `int eliminarTodasOcurrencias(int valor)`: elimina todas las ocurrencias y retorna cuántas eliminó

### Ejercicio 4: Lista de Caracteres
Crea una clase `ListaCaracteres` que almacene caracteres. Implementa:
- `void agregarInicio(char c)`
- `void agregarFinal(char c)`
- `int contarCaracter(char c)`: cuenta apariciones de un carácter
- `bool esPalindromo()`: verifica si la lista forma un palíndromo
- `string obtenerCadena()`: retorna los caracteres como string
- `void invertir()`: invierte el orden de los elementos

### Ejercicio 5: Lista de Números Reales
Crea una clase `ListaReales` que almacene números `double`. Implementa:
- Operaciones básicas (agregar inicio/final, eliminar inicio/final)
- `double suma()`: suma todos los elementos
- `double promedio()`: promedio de los elementos
- `double producto()`: multiplica todos los elementos
- `int contarPositivos()`: cuenta números positivos
- `int contarNegativos()`: cuenta números negativos
- `double encontrarMayor()`: encuentra el mayor valor
- `double encontrarMenor()`: encuentra el menor valor

### Ejercicio 6: Lista con Operaciones de Pila
Crea una clase `ListaPila` que funcione como una pila (LIFO - Last In First Out):
- `void push(int valor)`: agrega elemento (al inicio)
- `int pop()`: elimina y retorna el último elemento agregado
- `int top()`: retorna el último elemento sin eliminarlo
- `bool estaVacia()`: verifica si está vacía
- `int tamaño()`: retorna el tamaño

### Ejercicio 7: Lista con Operaciones de Cola
Crea una clase `ListaCola` que funcione como una cola (FIFO - First In First Out):
- `void encolar(int valor)`: agrega elemento (al final)
- `int desencolar()`: elimina y retorna el primer elemento
- `int frente()`: retorna el primer elemento sin eliminarlo
- `bool estaVacia()`: verifica si está vacía
- `int tamaño()`: retorna el tamaño

### Ejercicio 8: Lista con Duplicados
Crea una clase `ListaDuplicados` con:
- Operaciones básicas
- `bool tieneDuplicados()`: verifica si hay valores duplicados
- `void eliminarDuplicados()`: elimina todos los duplicados, dejando solo una ocurrencia
- `int contarUnicos()`: cuenta cuántos valores únicos hay
- `ListaDuplicados* obtenerUnicos()`: retorna nueva lista solo con valores únicos

### Ejercicio 9: Lista Ordenada
Crea una clase `ListaOrdenada` que mantenga los elementos ordenados:
- `void insertarOrdenado(int valor)`: inserta manteniendo orden ascendente
- `void insertarOrdenadoDesc(int valor)`: inserta manteniendo orden descendente
- `bool estaOrdenada()`: verifica si la lista está ordenada
- `void ordenar()`: ordena la lista usando algoritmo de burbuja
- `void ordenarDesc()`: ordena en orden descendente

### Ejercicio 10: Lista con Rango
Crea una clase `ListaRango` con:
- Operaciones básicas
- `ListaRango* obtenerRango(int inicio, int fin)`: retorna nueva lista con elementos en el rango
- `void eliminarRango(int inicio, int fin)`: elimina elementos en el rango
- `void insertarEnPosicion(int posicion, int valor)`: inserta en posición específica
- `bool eliminarEnPosicion(int posicion)`: elimina elemento en posición específica
- `int obtenerEnPosicion(int posicion)`: obtiene valor en posición

---

## PARTE II: LISTAS CON OBJETOS (Ejercicios 11-20)

### Ejercicio 11: Lista de Personas
Crea clases `Persona` (nombre, edad, género) y `ListaPersonas`. Implementa:
- `void agregarPersona(Persona* p)`: agrega persona al final
- `Persona* buscarPorNombre(string nombre)`: busca por nombre
- `int contarPorGenero(string genero)`: cuenta personas por género
- `double promedioEdades()`: promedio de edades
- `Persona* personaMasJoven()`: retorna la persona más joven
- `Persona* personaMasVieja()`: retorna la persona más vieja
- `int contarMayoresDe(int edad)`: cuenta personas mayores a una edad

### Ejercicio 12: Lista de Estudiantes
Crea clases `Estudiante` (nombre, carnet, promedio) y `ListaEstudiantes`. Implementa:
- `void agregarEstudiante(Estudiante* e)`
- `Estudiante* buscarPorCarnet(string carnet)`
- `double promedioGrupo()`: promedio general del grupo
- `int contarAprobados(double notaMinima)`: cuenta aprobados
- `Estudiante* mejorEstudiante()`: retorna estudiante con mejor promedio
- `int contarReprobados(double notaMinima)`: cuenta reprobados
- `void aplicarCurva(double porcentaje)`: aumenta todas las notas en un porcentaje

### Ejercicio 13: Lista de Productos
Crea clases `Producto` (codigo, nombre, precio, stock) y `ListaProductos`. Implementa:
- `void agregarProducto(Producto* p)`
- `Producto* buscarPorCodigo(string codigo)`
- `double valorTotalInventario()`: suma precio * stock de todos
- `Producto* productoMasCaro()`: retorna producto más caro
- `int productosConStockBajo(int limite)`: cuenta productos con stock bajo
- `bool actualizarStock(string codigo, int nuevoStock)`: actualiza stock
- `double gananciaTotal()`: suma precio * stock de todos

### Ejercicio 14: Lista de Libros
Crea clases `Libro` (ISBN, titulo, autor, año, disponible) y `ListaBiblioteca`. Implementa:
- `void agregarLibro(Libro* l)`
- `Libro* buscarPorISBN(string isbn)`
- `Libro* buscarPorTitulo(string titulo)`
- `int contarLibrosPorAutor(string autor)`: cuenta libros de un autor
- `int contarDisponibles()`: cuenta libros disponibles
- `bool prestarLibro(string isbn)`: marca libro como prestado
- `bool devolverLibro(string isbn)`: marca libro como disponible
- `ListaBiblioteca* librosPorAutor(string autor)`: retorna lista de libros de un autor

### Ejercicio 15: Lista de Carros
Crea clases `Carro` (placa, marca, año, precio) y `ListaCarros`. Implementa:
- `void insertarOrdenado(Carro* c)`: inserta ordenado por año
- `bool eliminarPorPlaca(string placa)`: elimina por placa
- `Carro* buscarPorPlaca(string placa)`
- `int contarPorMarca(string marca)`: cuenta carros de una marca
- `Carro* carroMasViejo()`: retorna carro más antiguo
- `Carro* carroMasNuevo()`: retorna carro más reciente
- `double precioPromedio()`: precio promedio de todos los carros

### Ejercicio 16: Lista de Empleados
Crea clases `Empleado` (id, nombre, salario, departamento) y `ListaEmpleados`. Implementa:
- `void agregarEmpleado(Empleado* e)`
- `Empleado* buscarPorId(int id)`
- `double salarioPromedio()`: salario promedio
- `double salarioTotal()`: suma de todos los salarios
- `int contarPorDepartamento(string depto)`: cuenta por departamento
- `Empleado* empleadoMejorPagado()`: retorna empleado con mayor salario
- `ListaEmpleados* empleadosPorDepartamento(string depto)`: retorna lista filtrada

### Ejercicio 17: Lista de Facturas
Crea clases `Factura` (numero, cliente, monto, fecha) y `ListaFacturas`. Implementa:
- `void agregarFactura(Factura* f)`
- `Factura* buscarPorNumero(int numero)`
- `double montoTotal()`: suma de todos los montos
- `double montoPromedio()`: monto promedio
- `int contarPorCliente(string cliente)`: cuenta facturas de un cliente
- `Factura* facturaMayor()`: retorna factura con mayor monto
- `double totalPorCliente(string cliente)`: suma montos de un cliente

### Ejercicio 18: Lista de Reservas
Crea clases `Reserva` (id, cliente, fecha, monto, estado) y `ListaReservas`. Implementa:
- `void agregarReserva(Reserva* r)`
- `Reserva* buscarPorId(int id)`
- `int contarPorEstado(string estado)`: cuenta por estado (confirmada, cancelada, etc.)
- `double montoTotalReservas()`: suma de montos
- `bool cambiarEstado(int id, string nuevoEstado)`: cambia estado de reserva
- `ListaReservas* reservasPorCliente(string cliente)`: retorna lista filtrada
- `int contarConfirmadas()`: cuenta reservas confirmadas

### Ejercicio 19: Lista de Cursos
Crea clases `Curso` (codigo, nombre, creditos, profesor) y `ListaCursos`. Implementa:
- `void agregarCurso(Curso* c)`
- `Curso* buscarPorCodigo(string codigo)`
- `int totalCreditos()`: suma de créditos de todos los cursos
- `int contarPorProfesor(string profesor)`: cuenta cursos de un profesor
- `ListaCursos* cursosPorProfesor(string profesor)`: retorna lista filtrada
- `Curso* cursoConMasCreditos()`: retorna curso con más créditos
- `double promedioCreditos()`: promedio de créditos

### Ejercicio 20: Lista de Transacciones
Crea clases `Transaccion` (id, tipo, monto, fecha) y `ListaTransacciones`. Implementa:
- `void agregarTransaccion(Transaccion* t)`
- `Transaccion* buscarPorId(int id)`
- `double montoTotal()`: suma de todos los montos
- `double montoPorTipo(string tipo)`: suma montos de un tipo específico
- `int contarPorTipo(string tipo)`: cuenta transacciones de un tipo
- `Transaccion* transaccionMayor()`: retorna transacción con mayor monto
- `ListaTransacciones* transaccionesPorTipo(string tipo)`: retorna lista filtrada

---

## PARTE III: OPERACIONES AVANZADAS (Ejercicios 21-30)

### Ejercicio 21: Invertir Lista
Crea una clase `ListaInvertir` con operaciones básicas y:
- `void invertir()`: invierte el orden de los elementos
- `ListaInvertir* obtenerInversa()`: retorna nueva lista invertida sin modificar la original
- `bool esPalindromo()`: verifica si la lista es igual a su inversa
- `void invertirRango(int inicio, int fin)`: invierte solo un rango de elementos

### Ejercicio 22: Comparar Listas
Crea una clase `ListaComparar` con:
- Operaciones básicas
- `bool sonIguales(ListaComparar* otra)`: compara si dos listas son iguales
- `bool contiene(ListaComparar* otra)`: verifica si esta lista contiene todos los elementos de otra
- `ListaComparar* diferencia(ListaComparar* otra)`: retorna elementos que están en esta pero no en otra
- `ListaComparar* interseccion(ListaComparar* otra)`: retorna elementos comunes

### Ejercicio 23: Concatenar Listas
Crea una clase `ListaConcatenar` con:
- Operaciones básicas
- `void concatenar(ListaConcatenar* otra)`: agrega todos los elementos de otra lista
- `ListaConcatenar* unir(ListaConcatenar* otra)`: retorna nueva lista con ambas unidas
- `void insertarLista(int posicion, ListaConcatenar* otra)`: inserta otra lista en posición específica

### Ejercicio 24: Dividir Lista
Crea una clase `ListaDividir` con:
- Operaciones básicas
- `ListaDividir* dividir(int posicion)`: divide la lista en dos partes en una posición
- `ListaDividir* obtenerPrimeraMitad()`: retorna primera mitad
- `ListaDividir* obtenerSegundaMitad()`: retorna segunda mitad
- `void eliminarMitad()`: elimina la segunda mitad de la lista

### Ejercicio 25: Rotar Lista
Crea una clase `ListaRotar` con:
- Operaciones básicas
- `void rotarIzquierda(int posiciones)`: rota elementos hacia la izquierda
- `void rotarDerecha(int posiciones)`: rota elementos hacia la derecha
- `void rotarHasta(int valor)`: rota hasta que un valor específico esté al inicio

### Ejercicio 26: Ordenar Lista
Crea una clase `ListaOrdenar` con:
- Operaciones básicas
- `void ordenarBurbuja()`: ordena usando bubble sort
- `void ordenarSeleccion()`: ordena usando selection sort
- `void ordenarInsercion()`: ordena usando insertion sort
- `bool estaOrdenada()`: verifica si está ordenada

### Ejercicio 27: Filtrar Lista
Crea una clase `ListaFiltrar` con:
- Operaciones básicas
- `ListaFiltrar* filtrarPares()`: retorna lista solo con números pares
- `ListaFiltrar* filtrarImpares()`: retorna lista solo con números impares
- `ListaFiltrar* filtrarMayores(int valor)`: retorna elementos mayores a un valor
- `ListaFiltrar* filtrarMenores(int valor)`: retorna elementos menores a un valor

### Ejercicio 28: Estadísticas Avanzadas
Crea una clase `ListaEstadisticas` con:
- Operaciones básicas
- `int moda()`: retorna el valor que más se repite
- `double mediana()`: retorna el valor medio
- `double desviacionEstandar()`: calcula desviación estándar
- `int rango()`: diferencia entre máximo y mínimo
- `ListaEstadisticas* obtenerTopN(int n)`: retorna los N mayores valores

### Ejercicio 29: Lista con Historial
Crea una clase `ListaHistorial` que mantenga un historial de cambios:
- Operaciones básicas
- `void deshacer()`: deshace la última operación
- `void rehacer()`: rehace la última operación deshecha
- `int historialDisponible()`: cuenta operaciones que se pueden deshacer
- `void limpiarHistorial()`: limpia el historial

### Ejercicio 30: Lista Circular Simple
Crea una clase `ListaCircular` que implemente una lista circular:
- `void agregar(int valor)`: agrega elemento
- `bool eliminar(int valor)`: elimina elemento específico
- `void recorrerCompleto()`: recorre toda la lista una vez
- `int contarElementos()`: cuenta elementos
- `bool buscar(int valor)`: busca elemento
- **Nota**: En lista circular, el último nodo apunta al primero

---

## PARTE IV: SISTEMAS COMPLEJOS (Ejercicios 31-40)

### Ejercicio 31: Sistema de Biblioteca Completo
Crea un sistema completo de biblioteca con:
- Clase `Libro` (ISBN, titulo, autor, año, disponible, categoria)
- Clase `ListaBiblioteca` con todas las operaciones necesarias
- `void prestarLibro(string isbn, string usuario)`
- `void devolverLibro(string isbn)`
- `int contarDisponibles()`
- `int contarPrestados()`
- `ListaBiblioteca* librosPorCategoria(string categoria)`
- `ListaBiblioteca* librosPorAutor(string autor)`
- `double valorTotalBiblioteca()`
- `Libro* libroMasAntiguo()`
- `Libro* libroMasReciente()`

### Ejercicio 32: Sistema de Inventario de Tienda
Crea un sistema de inventario con:
- Clase `Producto` (codigo, nombre, precio, stock, categoria, proveedor)
- Clase `ListaInventario` con operaciones completas
- `void agregarProducto(Producto* p)`
- `bool venderProducto(string codigo, int cantidad)`: reduce stock
- `bool reponerProducto(string codigo, int cantidad)`: aumenta stock
- `int productosAgotados()`: cuenta productos con stock 0
- `double valorTotalInventario()`
- `ListaInventario* productosPorCategoria(string categoria)`
- `ListaInventario* productosPorProveedor(string proveedor)`
- `Producto* productoMasVendido()` (requiere agregar contador de ventas)

### Ejercicio 33: Sistema de Gestión de Estudiantes
Crea un sistema completo de estudiantes con:
- Clase `Estudiante` (carnet, nombre, edad, promedio, carrera, semestre)
- Clase `ListaEstudiantes` con operaciones avanzadas
- `void agregarEstudiante(Estudiante* e)`
- `Estudiante* buscarPorCarnet(string carnet)`
- `double promedioGeneral()`: promedio de todos
- `double promedioPorCarrera(string carrera)`: promedio de una carrera
- `int contarPorCarrera(string carrera)`
- `int contarPorSemestre(int semestre)`
- `ListaEstudiantes* estudiantesAprobados(double notaMinima)`
- `Estudiante* mejorEstudiantePorCarrera(string carrera)`
- `void aplicarCurva(double porcentaje)`: aumenta todas las notas

### Ejercicio 34: Sistema de Reservas de Hotel
Crea un sistema de reservas con:
- Clase `Reserva` (id, cliente, fechaEntrada, fechaSalida, habitacion, monto, estado)
- Clase `ListaReservas` con operaciones completas
- `void crearReserva(Reserva* r)`
- `bool cancelarReserva(int id)`: cambia estado a cancelada
- `bool confirmarReserva(int id)`: cambia estado a confirmada
- `double ingresosTotales()`: suma de montos de reservas confirmadas
- `int contarReservasActivas()`: cuenta reservas confirmadas
- `ListaReservas* reservasPorCliente(string cliente)`
- `ListaReservas* reservasPorFecha(string fecha)`
- `Reserva* reservaConMayorMonto()`

### Ejercicio 35: Sistema de Facturación
Crea un sistema de facturación con:
- Clase `LineaFactura` (producto, cantidad, precioUnitario, subtotal)
- Clase `Factura` (numero, cliente, fecha, listaLineas, total)
- Clase `ListaFacturas` para gestionar facturas
- `void agregarFactura(Factura* f)`
- `Factura* buscarPorNumero(int numero)`
- `double totalFacturado()`: suma de todos los totales
- `double totalPorCliente(string cliente)`
- `int contarFacturasPorCliente(string cliente)`
- `Factura* facturaMayor()`
- `double promedioFacturacion()`
- `ListaFacturas* facturasPorFecha(string fecha)`

### Ejercicio 36: Sistema de Gestión de Empleados
Crea un sistema completo de empleados con:
- Clase `Empleado` (id, nombre, salario, departamento, cargo, fechaIngreso)
- Clase `ListaEmpleados` con operaciones avanzadas
- `void contratarEmpleado(Empleado* e)`
- `bool despedirEmpleado(int id)`: elimina empleado
- `double salarioPromedio()`: promedio general
- `double salarioPromedioPorDepto(string depto)`: promedio por departamento
- `double salarioTotal()`: suma de todos los salarios
- `Empleado* empleadoMejorPagado()`
- `Empleado* empleadoMejorPagadoPorDepto(string depto)`
- `int contarPorDepartamento(string depto)`
- `ListaEmpleados* empleadosPorDepartamento(string depto)`
- `void aumentarSalario(double porcentaje)`: aumenta todos los salarios

### Ejercicio 37: Sistema de Gestión de Cursos Académicos
Crea un sistema académico con:
- Clase `Curso` (codigo, nombre, creditos, profesor, horario, aula)
- Clase `ListaCursos` con operaciones completas
- `void agregarCurso(Curso* c)`
- `Curso* buscarPorCodigo(string codigo)`
- `int totalCreditos()`: suma de créditos
- `int contarPorProfesor(string profesor)`
- `ListaCursos* cursosPorProfesor(string profesor)`
- `Curso* cursoConMasCreditos()`
- `bool hayConflictoHorario(Curso* c)`: verifica si hay solapamiento
- `double promedioCreditos()`
- `int contarCursosPorHorario(string horario)`

### Ejercicio 38: Sistema de Transacciones Bancarias
Crea un sistema bancario con:
- Clase `Transaccion` (id, tipo, monto, fecha, cuentaOrigen, cuentaDestino)
- Clase `ListaTransacciones` con operaciones avanzadas
- `void registrarTransaccion(Transaccion* t)`
- `Transaccion* buscarPorId(int id)`
- `double montoTotal()`: suma de todos los montos
- `double montoPorTipo(string tipo)`: suma por tipo (deposito, retiro, transferencia)
- `int contarPorTipo(string tipo)`
- `double montoPorCuenta(string cuenta)`: suma de transacciones de una cuenta
- `Transaccion* transaccionMayor()`
- `ListaTransacciones* transaccionesPorFecha(string fecha)`
- `ListaTransacciones* transaccionesPorCuenta(string cuenta)`

### Ejercicio 39: Sistema de Gestión de Proyectos
Crea un sistema de proyectos con:
- Clase `Tarea` (id, descripcion, estado, responsable, fechaLimite, prioridad)
- Clase `Proyecto` (codigo, nombre, listaTareas, fechaInicio, fechaFin)
- Clase `ListaProyectos` para gestionar proyectos
- `void agregarProyecto(Proyecto* p)`
- `Proyecto* buscarPorCodigo(string codigo)`
- `int contarTareasPorEstado(string estado)`: cuenta tareas en un estado
- `int contarTareasPorResponsable(string responsable)`
- `ListaProyectos* proyectosPorEstado(string estado)`
- `Proyecto* proyectoConMasTareas()`
- `void agregarTareaAProyecto(string codigo, Tarea* t)`
- `bool completarTarea(string codigoProyecto, int idTarea)`

### Ejercicio 40: Sistema Completo de Venta de Entradas
Crea un sistema de venta de entradas con:
- Clase `Evento` (id, nombre, fecha, lugar, capacidad, precioEntrada)
- Clase `Entrada` (numero, evento, cliente, fechaVenta, precioPagado)
- Clase `ListaEventos` para gestionar eventos
- Clase `ListaEntradas` para gestionar entradas vendidas
- `void crearEvento(Evento* e)`
- `bool venderEntrada(string idEvento, Entrada* ent)`: vende entrada si hay capacidad
- `int entradasVendidas(string idEvento)`: cuenta entradas vendidas de un evento
- `int entradasDisponibles(string idEvento)`: capacidad - vendidas
- `double ingresosTotales()`: suma de todas las entradas vendidas
- `double ingresosPorEvento(string idEvento)`: ingresos de un evento
- `Evento* eventoMasVendido()`: evento con más entradas vendidas
- `ListaEntradas* entradasPorCliente(string cliente)`
- `bool cancelarEntrada(int numeroEntrada)`: elimina entrada vendida

---

## Notas Finales

- Todos los ejercicios deben incluir un programa `main.cpp` que demuestre el funcionamiento
- Implementa validaciones de punteros NULL para evitar crashes
- Asegúrate de liberar correctamente toda la memoria dinámica
- Maneja casos especiales: lista vacía, un elemento, elemento no encontrado
- Usa nombres descriptivos para variables y métodos
- Incluye comentarios donde sea necesario para claridad
- Prueba tus implementaciones con diferentes casos de uso
- Para ejercicios con objetos, decide si el nodo debe eliminar el objeto o la lista

**¡Buena suerte con los ejercicios!**
