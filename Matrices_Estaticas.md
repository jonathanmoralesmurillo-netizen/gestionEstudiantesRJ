# Matrices Estáticas (Automáticas)

## 📚 Explicación Teórica

### ¿Qué son las Matrices Estáticas?

Las **matrices estáticas** (también llamadas **automáticas**) son estructuras de datos bidimensionales cuyo tamaño se define en tiempo de compilación y no puede cambiar durante la ejecución del programa. A diferencia de las matrices dinámicas, el espacio de memoria se reserva automáticamente en la pila (stack) cuando se declara la variable.

### Características Principales

1. **Tamaño fijo**: El tamaño debe ser conocido en tiempo de compilación
2. **Memoria en la pila**: Se almacenan en la memoria estática/automática
3. **Acceso rápido**: El acceso a elementos es muy eficiente (O(1))
4. **Sin gestión manual**: No necesitas liberar memoria manualmente
5. **Limitación de tamaño**: Están limitadas por el tamaño de la pila

### Ventajas

- ✅ Acceso rápido a elementos
- ✅ No requiere gestión manual de memoria
- ✅ Sintaxis simple y directa
- ✅ Mejor rendimiento para matrices pequeñas/medianas

### Desventajas

- ❌ Tamaño fijo (no puede cambiar en tiempo de ejecución)
- ❌ Limitadas por el tamaño de la pila
- ❌ Pueden desperdiciar memoria si no se usan todas las celdas

---

## 💻 Ejemplos Prácticos en C++

### 1. Declaración e Inicialización

```cpp
#include <iostream>
using namespace std;

int main() {
    // Declaración de una matriz 3x3
    int matriz[3][3];
    
    // Inicialización al declarar
    int matriz1[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    
    // Inicialización parcial (el resto se llena con ceros)
    int matriz2[3][3] = {
        {1, 2},
        {4}
    };
    
    // Inicialización con un solo valor (todos los elementos son 0)
    int matriz3[3][3] = {0};
    
    // Usando constantes para definir el tamaño
    const int FILAS = 3;
    const int COLUMNAS = 3;
    int matriz4[FILAS][COLUMNAS] = {{0}};
    
    return 0;
}
```

---

### 2. Acceso a Elementos

```cpp
#include <iostream>
using namespace std;

int main() {
    int matriz[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    
    // Acceder a un elemento específico (fila 1, columna 2)
    int valor = matriz[1][2]; // Recuerda: índices empiezan en 0
    cout << "Valor en [1][2]: " << valor << endl;
    
    // Modificar un elemento
    matriz[0][0] = 10;
    cout << "Nuevo valor en [0][0]: " << matriz[0][0] << endl;
    
    return 0;
}
```

---

### 3. Recorrer una Matriz

#### Recorrido por Filas

```cpp
#include <iostream>
using namespace std;

int main() {
    const int FILAS = 3;
    const int COLUMNAS = 3;
    
    int matriz[FILAS][COLUMNAS] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    
    // Recorrer por filas
    cout << "Recorrido por filas:" << endl;
    for (int i = 0; i < FILAS; i++) {
        for (int j = 0; j < COLUMNAS; j++) {
            cout << matriz[i][j] << " ";
        }
        cout << endl;
    }
    
    return 0;
}
```

#### Recorrido por Columnas

```cpp
// Recorrer por columnas
cout << "\nRecorrido por columnas:" << endl;
for (int j = 0; j < COLUMNAS; j++) {
    for (int i = 0; i < FILAS; i++) {
        cout << matriz[i][j] << " ";
    }
    cout << endl;
}
```

#### Recorrido con Range-based for (C++11)

```cpp
// Usando range-based for loop (C++11)
cout << "\nRecorrido con range-based for:" << endl;
for (const auto& fila : matriz) {
    for (const auto& elemento : fila) {
        cout << elemento << " ";
    }
    cout << endl;
}
```

---

### 4. Operaciones Comunes

#### Suma de Matrices

