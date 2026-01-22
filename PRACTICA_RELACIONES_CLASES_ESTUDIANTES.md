# Práctica: Relaciones de Diseño entre Clases en C++

## Objetivo
Comprender e implementar los diferentes tipos de relaciones entre clases: Dependencia, Asociación, Agregación, Composición, Cardinalidad y Navegabilidad.

---

## Conceptos Teóricos

### 1. Dependencia (Dependency)
- **Definición**: Una clase usa temporalmente otra clase, pero no mantiene una referencia permanente.
- **Características**: 
  - Relación más débil
  - La clase dependiente no posee la clase de la que depende
  - Se usa como parámetro de método o variable local
- **Símbolo UML**: Flecha punteada con dirección `---->`

### 2. Asociación (Association)
- **Definición**: Relación estructural donde dos clases están relacionadas pero pueden existir independientemente.
- **Características**:
  - Ambas clases pueden existir sin la otra
  - Puede ser bidireccional o unidireccional
  - Se implementa con punteros o referencias
- **Símbolo UML**: Línea sólida `----`

### 3. Agregación (Aggregation)
- **Definición**: Relación "tiene-un" donde una clase contiene objetos de otra clase, pero estos pueden existir independientemente.
- **Características**:
  - Relación "todo-parte" débil
  - La parte puede existir sin el todo
  - Se implementa con punteros (no se destruye la parte al destruir el todo)
- **Símbolo UML**: Línea sólida con diamante vacío `----<>`

### 4. Composición (Composition)
- **Definición**: Relación "tiene-un" fuerte donde una clase contiene objetos de otra clase que no pueden existir independientemente.
- **Características**:
  - Relación "todo-parte" fuerte
  - La parte no puede existir sin el todo
  - Se implementa con objetos directos (se destruye la parte al destruir el todo)
- **Símbolo UML**: Línea sólida con diamante relleno `----◆`

### 5. Cardinalidad
- **Definición**: Indica cuántos objetos de una clase se relacionan con objetos de otra clase.
- **Tipos**:
  - `1`: Uno
  - `*` o `0..*`: Cero o muchos
  - `1..*`: Uno o muchos
  - `0..1`: Cero o uno
  - `n`: Número específico

### 6. Navegabilidad
- **Definición**: Indica si una clase puede acceder a otra clase en la relación.
- **Tipos**:
  - **Unidireccional**: Solo una clase conoce a la otra
  - **Bidireccional**: Ambas clases se conocen mutuamente

---

## Ejercicios

### Ejercicio 1
**Enunciado**: Crea una clase `Estudiante` y una clase `Profesor`. Un `Profesor` puede calificar a múltiples `Estudiante`, pero un `Estudiante` solo puede ser calificado por un `Profesor`. Identifica el tipo de relación y la cardinalidad. Implementa el código en C++.

**Tipo de relación**: _______________
**Cardinalidad**: _______________
**Navegabilidad**: _______________

---

### Ejercicio 2
**Enunciado**: Implementa una clase `Biblioteca` que contiene múltiples `Libro`. Los libros pueden existir fuera de la biblioteca. Identifica el tipo de relación y la cardinalidad.

**Tipo de relación**: _______________
**Cardinalidad**: _______________

---

### Ejercicio 3
**Enunciado**: Crea una clase `Casa` que tiene múltiples `Habitacion`. Las habitaciones no pueden existir sin la casa. Identifica el tipo de relación y la cardinalidad.

**Tipo de relación**: _______________
**Cardinalidad**: _______________

---

### Ejercicio 4
**Enunciado**: Implementa una clase `Calculadora` que usa una clase `Operacion` solo como parámetro en un método. La `Calculadora` no mantiene referencia a `Operacion`. Identifica el tipo de relación.

**Tipo de relación**: _______________

---

### Ejercicio 5
**Enunciado**: Crea una clase `Universidad` que tiene múltiples `Departamento`. Los departamentos pueden existir independientemente de la universidad. Implementa con cardinalidad 1..*.

**Tipo de relación**: _______________
**Cardinalidad**: _______________

---

