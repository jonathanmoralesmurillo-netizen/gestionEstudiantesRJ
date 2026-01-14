# Ejercicios de Matrices en C++

## Instrucciones Generales

Este documento contiene 30 ejercicios sobre matrices en C++ que cubren tanto matrices automáticas (estáticas) como matrices dinámicas. Cada ejercicio debe resolverse implementando las clases y métodos necesarios.

**Requisitos:**
- Implementar todas las clases en archivos separados (.h y .cpp)
- Usar encapsulación adecuada (atributos privados)
- Implementar constructores y destructores cuando sea necesario
- Liberar correctamente la memoria dinámica
- Incluir validaciones de índices cuando sea apropiado

---

## PARTE I: MATRICES AUTOMÁTICAS (Estáticas)

### Ejercicio 1: Matriz de Enteros Básica
Crea una clase `MatrizEnteros` que contenga una matriz estática de 5x5 de enteros. Implementa los siguientes métodos:
- Constructor que inicialice todos los valores en 0
- `insertar(int fila, int columna, int valor)`: inserta un valor en una posición específica
- `obtener(int fila, int columna)`: retorna el valor en una posición específica
- `toString()`: retorna una representación en string de la matriz
- `limpiar()`: establece todos los valores en 0

### Ejercicio 2: Búsqueda en Matriz
Extiende la clase del Ejercicio 1 con los siguientes métodos:
- `buscar(int valor)`: retorna `true` si el valor existe en la matriz, `false` en caso contrario
- `contarApariciones(int valor)`: retorna el número de veces que aparece un valor en la matriz
- `buscarEnFila(int fila, int valor)`: retorna `true` si el valor existe en la fila especificada
- `buscarEnColumna(int columna, int valor)`: retorna `true` si el valor existe en la columna especificada

### Ejercicio 3: Operaciones con Filas y Columnas
Crea una clase `MatrizOperaciones` con una matriz de 4x4. Implementa:
- `llenarFila(int fila, int valor)`: llena una fila completa con un valor específico
- `llenarColumna(int columna, int valor)`: llena una columna completa con un valor específico
- `sumarFila(int fila)`: retorna la suma de todos los elementos de una fila
- `sumarColumna(int columna)`: retorna la suma de todos los elementos de una columna
- `promedioFila(int fila)`: retorna el promedio de los elementos de una fila

### Ejercicio 4: Matriz de Caracteres
Crea una clase `MatrizCaracteres` con una matriz de 3x3 de caracteres. Implementa:
- Constructor que inicialice todos los caracteres en espacio (' ')
- `insertarCaracter(int fila, int columna, char c)`: inserta un carácter en una posición
- `contarCaracter(char c)`: cuenta cuántas veces aparece un carácter en la matriz
- `verificarFilaIgual(int fila)`: retorna `true` si todos los caracteres de una fila son iguales

### Ejercicio 5: Matriz de Puntuaciones
Crea una clase `Puntuaciones` que almacene las puntuaciones de 5 estudiantes en 3 exámenes (matriz 5x3). Implementa:
- `agregarPuntuacion(int estudiante, int examen, double puntuacion)`
- `promedioEstudiante(int estudiante)`: retorna el promedio de un estudiante
- `promedioExamen(int examen)`: retorna el promedio de un examen
- `mejorEstudiante()`: retorna el índice del estudiante con mejor promedio

### Ejercicio 6: Matriz de Temperaturas
Crea una clase `Temperaturas` que almacene temperaturas de 7 días de la semana y 4 ciudades (matriz 7x4). Implementa:
- `registrarTemperatura(int dia, int ciudad, double temp)`
- `temperaturaPromedioCiudad(int ciudad)`: promedio de una ciudad durante la semana
- `diaMasCaliente()`: retorna el índice del día más caliente (promedio de todas las ciudades)
- `ciudadMasFria()`: retorna el índice de la ciudad más fría (promedio de todos los días)

### Ejercicio 7: Matriz Simétrica
Crea una clase `MatrizSimetrica` de 4x4. Implementa:
- `esSimetrica()`: retorna `true` si la matriz es simétrica (m[i][j] == m[j][i])
- `transponer()`: transpone la matriz (intercambia filas por columnas)
- `esDiagonal()`: retorna `true` si todos los elementos fuera de la diagonal principal son 0