```cpp
#include <iostream>
using namespace std;

const int TAM = 3;

void sumarMatrices(const int a[TAM][TAM], const int b[TAM][TAM], int resultado[TAM][TAM]) {
    for (int i = 0; i < TAM; i++) {
        for (int j = 0; j < TAM; j++) {
            resultado[i][j] = a[i][j] + b[i][j];
        }
    }
}

void imprimirMatriz(const int matriz[TAM][TAM]) {
    for (int i = 0; i < TAM; i++) {
        for (int j = 0; j < TAM; j++) {
            cout << matriz[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    int matrizA[TAM][TAM] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int matrizB[TAM][TAM] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};
    int resultado[TAM][TAM];
    
    sumarMatrices(matrizA, matrizB, resultado);
    
    cout << "Matriz A:" << endl;
    imprimirMatriz(matrizA);
    
    cout << "\nMatriz B:" << endl;
    imprimirMatriz(matrizB);
    
    cout << "\nResultado (A + B):" << endl;
    imprimirMatriz(resultado);
    
    return 0;
}
```

#### Multiplicación de Matrices

```cpp
void multiplicarMatrices(const int a[TAM][TAM], const int b[TAM][TAM], int resultado[TAM][TAM]) {
    for (int i = 0; i < TAM; i++) {
        for (int j = 0; j < TAM; j++) {
            resultado[i][j] = 0;
            for (int k = 0; k < TAM; k++) {
                resultado[i][j] += a[i][k] * b[k][j];
            }
        }
    }
}
```

---

### 5. Buscar un Elemento

```cpp
#include <iostream>
using namespace std;

const int TAM = 3;

bool buscarElemento(const int matriz[TAM][TAM], int valor) {
    for (int i = 0; i < TAM; i++) {
        for (int j = 0; j < TAM; j++) {
            if (matriz[i][j] == valor) {
                return true;
            }
        }
    }
    return false;
}

// Versión que retorna la posición usando referencias
bool buscarPosicion(const int matriz[TAM][TAM], int valor, int& fila, int& columna) {
    for (int i = 0; i < TAM; i++) {
        for (int j = 0; j < TAM; j++) {
            if (matriz[i][j] == valor) {
                fila = i;
                columna = j;
                return true;
            }
        }
    }
    fila = -1;
    columna = -1;
    return false;
}

int main() {
    int matriz[TAM][TAM] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int valorBuscado = 5;
    
    if (buscarElemento(matriz, valorBuscado)) {
        cout << "El valor " << valorBuscado << " se encuentra en la matriz" << endl;
    }
    
    int fila, columna;
    if (buscarPosicion(matriz, valorBuscado, fila, columna)) {
        cout << "Posición: [" << fila << "][" << columna << "]" << endl;
    }
    
    return 0;
}
```

---

### 6. Matriz Transpuesta

```cpp
#include <iostream>
using namespace std;

const int TAM = 3;

void transponerMatriz(const int matriz[TAM][TAM], int transpuesta[TAM][TAM]) {
    for (int i = 0; i < TAM; i++) {
        for (int j = 0; j < TAM; j++) {
            transpuesta[j][i] = matriz[i][j];
        }
    }
}

void imprimirMatriz(const int matriz[TAM][TAM]) {
    for (int i = 0; i < TAM; i++) {
        for (int j = 0; j < TAM; j++) {
            cout << matriz[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    int matriz[TAM][TAM] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int transpuesta[TAM][TAM];
    
    cout << "Matriz original:" << endl;
    imprimirMatriz(matriz);
    
    transponerMatriz(matriz, transpuesta);
    
    cout << "\nMatriz transpuesta:" << endl;
    imprimirMatriz(transpuesta);
    
    return 0;
}
```

---

### 7. Suma de Diagonal Principal

```cpp
#include <iostream>
using namespace std;

const int TAM = 3;

int sumaDiagonal(const int matriz[TAM][TAM]) {
    int suma = 0;
    for (int i = 0; i < TAM; i++) {
        suma += matriz[i][i];
    }
    return suma;
}

int sumaDiagonalSecundaria(const int matriz[TAM][TAM]) {
    int suma = 0;
    for (int i = 0; i < TAM; i++) {
        suma += matriz[i][TAM - 1 - i];
    }
    return suma;
}

int main() {
    int matriz[TAM][TAM] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    
    cout << "Suma diagonal principal: " << sumaDiagonal(matriz) << endl;
    cout << "Suma diagonal secundaria: " << sumaDiagonalSecundaria(matriz) << endl;
    
    return 0;
}
```

