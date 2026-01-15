# Clase 1: Listas Enlazadas Básicas en C++

## Índice
1. [Introducción a Listas Enlazadas](#introducción-a-listas-enlazadas)
2. [Conceptos Fundamentales](#conceptos-fundamentales)
3. [Estructura del Nodo](#estructura-del-nodo)
4. [Estructura de la Lista](#estructura-de-la-lista)
5. [Operaciones Básicas](#operaciones-básicas)
6. [Implementación Completa](#implementación-completa)
7. [Ejemplos Prácticos](#ejemplos-prácticos)

---

## Introducción a Listas Enlazadas

Una **lista enlazada** es una estructura de datos dinámica que almacena elementos de forma secuencial, donde cada elemento (nodo) contiene:
- **Datos**: La información que se desea almacenar
- **Puntero**: Referencia al siguiente nodo en la lista

### Ventajas de las Listas Enlazadas

- ✅ **Tamaño dinámico**: Se puede crecer o reducir según sea necesario
- ✅ **Inserción/eliminación eficiente**: No requiere desplazar elementos
- ✅ **Uso eficiente de memoria**: Solo usa la memoria necesaria
- ✅ **Flexibilidad**: Fácil de reorganizar

### Desventajas

- ❌ **Acceso secuencial**: No se puede acceder directamente a un elemento por índice
- ❌ **Memoria extra**: Cada nodo requiere espacio para el puntero
- ❌ **No hay caché**: Los nodos pueden estar dispersos en memoria

---

## Conceptos Fundamentales

### Nodo (Node)

Un **nodo** es la unidad básica de una lista enlazada. Cada nodo contiene:
- **Datos**: El valor o objeto que almacena
- **Siguiente**: Puntero al siguiente nodo (o `NULL` si es el último)

### Lista Enlazada

Una **lista enlazada** es una colección de nodos conectados mediante punteros. Tiene:
- **Primero**: Puntero al primer nodo de la lista
- **Último** (opcional): Puntero al último nodo de la lista
- **Actual** (opcional): Puntero al nodo actual durante recorridos

### Tipos de Listas Enlazadas

1. **Lista Simple**: Cada nodo apunta solo al siguiente
2. **Lista Doble**: Cada nodo apunta al siguiente y al anterior
3. **Lista Circular**: El último nodo apunta al primero

En este curso nos enfocaremos en **listas simples**.

---

## Estructura del Nodo

### Nodo con Tipo Primitivo

```cpp
// nodo.h
#ifndef NODO_H
#define NODO_H

class nodo {
private:
    int num;           // Dato almacenado
    nodo* sig;         // Puntero al siguiente nodo
    
public:
    nodo(int num, nodo* sig);
    ~nodo();
    int getNum() const;
    nodo* getSig() const;
    void setSig(nodo* sig);
};

#endif
```

```cpp
// nodo.cpp
#include "nodo.h"

nodo::nodo(int num, nodo* sig) {
    this->num = num;
    this->sig = sig;
}

nodo::~nodo() {
    // El destructor del nodo NO debe eliminar el siguiente
    // Eso es responsabilidad de la lista
}

int nodo::getNum() const {
    return num;
}

nodo* nodo::getSig() const {
    return sig;
}

void nodo::setSig(nodo* sig) {
    this->sig = sig;
}
```

### Nodo con Objeto

```cpp
// nodo.h
#ifndef NODO_H
#define NODO_H
#include "persona.h"

class nodo {
private:
    Persona* persona;   // Puntero al objeto almacenado
    nodo* sig;          // Puntero al siguiente nodo
    
public:
    nodo(Persona* persona, nodo* sig);
    ~nodo();
    Persona* getPersona() const;
    nodo* getSig() const;
    void setSig(nodo* sig);
    string toStringNodo();
};

#endif
```

```cpp
// nodo.cpp
#include "nodo.h"
#include <sstream>

nodo::nodo(Persona* persona, nodo* sig) {
    this->persona = persona;
    this->sig = sig;
}

nodo::~nodo() {
    // Decidir si eliminar el objeto persona aquí
    // Generalmente NO se elimina aquí, se elimina en la lista
}

Persona* nodo::getPersona() const {
    return persona;
}

nodo* nodo::getSig() const {
    return sig;
}

void nodo::setSig(nodo* sig) {
    this->sig = sig;
}

string nodo::toStringNodo() {
    stringstream s;
    if (persona != nullptr) {
        s << persona->toString() << endl;
    }
    return s.str();
}
```

---

## Estructura de la Lista

### Lista Básica con Puntero Último

```cpp
// lista.h
#ifndef LISTA_H
#define LISTA_H
#include "nodo.h"
#include <string>

class lista {
private:
    nodo* primero;      // Puntero al primer nodo
    nodo* ultimo;       // Puntero al último nodo
    int can;            // Contador de elementos
    
public:
    lista();
    ~lista();
    bool vacia();
    int getCan();
    void agregarInicio(int valor);
    void agregarFinal(int valor);
    bool eliminaInicio();
    bool eliminaFinal();
    string toString();
};

#endif
```

### Lista con Puntero Actual

```cpp
// lista.h
#ifndef LISTA_H
#define LISTA_H
#include "nodo.h"
#include "persona.h"
#include <string>

class lista {
private:
    nodo* primero;      // Puntero al primer nodo
    nodo* actual;      // Puntero al nodo actual (para recorridos)
    
public:
    lista();
    ~lista();
    bool listaVacia();
    void insertarInicio(Persona* p);
    void insertarFinal(Persona* p);
    bool eliminaInicio();
    bool eliminaFinal();
    string toString();
    Persona* obtenerPrimero();
    Persona* obtenerUltimo();
};

#endif
```

---

## Operaciones Básicas

### 1. Constructor

```cpp
lista::lista() {
    primero = NULL;
    ultimo = NULL;
    can = 0;
}
```

O con puntero actual:

```cpp
lista::lista() {
    primero = NULL;
    actual = NULL;
}
```

### 2. Verificar si está Vacía

```cpp
bool lista::vacia() {
    return (primero == NULL);
}
```

### 3. Insertar al Inicio

**Casos a considerar:**
- Lista vacía: El nuevo nodo será primero y último
- Lista con elementos: El nuevo nodo será primero

```cpp
void lista::agregarInicio(int x) {
    nodo* nuevo = new nodo(x, primero);
    
    if (vacia()) {
        ultimo = nuevo;  // Si está vacía, también es el último
    }
    
    primero = nuevo;
    can++;
}
```

### 4. Insertar al Final

**Casos a considerar:**
- Lista vacía: Usar `agregarInicio`
- Lista con elementos: Actualizar el último nodo

```cpp
void lista::agregarFinal(int x) {
    if (vacia()) {
        agregarInicio(x);  // Reutilizar código
    } else {
        ultimo->setSig(new nodo(x, NULL));
        ultimo = ultimo->getSig();
        can++;
    }
}
```

**Versión sin puntero último:**

```cpp
void lista::insertarFinal(Persona* p) {
    actual = primero;
    
    if (primero == NULL) {  // Lista vacía
        primero = new nodo(p, NULL);
    } else {
        // Avanzar hasta el último nodo
        while (actual->getSig() != NULL) {
            actual = actual->getSig();
        }
        // Insertar después del último
        actual->setSig(new nodo(p, NULL));
    }
}
```

### 5. Eliminar del Inicio

**Casos a considerar:**
- Lista vacía: Retornar `false`
- Lista con un elemento: Primero y último quedan en `NULL`
- Lista con varios elementos: Solo actualizar primero

```cpp
bool lista::eliminaInicio() {
    if (primero == NULL) {  // Lista vacía
        return false;
    }
    
    nodo* temp = primero;
    primero = primero->getSig();
    delete temp;
    can--;
    
    if (primero == NULL) {  // Si quedó vacía
        ultimo = NULL;
    }
    
    return true;
}
```

### 6. Eliminar del Final

**Casos a considerar:**
- Lista vacía: Retornar `false`
- Lista con un elemento: Eliminar y dejar lista vacía
- Lista con varios elementos: Encontrar el penúltimo y eliminar el último

```cpp
bool lista::eliminaFinal() {
    if (primero == NULL) {  // Lista vacía
        return false;
    }
    
    if (primero->getSig() == NULL) {  // Solo un elemento
        delete primero;
        primero = NULL;
        ultimo = NULL;
        can--;
        return true;
    }
    
    // Varios elementos: encontrar penúltimo
    nodo* actual = primero;
    while (actual->getSig()->getSig() != NULL) {
        actual = actual->getSig();
    }
    
    delete actual->getSig();
    actual->setSig(NULL);
    ultimo = actual;
    can--;
    return true;
}
```

### 7. Recorrer la Lista (toString)

```cpp
string lista::toString() {
    stringstream s;
    nodo* actual = primero;
    
    while (actual != NULL) {
        s << actual->getNum() << endl;
        actual = actual->getSig();
    }
    
    return s.str();
}
```

### 8. Destructor

```cpp
lista::~lista() {
    while (!vacia()) {
        eliminaInicio();  // Eliminar siempre el primero es más eficiente
    }
}
```

O alternativamente:

```cpp
lista::~lista() {
    while (primero != NULL) {
        nodo* temp = primero;
        primero = primero->getSig();
        delete temp;
    }
}
```

---

## Implementación Completa

### Ejemplo: Lista de Enteros

```cpp
// lista.h
#ifndef LISTA_H
#define LISTA_H
#include "nodo.h"
#include <string>

class lista {
private:
    nodo* primero;
    nodo* ultimo;
    int can;
    
public:
    lista();
    ~lista();
    bool vacia();
    int getCan();
    void agregarInicio(int valor);
    void agregarFinal(int valor);
    bool eliminaInicio();
    bool eliminaFinal();
    string toString();
    int obtenerPrimero();
    int obtenerUltimo();
    bool buscar(int valor);
    int contarApariciones(int valor);
};

#endif
```

```cpp
// lista.cpp
#include "lista.h"
#include <sstream>

lista::lista() {
    primero = NULL;
    ultimo = NULL;
    can = 0;
}

lista::~lista() {
    while (!vacia()) {
        eliminaInicio();
    }
}

bool lista::vacia() {
    return (primero == NULL);
}

int lista::getCan() {
    return can;
}

void lista::agregarInicio(int valor) {
    nodo* nuevo = new nodo(valor, primero);
    
    if (vacia()) {
        ultimo = nuevo;
    }
    
    primero = nuevo;
    can++;
}

void lista::agregarFinal(int valor) {
    if (vacia()) {
        agregarInicio(valor);
    } else {
        ultimo->setSig(new nodo(valor, NULL));
        ultimo = ultimo->getSig();
        can++;
    }
}

bool lista::eliminaInicio() {
    if (vacia()) {
        return false;
    }
    
    nodo* temp = primero;
    primero = primero->getSig();
    delete temp;
    can--;
    
    if (primero == NULL) {
        ultimo = NULL;
    }
    
    return true;
}

bool lista::eliminaFinal() {
    if (vacia()) {
        return false;
    }
    
    if (primero->getSig() == NULL) {
        delete primero;
        primero = NULL;
        ultimo = NULL;
        can--;
        return true;
    }
    
    nodo* actual = primero;
    while (actual->getSig()->getSig() != NULL) {
        actual = actual->getSig();
    }
    
    delete actual->getSig();
    actual->setSig(NULL);
    ultimo = actual;
    can--;
    return true;
}

string lista::toString() {
    stringstream s;
    nodo* actual = primero;
    
    while (actual != NULL) {
        s << actual->getNum() << " ";
        actual = actual->getSig();
    }
    
    return s.str();
}

int lista::obtenerPrimero() {
    if (!vacia()) {
        return primero->getNum();
    }
    return -1; // Valor por defecto
}

int lista::obtenerUltimo() {
    if (!vacia()) {
        return ultimo->getNum();
    }
    return -1;
}

bool lista::buscar(int valor) {
    nodo* actual = primero;
    
    while (actual != NULL) {
        if (actual->getNum() == valor) {
            return true;
        }
        actual = actual->getSig();
    }
    
    return false;
}

int lista::contarApariciones(int valor) {
    int contador = 0;
    nodo* actual = primero;
    
    while (actual != NULL) {
        if (actual->getNum() == valor) {
            contador++;
        }
        actual = actual->getSig();
    }
    
    return contador;
}
```

---

## Ejemplos Prácticos

### Ejemplo 1: Uso Básico

```cpp
// main.cpp
#include "lista.h"
#include <iostream>

int main() {
    lista miLista;
    
    // Agregar elementos
    miLista.agregarInicio(10);
    miLista.agregarInicio(20);
    miLista.agregarFinal(30);
    miLista.agregarFinal(40);
    
    // Mostrar lista
    cout << "Lista: " << miLista.toString() << endl;
    cout << "Cantidad: " << miLista.getCan() << endl;
    
    // Buscar elemento
    if (miLista.buscar(30)) {
        cout << "30 encontrado" << endl;
    }
    
    // Eliminar elementos
    miLista.eliminaInicio();
    miLista.eliminaFinal();
    
    cout << "Después de eliminar: " << miLista.toString() << endl;
    
    return 0;
}
```

### Ejemplo 2: Lista de Personas

```cpp
// Persona.h
class Persona {
private:
    string nombre;
    int edad;
    
public:
    Persona(string nombre, int edad);
    string getNombre();
    int getEdad();
    string toString();
};

// nodo.h (para Persona)
class nodo {
private:
    Persona* persona;
    nodo* sig;
    
public:
    nodo(Persona* persona, nodo* sig);
    Persona* getPersona();
    nodo* getSig();
    void setSig(nodo* sig);
};

// lista.h (para Persona)
class lista {
private:
    nodo* primero;
    
public:
    lista();
    ~lista();
    void insertarFinal(Persona* p);
    string toString();
    Persona* buscarPorNombre(string nombre);
    int contarPersonas();
};
```

---

## Buenas Prácticas

### 1. Siempre Verificar NULL

```cpp
// ✅ CORRECTO
if (primero != NULL) {
    // Usar primero
}

// ❌ INCORRECTO
primero->getNum();  // Puede causar crash si primero es NULL
```

### 2. Manejar Casos Especiales

Siempre considerar:
- Lista vacía
- Lista con un solo elemento
- Lista con varios elementos

### 3. Liberar Memoria Correctamente

```cpp
// En el destructor de la lista
lista::~lista() {
    while (primero != NULL) {
        nodo* temp = primero;
        primero = primero->getSig();
        delete temp;  // Liberar cada nodo
    }
}
```

### 4. No Eliminar el Siguiente en el Destructor del Nodo

```cpp
// ❌ INCORRECTO en nodo.cpp
nodo::~nodo() {
    delete sig;  // NO hacer esto
}

// ✅ CORRECTO
nodo::~nodo() {
    // No hacer nada, la lista se encarga
}
```

---

## Errores Comunes

### 1. Olvidar Actualizar Punteros

```cpp
// ❌ INCORRECTO
void agregarInicio(int x) {
    primero = new nodo(x, primero);
    // Olvidó actualizar ultimo si estaba vacía
}

// ✅ CORRECTO
void agregarInicio(int x) {
    nodo* nuevo = new nodo(x, primero);
    if (vacia()) {
        ultimo = nuevo;
    }
    primero = nuevo;
    can++;
}
```

### 2. Acceder a Nodos Eliminados

```cpp
// ❌ INCORRECTO
delete primero;
cout << primero->getNum();  // CRASH: primero ya fue eliminado

// ✅ CORRECTO
nodo* temp = primero;
primero = primero->getSig();
delete temp;  // Eliminar después de actualizar
```

### 3. No Verificar Lista Vacía

```cpp
// ❌ INCORRECTO
int obtenerPrimero() {
    return primero->getNum();  // CRASH si está vacía
}

// ✅ CORRECTO
int obtenerPrimero() {
    if (!vacia()) {
        return primero->getNum();
    }
    return -1;  // Valor por defecto
}
```

---

## Resumen

- **Nodo**: Unidad básica con datos y puntero al siguiente
- **Lista**: Colección de nodos con puntero al primero (y opcionalmente al último)
- **Operaciones básicas**: Insertar inicio/final, eliminar inicio/final, recorrer
- **Siempre verificar**: Lista vacía, NULL, casos especiales
- **Liberar memoria**: En el destructor de la lista, no del nodo

**Próxima clase**: Operaciones avanzadas (búsqueda, eliminación específica, inserción ordenada, etc.)