### Ejercicio 6
**Enunciado**: Implementa una clase `Automovil` que tiene exactamente 4 `Rueda`. Las ruedas no pueden existir sin el automóvil. Identifica el tipo de relación y la cardinalidad.

**Tipo de relación**: _______________
**Cardinalidad**: _______________

---

### Ejercicio 7
**Enunciado**: Crea una clase `EditorTexto` que usa una clase `Impresora` solo para imprimir documentos. El `EditorTexto` no mantiene referencia permanente a `Impresora`. Identifica el tipo de relación.

**Tipo de relación**: _______________

---

### Ejercicio 8
**Enunciado**: Implementa una clase `Empresa` que tiene múltiples `Empleado`. Los empleados pueden trabajar en diferentes empresas a lo largo del tiempo. Identifica el tipo de relación y la cardinalidad.

**Tipo de relación**: _______________
**Cardinalidad**: _______________

---

### Ejercicio 9
**Enunciado**: Crea una clase `Computadora` que tiene un `Procesador`, una `MemoriaRAM` y múltiples `DiscoDuro`. Estos componentes no pueden existir sin la computadora. Identifica el tipo de relación.

**Tipo de relación**: _______________

---

### Ejercicio 10
**Enunciado**: Implementa una clase `Restaurante` que tiene múltiples `Mesa`. Las mesas pueden existir fuera del restaurante. Implementa con cardinalidad 0..*.

**Tipo de relación**: _______________
**Cardinalidad**: _______________

---

### Ejercicio 11
**Enunciado**: Crea una clase `Persona` y una clase `Direccion`. Una persona puede tener una dirección, pero la dirección puede existir sin la persona. Identifica el tipo de relación y la cardinalidad.

**Tipo de relación**: _______________
**Cardinalidad**: _______________

---

### Ejercicio 12
**Enunciado**: Implementa una clase `Telefono` que tiene una `Pantalla`. La pantalla no puede existir sin el teléfono. Identifica el tipo de relación.

**Tipo de relación**: _______________

---

### Ejercicio 13
**Enunciado**: Crea una clase `Banco` que tiene múltiples `CuentaBancaria`. Las cuentas bancarias no pueden existir sin el banco. Identifica el tipo de relación y la cardinalidad.

**Tipo de relación**: _______________
**Cardinalidad**: _______________

---

### Ejercicio 14
**Enunciado**: Implementa una clase `Reportero` que usa una clase `Camara` solo para tomar fotografías. El reportero no mantiene la cámara permanentemente. Identifica el tipo de relación.

**Tipo de relación**: _______________

---

### Ejercicio 15
**Enunciado**: Crea una clase `Hospital` que tiene múltiples `Doctor`. Los doctores pueden trabajar en diferentes hospitales. Identifica el tipo de relación y la cardinalidad.

**Tipo de relación**: _______________
**Cardinalidad**: _______________

---

### Ejercicio 16
**Enunciado**: Implementa una clase `Avion` que tiene múltiples `Motor`. Los motores no pueden existir sin el avión. Identifica el tipo de relación y la cardinalidad.

**Tipo de relación**: _______________
**Cardinalidad**: _______________

---

### Ejercicio 17
**Enunciado**: Crea una clase `Estudiante` y una clase `Curso`. Un estudiante puede estar inscrito en múltiples cursos, y un curso puede tener múltiples estudiantes. Identifica el tipo de relación y la cardinalidad.

**Tipo de relación**: _______________
**Cardinalidad**: _______________

---

### Ejercicio 18
**Enunciado**: Implementa una clase `Documento` que tiene múltiples `Pagina`. Las páginas no pueden existir sin el documento. Identifica el tipo de relación y la cardinalidad.

**Tipo de relación**: _______________
**Cardinalidad**: _______________

---

### Ejercicio 19
**Enunciado**: Crea una clase `Tienda` que tiene múltiples `Producto`. Los productos pueden existir fuera de la tienda. Implementa con cardinalidad 1..*.

**Tipo de relación**: _______________
**Cardinalidad**: _______________

---