---

## 🎯 Ejercicios Prácticos

### Ejercicio 1: Llenar una Matriz con Valores del Usuario

**Objetivo**: Crear un programa que lea valores del usuario y los almacene en una matriz estática.

```cpp
#include <iostream>
using namespace std;

const int FILAS = 3;
const int COLUMNAS = 3;

int main() {
    int matriz[FILAS][COLUMNAS];
    
    cout << "Ingrese los valores de la matriz " << FILAS << "x" << COLUMNAS << ":" << endl;
    for (int i = 0; i < FILAS; i++) {
        for (int j = 0; j < COLUMNAS; j++) {
            cout << "Matriz[" << i << "][" << j << "]: ";
            cin >> matriz[i][j];
        }
    }
    
    cout << "\nMatriz ingresada:" << endl;
    for (int i = 0; i < FILAS; i++) {
        for (int j = 0; j < COLUMNAS; j++) {
            cout << matriz[i][j] << " ";
        }
        cout << endl;
    }
    
    return 0;
}
```

---

### Ejercicio 2: Encontrar el Elemento Máximo y Mínimo

```cpp
#include <iostream>
#include <climits>
using namespace std;

const int TAM = 3;

void encontrarMaxMin(const int matriz[TAM][TAM], int& max, int& min, 
                     int& fila_max, int& col_max, 
                     int& fila_min, int& col_min) {
    max = INT_MIN;
    min = INT_MAX;
    
    for (int i = 0; i < TAM; i++) {
        for (int j = 0; j < TAM; j++) {
            if (matriz[i][j] > max) {
                max = matriz[i][j];
                fila_max = i;
                col_max = j;
            }
            if (matriz[i][j] < min) {
                min = matriz[i][j];
                fila_min = i;
                col_min = j;
            }
        }
    }
}

int main() {
    int matriz[TAM][TAM] = {{5, 2, 9}, {1, 8, 3}, {7, 4, 6}};
    int max, min, fila_max, col_max, fila_min, col_min;
    
    encontrarMaxMin(matriz, max, min, fila_max, col_max, fila_min, col_min);
    
    cout << "Máximo: " << max << " en posición [" << fila_max << "][" << col_max << "]" << endl;
    cout << "Mínimo: " << min << " en posición [" << fila_min << "][" << col_min << "]" << endl;
    
    return 0;
}
```

---

### Ejercicio 3: Verificar si una Matriz es Simétrica

```cpp
#include <iostream>
using namespace std;

const int TAM = 3;

bool esSimetrica(const int matriz[TAM][TAM]) {
    for (int i = 0; i < TAM; i++) {
        for (int j = 0; j < TAM; j++) {
            if (matriz[i][j] != matriz[j][i]) {
                return false;
            }
        }
    }
    return true;
}

int main() {
    int matriz[TAM][TAM] = {{1, 2, 3}, {2, 4, 5}, {3, 5, 6}};
    
    if (esSimetrica(matriz)) {
        cout << "La matriz es simétrica" << endl;
    } else {
        cout << "La matriz NO es simétrica" << endl;
    }
    
    return 0;
}
```

---

### Ejercicio 4: Suma de Filas y Columnas

```cpp
#include <iostream>
using namespace std;

const int TAM = 3;

void sumarFilasColumnas(const int matriz[TAM][TAM]) {
    int suma_fila, suma_col;
    
    cout << "Suma de filas:" << endl;
    for (int i = 0; i < TAM; i++) {
        suma_fila = 0;
        for (int j = 0; j < TAM; j++) {
            suma_fila += matriz[i][j];
        }
        cout << "Fila " << i << ": " << suma_fila << endl;
    }
    
    cout << "\nSuma de columnas:" << endl;
    for (int j = 0; j < TAM; j++) {
        suma_col = 0;
        for (int i = 0; i < TAM; i++) {
            suma_col += matriz[i][j];
        }
        cout << "Columna " << j << ": " << suma_col << endl;
    }
}

int main() {
    int matriz[TAM][TAM] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    sumarFilasColumnas(matriz);
    return 0;
}
```