### Ejercicio 8: Matriz de Inventario
Crea una clase `Inventario` que almacene cantidades de productos en diferentes almacenes (matriz 6x5). Implementa:
- `agregarCantidad(int producto, int almacen, int cantidad)`
- `totalProducto(int producto)`: suma total de un producto en todos los almacenes
- `totalAlmacen(int almacen)`: suma total de un almacén
- `almacenConMasProductos()`: retorna el índice del almacén con más productos totales

### Ejercicio 9: Matriz de Horarios
Crea una clase `Horario` que represente un horario semanal de clases (7 días x 8 horas). Implementa:
- `agregarClase(int dia, int hora, string nombreClase)`
- `clasesPorDia(int dia)`: retorna el número de clases en un día
- `diaMasOcupado()`: retorna el índice del día con más clases
- `estaLibre(int dia, int hora)`: retorna `true` si no hay clase en ese horario

### Ejercicio 10: Matriz de Asientos
Crea una clase `SalaCine` que represente una sala de cine de 10 filas x 15 columnas. Implementa:
- `reservarAsiento(int fila, int columna)`: marca un asiento como ocupado (1) o libre (0)
- `asientosDisponibles()`: retorna el número de asientos libres
- `filaCompleta(int fila)`: retorna `true` si todos los asientos de una fila están ocupados
- `mejorFila()`: retorna el índice de la fila con más asientos libres

---

## PARTE II: MATRICES DINÁMICAS CON OBJETOS ESTÁTICOS

### Ejercicio 11: Matriz Dinámica de Enteros
Crea una clase `MatrizDinamica` que cree una matriz dinámica de enteros. El constructor debe recibir el número de filas y columnas. Implementa:
- Constructor que reciba filas y columnas
- Destructor que libere la memoria correctamente
- `insertar(int fila, int columna, int valor)`
- `obtener(int fila, int columna)`
- `toString()`

### Ejercicio 12: Matriz Dinámica de Personas
Crea una clase `Persona` con atributos: nombre (string) y edad (int). Luego crea una clase `ColeccionPersonas` que contenga una matriz dinámica de objetos `Persona`. Implementa:
- Constructor que reciba filas y columnas
- Destructor adecuado
- `agregarPersona(int fila, int columna, string nombre, int edad)`
- `personaMasJoven()`: retorna la persona con menor edad
- `promedioEdades()`: retorna el promedio de todas las edades

### Ejercicio 13: Matriz Dinámica de Productos
Crea una clase `Producto` con: nombre (string), precio (double) y stock (int). Crea una clase `InventarioDinamico` con matriz dinámica de `Producto`. Implementa:
- `agregarProducto(int fila, int columna, string nombre, double precio, int stock)`
- `valorTotalInventario()`: suma precio * stock de todos los productos
- `productoMasCaro()`: retorna el producto con mayor precio
- `productosConStockBajo(int limite)`: retorna el número de productos con stock menor al límite

### Ejercicio 14: Matriz Dinámica de Estudiantes
Crea una clase `Estudiante` con: nombre (string) y calificaciones (arreglo de 5 doubles). Crea una clase `Grupo` con matriz dinámica de `Estudiante`. Implementa:
- `agregarEstudiante(int fila, int columna, string nombre, double calificaciones[])`
- `promedioGrupo()`: promedio general de todos los estudiantes
- `mejorPromedio()`: retorna el estudiante con mejor promedio
- `estudiantesAprobados(double notaMinima)`: cuenta estudiantes con promedio >= notaMinima

### Ejercicio 15: Matriz Dinámica de Libros
Crea una clase `Libro` con: titulo (string), autor (string) y año (int). Crea una clase `Biblioteca` con matriz dinámica de `Libro`. Implementa:
- `agregarLibro(int fila, int columna, string titulo, string autor, int año)`
- `buscarPorAutor(string autor)`: retorna el número de libros de un autor
- `librosAntiguos(int añoLimite)`: cuenta libros anteriores a un año
- `libroMasReciente()`: retorna el libro con año más reciente

---

## PARTE III: MATRICES DINÁMICAS CON PUNTEROS A OBJETOS

### Ejercicio 16: Matriz de Punteros a Enteros
Crea una clase `MatrizPunteros` que cree una matriz dinámica de punteros a enteros. Implementa:
- Constructor que reciba filas y columnas y cree la matriz de punteros
- Destructor que libere correctamente toda la memoria
- `asignarValor(int fila, int columna, int valor)`: crea un nuevo entero y lo asigna
- `obtenerValor(int fila, int columna)`: retorna el valor apuntado
- `toString()`