### Ejercicio 20
**Enunciado**: Implementa una clase `Cocinero` que usa una clase `Receta` solo para cocinar. El cocinero no mantiene referencia permanente a la receta. Identifica el tipo de relación.

**Tipo de relación**: _______________

---

### Ejercicio 21
**Enunciado**: Crea una clase `Escuela` que tiene múltiples `Aula`. Las aulas no pueden existir sin la escuela. Identifica el tipo de relación y la cardinalidad.

**Tipo de relación**: _______________
**Cardinalidad**: _______________

---

### Ejercicio 22
**Enunciado**: Implementa una clase `Cliente` y una clase `Pedido`. Un cliente puede hacer múltiples pedidos, pero un pedido pertenece a un solo cliente. Identifica el tipo de relación y la cardinalidad.

**Tipo de relación**: _______________
**Cardinalidad**: _______________

---

### Ejercicio 23
**Enunciado**: Crea una clase `Celular` que tiene una `Bateria`. La batería no puede existir sin el celular. Identifica el tipo de relación.

**Tipo de relación**: _______________

---

### Ejercicio 24
**Enunciado**: Implementa una clase `Bibliotecario` que usa una clase `Catalogo` solo para buscar libros. El bibliotecario no mantiene referencia permanente al catálogo. Identifica el tipo de relación.

**Tipo de relación**: _______________

---

### Ejercicio 25
**Enunciado**: Crea una clase `Ciudad` que tiene múltiples `Edificio`. Los edificios pueden existir independientemente de la ciudad. Identifica el tipo de relación y la cardinalidad.

**Tipo de relación**: _______________
**Cardinalidad**: _______________

---

### Ejercicio 26
**Enunciado**: Implementa una clase `Bicicleta` que tiene exactamente 2 `Rueda`. Las ruedas no pueden existir sin la bicicleta. Identifica el tipo de relación y la cardinalidad.

**Tipo de relación**: _______________
**Cardinalidad**: _______________

---

### Ejercicio 27
**Enunciado**: Crea una clase `Museo` que tiene múltiples `ObraArte`. Las obras de arte pueden existir fuera del museo. Identifica el tipo de relación y la cardinalidad.

**Tipo de relación**: _______________
**Cardinalidad**: _______________

---

### Ejercicio 28
**Enunciado**: Implementa una clase `Programador` que usa una clase `IDE` solo para escribir código. El programador no mantiene referencia permanente al IDE. Identifica el tipo de relación.

**Tipo de relación**: _______________

---

### Ejercicio 29
**Enunciado**: Crea una clase `Hotel` que tiene múltiples `Habitacion`. Las habitaciones no pueden existir sin el hotel. Identifica el tipo de relación y la cardinalidad.

**Tipo de relación**: _______________
**Cardinalidad**: _______________

---

### Ejercicio 30
**Enunciado**: Implementa una clase `Orquesta` que tiene múltiples `Musico`. Los músicos pueden tocar en diferentes orquestas. Identifica el tipo de relación y la cardinalidad. Implementa con navegabilidad bidireccional.

**Tipo de relación**: _______________
**Cardinalidad**: _______________
**Navegabilidad**: _______________

---

## Instrucciones para la Entrega

1. Para cada ejercicio, identifica correctamente el tipo de relación.
2. Especifica la cardinalidad cuando aplique.
3. Indica la navegabilidad cuando sea relevante.
4. Implementa el código en C++ con:
   - Clases bien definidas
   - Constructores y destructores apropiados
   - Métodos que demuestren la relación
   - Un programa `main()` que muestre el funcionamiento
5. Incluye comentarios explicando por qué elegiste ese tipo de relación.

---

## Criterios de Evaluación

- **Identificación correcta de relaciones** (40%)
- **Implementación correcta en C++** (40%)
- **Uso adecuado de cardinalidad y navegabilidad** (10%)
- **Comentarios y documentación** (10%)

---

**Nota**: Recuerda que la diferencia clave entre Agregación y Composición es la dependencia del ciclo de vida. En Composición, cuando se destruye el objeto contenedor, también se destruyen los objetos contenidos. En Agregación, los objetos contenidos pueden seguir existiendo.
