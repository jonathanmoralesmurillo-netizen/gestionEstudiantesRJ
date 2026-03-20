# 🍕 Laboratorio: Patrón Decorator – Sistema de Pizzas

## 🎯 Objetivo
Implementar el **Patrón de Diseño Decorator** para construir pizzas dinámicamente agregando ingredientes sin modificar las clases existentes.

---

## 🧩 Descripción del problema
Se desea modelar un sistema donde se puedan crear pizzas base y agregar ingredientes como queso, pepperoni, hongos, etc., de forma flexible.

Cada ingrediente debe:
- Añadir descripción
- Incrementar el costo

---

## 🧱 Requerimientos

### 1. Componente base
Crear una clase abstracta `Pizza` que contenga:

- Método `descripcion()`
- Método `costo()`

---

### 2. Componente concreto
Crear una clase `PizzaBasica` que:

- Extienda de `Pizza`
- Retorne una descripción base
- Defina un costo inicial

---

### 3. Decorador base
Crear una clase abstracta `DecoradorPizza` que:

- Extienda de `Pizza`
- Contenga una referencia a un objeto `Pizza`
- Utilice composición

---

### 4. Decoradores concretos (ingredientes)
Implementar al menos **3 ingredientes** como decoradores:

Ejemplos:
- Queso
- Pepperoni
- Hongos

Cada uno debe:
- Modificar la descripción
- Incrementar el costo

---

### 5. Uso en el programa principal
En el `main`, crear diferentes combinaciones de pizzas utilizando decoradores.

Ejemplo esperado:

```cpp
Pizza* pizza = new PizzaBasica();
pizza = new Queso(new PizzaBasica());
pizza = new Pepperoni(new PizzaBasica());