### Ejercicio 17: Matriz de Punteros a Personas
Crea una clase `ColeccionPersonasPunteros` con matriz dinámica de punteros a objetos `Persona`. Implementa:
- Constructor y destructor adecuados
- `agregarPersona(int fila, int columna, string nombre, int edad)`: crea un nuevo objeto Persona
- `eliminarPersona(int fila, int columna)`: elimina y libera la memoria de una persona
- `personaMasVieja()`: retorna la persona con mayor edad
- `contarPersonas()`: retorna el número de personas no nulas

### Ejercicio 18: Matriz de Punteros a Productos
Crea una clase `Tienda` con matriz dinámica de punteros a `Producto`. Implementa:
- `agregarProducto(int fila, int columna, string nombre, double precio, int stock)`
- `eliminarProducto(int fila, int columna)`
- `buscarProducto(string nombre)`: retorna `true` si existe un producto con ese nombre
- `actualizarStock(int fila, int columna, int nuevoStock)`
- `productosAgotados()`: cuenta productos con stock = 0

### Ejercicio 19: Matriz de Punteros a Estudiantes
Crea una clase `Aula` con matriz dinámica de punteros a `Estudiante`. Implementa:
- `agregarEstudiante(int fila, int columna, string nombre, double calificaciones[])`
- `eliminarEstudiante(int fila, int columna)`
- `promedioAula()`: promedio de todos los estudiantes
- `mejorEstudiante()`: retorna el estudiante con mejor promedio
- `reemplazarEstudiante(int fila, int columna, string nombre, double calificaciones[])`: elimina el anterior y agrega uno nuevo

### Ejercicio 20: Matriz de Punteros a Libros
Crea una clase `Libreria` con matriz dinámica de punteros a `Libro`. Implementa:
- `agregarLibro(int fila, int columna, string titulo, string autor, int año)`
- `eliminarLibro(int fila, int columna)`
- `buscarLibro(string titulo)`: retorna `true` si existe
- `librosPorAutor(string autor)`: retorna el número de libros de un autor
- `libroMasAntiguo()`: retorna el libro con año más antiguo

---

## PARTE IV: EJERCICIOS AVANZADOS

### Ejercicio 21: Sistema de Reservas de Hotel
Crea clases `Habitacion` (número, tipo, precio) y `Hotel` con matriz dinámica de punteros a `Habitacion`. Implementa:
- `reservarHabitacion(int fila, int columna, int numero, string tipo, double precio)`
- `liberarHabitacion(int fila, int columna)`
- `habitacionesDisponibles()`: cuenta habitaciones no reservadas (nullptr)
- `ingresosTotales()`: suma precios de todas las habitaciones reservadas
- `habitacionMasCara()`: retorna la habitación con mayor precio

### Ejercicio 22: Sistema de Equipos de Fútbol
Crea clases `Jugador` (nombre, posición, número) y `Equipo` con matriz dinámica de punteros a `Jugador`. Implementa:
- `agregarJugador(int fila, int columna, string nombre, string posicion, int numero)`
- `eliminarJugador(int fila, int columna)`
- `jugadoresPorPosicion(string posicion)`: cuenta jugadores en una posición
- `buscarJugador(int numero)`: busca por número de camiseta
- `totalJugadores()`: cuenta jugadores no nulos

### Ejercicio 23: Sistema de Horario de Clases
Crea clases `Clase` (nombre, profesor, horaInicio, horaFin) y `HorarioSemanal` con matriz dinámica de punteros a `Clase` (7 días x 12 horas). Implementa:
- `agregarClase(int dia, int hora, string nombre, string profesor, int inicio, int fin)`
- `eliminarClase(int dia, int hora)`
- `clasesPorDia(int dia)`: cuenta clases en un día
- `clasesPorProfesor(string profesor)`: cuenta clases de un profesor
- `hayConflicto(int dia, int hora)`: verifica si hay solapamiento de horarios

### Ejercicio 24: Sistema de Editorial
Crea clases `Libro` (título, autor, unidadesVendidas, precioUnitario, año) y `Editorial` con matriz dinámica de punteros a `Libro` (sucursales x años). Implementa:
- `agregarLibro(int sucursal, int año, string titulo, string autor, int unidades, double precio, int añoPublicacion)`
- `gananciasAutor(string autor)`: suma precio * unidades de libros de un autor
- `unidadesVendidasAño(int año)`: suma unidades vendidas en un año
- `libroBestSeller()`: retorna el libro con más unidades vendidas
- `gananciasSucursal(int sucursal)`: suma ganancias de una sucursal