---

### Ejercicio 5: Rotar una Matriz 90 Grados

```cpp
#include <iostream>
using namespace std;

const int TAM = 3;

void rotar90Grados(const int matriz[TAM][TAM], int rotada[TAM][TAM]) {
    for (int i = 0; i < TAM; i++) {
        for (int j = 0; j < TAM; j++) {
            rotada[j][TAM - 1 - i] = matriz[i][j];
        }
    }
}

void imprimirMatriz(const int matriz[TAM][TAM]) {
    for (int i = 0; i < TAM; i++) {
        for (int j = 0; j < TAM; j++) {
            cout << matriz[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    int matriz[TAM][TAM] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int rotada[TAM][TAM];
    
    cout << "Matriz original:" << endl;
    imprimirMatriz(matriz);
    
    rotar90Grados(matriz, rotada);
    
    cout << "\nMatriz rotada 90 grados (sentido horario):" << endl;
    imprimirMatriz(rotada);
    
    return 0;
}
```

---

## 📝 Resumen de Conceptos Clave

1. **Declaración**: `tipo nombre[filas][columnas];`
2. **Inicialización**: Puede hacerse al declarar o después
3. **Acceso**: `matriz[fila][columna]` (índices empiezan en 0)
4. **Recorrido**: Usar bucles anidados (for/while)
5. **Tamaño**: Debe ser conocido en tiempo de compilación
6. **Memoria**: Se almacena en la pila (stack)

---

## 🔍 Diferencias: Estática vs Dinámica en C++

| Característica | Matriz Estática | Matriz Dinámica |
|---------------|-----------------|-----------------|
| Tamaño | Fijo en compilación | Variable en ejecución |
| Memoria | Pila (stack) | Heap |
| Gestión | Automática | Manual (`new`/`delete` o `malloc`/`free`) |
| Rendimiento | Más rápido | Ligeramente más lento |
| Flexibilidad | Limitada | Alta |
| Ejemplo | `int matriz[3][3];` | `int** matriz = new int*[3];` |

---

## 💡 Consejos Prácticos

1. **Usa matrices estáticas cuando**:
   - El tamaño es conocido y fijo
   - Necesitas máximo rendimiento
   - El tamaño es pequeño/medio

2. **Evita matrices estáticas cuando**:
   - El tamaño depende de entrada del usuario
   - Necesitas cambiar el tamaño en tiempo de ejecución
   - El tamaño es muy grande (riesgo de desbordamiento de pila)

3. **Buenas prácticas en C++**:
   - Usa constantes para definir tamaños: `const int FILAS = 3;`
   - Usa `const` cuando pases matrices a funciones que no las modifican
   - Usa referencias (`&`) en lugar de punteros cuando sea posible
   - Valida índices antes de acceder
   - Documenta el tamaño de la matriz en comentarios
   - Considera usar `std::array` (C++11) para mejor seguridad de tipos

---

## 📚 Recursos Adicionales

- **Complejidad temporal**: Acceso O(1), Recorrido O(n×m)
- **Complejidad espacial**: O(n×m) donde n y m son filas y columnas
- **Aplicaciones**: Gráficos, procesamiento de imágenes, juegos, simulaciones

---

## 🔧 Alternativa Moderna: std::array (C++11)

Aunque las matrices estilo C son válidas, C++11 ofrece `std::array` que proporciona mejor seguridad de tipos:

```cpp
#include <iostream>
#include <array>
using namespace std;

int main() {
    // Usando std::array en lugar de matriz estilo C
    array<array<int, 3>, 3> matriz = {{
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    }};
    
    // Acceso igual que matrices estilo C
    cout << matriz[0][0] << endl;
    
    // Ventajas: métodos como size(), iteradores, etc.
    cout << "Tamaño: " << matriz.size() << "x" << matriz[0].size() << endl;
    
    return 0;
}
```

**Ventajas de `std::array`**:
- Mejor seguridad de tipos
- Métodos útiles (`size()`, `fill()`, etc.)
- Compatible con algoritmos STL
- Sin overhead de rendimiento

---

*Documento creado para práctica y aprendizaje de matrices estáticas en C++*