### Ejercicio 25: Sistema de Hacienda
Crea clases `Declaracion` (idContribuyente, monto, año) y `Hacienda` con matriz dinámica de punteros a `Declaracion` (contribuyentes x años). Implementa:
- `agregarDeclaracion(int contribuyente, int año, int id, double monto)`
- `totalContribuyente(int contribuyente)`: suma montos de un contribuyente
- `totalAño(int año)`: suma montos de un año
- `contribuyenteConMayorMonto()`: retorna el índice del contribuyente con mayor monto total
- `promedioAño(int año)`: promedio de montos en un año

### Ejercicio 26: Matriz de Matrices
Crea una clase `MatrizDeMatrices` que contenga una matriz dinámica de punteros a matrices dinámicas de enteros. Implementa:
- Constructor que reciba el tamaño de la matriz principal y el tamaño de cada submatriz
- Destructor que libere toda la memoria correctamente
- `asignarValor(int filaPrincipal, int colPrincipal, int filaSub, int colSub, int valor)`
- `obtenerValor(int filaPrincipal, int colPrincipal, int filaSub, int colSub)`
- `sumarSubmatriz(int filaPrincipal, int colPrincipal)`: suma elementos de una submatriz

### Ejercicio 27: Sistema de Votaciones
Crea clases `Voto` (candidato, fecha) y `Urna` con matriz dinámica de punteros a `Voto` (mesas x candidatos). Implementa:
- `registrarVoto(int mesa, int candidato, string nombreCandidato, string fecha)`
- `votosPorCandidato(int candidato)`: cuenta votos de un candidato
- `votosPorMesa(int mesa)`: cuenta votos de una mesa
- `candidatoGanador()`: retorna el índice del candidato con más votos
- `totalVotos()`: cuenta todos los votos registrados

### Ejercicio 28: Sistema de Almacén
Crea clases `Articulo` (codigo, nombre, categoria, cantidad, precio) y `Almacen` con matriz dinámica de punteros a `Articulo` (estantes x categorías). Implementa:
- `agregarArticulo(int estante, int categoria, string codigo, string nombre, string cat, int cantidad, double precio)`
- `eliminarArticulo(int estante, int categoria)`
- `articulosPorCategoria(int categoria)`: cuenta artículos en una categoría
- `valorEstante(int estante)`: suma precio * cantidad de un estante
- `articuloMasCaro()`: retorna el artículo con mayor precio
- `articulosAgotados()`: cuenta artículos con cantidad = 0

### Ejercicio 29: Sistema de Calificaciones Escolares
Crea clases `Calificacion` (estudiante, materia, nota, trimestre) y `RegistroAcademico` con matriz dinámica de punteros a `Calificacion` (estudiantes x materias). Implementa:
- `agregarCalificacion(int estudiante, int materia, string nombreEst, string nombreMat, double nota, int trimestre)`
- `promedioEstudiante(int estudiante)`: promedio de un estudiante en todas las materias
- `promedioMateria(int materia)`: promedio de una materia de todos los estudiantes
- `mejorEstudiante()`: retorna el índice del estudiante con mejor promedio
- `estudiantesAprobados(double notaMinima)`: cuenta estudiantes con promedio >= notaMinima
- `materiaMasDificil()`: retorna el índice de la materia con menor promedio

### Ejercicio 30: Sistema Completo de Biblioteca Universitaria
Crea clases `Libro` (ISBN, titulo, autor, año, disponible) y `Biblioteca` con matriz dinámica de punteros a `Libro` (estantes x secciones). Implementa:
- `agregarLibro(int estante, int seccion, string ISBN, string titulo, string autor, int año, bool disponible)`
- `prestarLibro(int estante, int seccion)`: marca libro como no disponible
- `devolverLibro(int estante, int seccion)`: marca libro como disponible
- `librosDisponibles()`: cuenta libros disponibles
- `buscarPorISBN(string ISBN)`: retorna `true` si existe el libro
- `librosPorAutor(string autor)`: cuenta libros de un autor
- `librosAntiguos(int añoLimite)`: cuenta libros anteriores a un año
- `valorTotalBiblioteca()`: asume un valor fijo por libro y calcula el total

---

## Notas Finales

- Todos los ejercicios deben incluir un programa `main.cpp` que demuestre el funcionamiento
- Implementa validaciones de índices para evitar accesos fuera de rango
- Asegúrate de liberar correctamente toda la memoria dinámica
- Usa nombres descriptivos para variables y métodos
- Incluye comentarios donde sea necesario para claridad
- Prueba tus implementaciones con diferentes casos de uso

**¡Buena suerte con los ejercicios!**
