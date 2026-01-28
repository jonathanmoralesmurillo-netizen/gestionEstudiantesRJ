# Polimorfismo en la Clase Producto - Explicación

## ¿Qué es el Polimorfismo?

El **polimorfismo** permite que diferentes tipos de productos respondan al mismo método `calcularPrecioVenta()`, pero cada uno ejecute su propia lógica específica.

---

## Jerarquía de Clases Producto

```
                    Producto (clase abstracta)
                    │
                    ├─── calcularPrecioVenta() = 0  (virtual puro)
                    │
        ┌───────────┴───────────┐
        │                       │
   Perecedero            NoPerecedero
        │                       │
        │                       ├─── Electronico
        │                       │
        │                       └─── Abarrotes
```

---

## Paso 1: Clase Base Producto (Abstracta)

```cpp
class Producto {
protected:
    char* codigo;
    char* nombre;
    double precio;

public:
    // Método virtual puro - DEBE ser implementado por las subclases
    virtual double calcularPrecioVenta() const = 0;
};
```

**Características importantes:**
- `virtual`: Permite el enlace dinámico (resolución en tiempo de ejecución)
- `= 0`: Hace el método **virtual puro** (sin implementación)
- La clase `Producto` es **abstracta** (no se puede instanciar)
- Todas las subclases DEBEN implementar este método

---

## Paso 2: Implementación en Perecedero

```cpp
class Perecedero : public Producto {
    // ...
    double calcularPrecioVenta() const override;
};

// Implementación
double Perecedero::calcularPrecioVenta() const {
    return precio * 1.40;  // Precio base + 40% de utilidad
}
```

**Ejemplo:**
- Precio base: $2.50
- Precio venta: $2.50 × 1.40 = **$3.50**

---

## Paso 3: Implementación en NoPerecedero

```cpp
class NoPerecedero : public Producto {
    // ...
    double calcularPrecioVenta() const override;
};

// Implementación
double NoPerecedero::calcularPrecioVenta() const {
    return precio * 1.15;  // Precio base + 15% de utilidad
}
```

**Ejemplo:**
- Precio base: $1.20
- Precio venta: $1.20 × 1.15 = **$1.38**

---

## Paso 4: Implementación en Electronico

```cpp
class Electronico : public NoPerecedero {
    // ...
    double calcularPrecioVenta() const override;
};

// Implementación
double Electronico::calcularPrecioVenta() const {
    double precioBase = precio * 1.10;  // Precio base + 10% de utilidad
    
    // Si tiene cliente frecuente con tarjeta, aplicar descuento
    if (clienteFrecuente && clienteFrecuente->getTarjetaDescuento()) {
        double porcentajeDescuento = 
            clienteFrecuente->getTarjetaDescuento()->getPorcentajeDescuento();
        double descuento = precioBase * (porcentajeDescuento / 100.0);
        precioBase -= descuento;
    }
    
    return precioBase;
}
```

**Ejemplo con descuento:**
- Precio base: $500.00
- Con 10% utilidad: $500.00 × 1.10 = $550.00
- Con 10% descuento de tarjeta: $550.00 - $55.00 = **$495.00**

---

## Paso 5: Abarrotes (Hereda la Implementación)

```cpp
class Abarrotes : public NoPerecedero {
    // NO sobrescribe calcularPrecioVenta()
    // Usa la implementación heredada de NoPerecedero
};
```

**Ejemplo:**
- Precio base: $1.50
- Precio venta: $1.50 × 1.15 = **$1.73** (heredado de NoPerecedero)

---

## Cómo Funciona el Polimorfismo

### Ejemplo Práctico:

```cpp
// Crear diferentes tipos de productos
Producto* productos[4];

productos[0] = new Perecedero("P001", "Leche", 2.50, 1000, fecha);
productos[1] = new NoPerecedero("NP001", "Arroz", 1.20, "Costa Rica");
productos[2] = new Electronico("E001", "Smartphone", 500.00, "China", 2, cliente);
productos[3] = new Abarrotes("A001", "Frijoles", 1.50, "CR", "Proveedor", ...);

// Polimorfismo: todos responden al mismo método
for (int i = 0; i < 4; i++) {
    double precioVenta = productos[i]->calcularPrecioVenta();
    printf("%s: $%.2f\n", productos[i]->getNombre(), precioVenta);
}
```

### Ejecución Paso a Paso:

1. **productos[0] (Perecedero)**:
   - Se llama `calcularPrecioVenta()`
   - Enlace dinámico encuentra que es `Perecedero`
   - Ejecuta: `Perecedero::calcularPrecioVenta()`
   - Resultado: $2.50 × 1.40 = **$3.50**

2. **productos[1] (NoPerecedero)**:
   - Se llama `calcularPrecioVenta()`
   - Enlace dinámico encuentra que es `NoPerecedero`
   - Ejecuta: `NoPerecedero::calcularPrecioVenta()`
   - Resultado: $1.20 × 1.15 = **$1.38**

3. **productos[2] (Electronico)**:
   - Se llama `calcularPrecioVenta()`
   - Enlace dinámico encuentra que es `Electronico`
   - Ejecuta: `Electronico::calcularPrecioVenta()`
   - Resultado: $500.00 × 1.10 - descuento = **$495.00**

4. **productos[3] (Abarrotes)**:
   - Se llama `calcularPrecioVenta()`
   - No tiene implementación propia
   - Usa la heredada de `NoPerecedero`
   - Resultado: $1.50 × 1.15 = **$1.73**

---

## Tabla Comparativa

| Clase | Fórmula | Ejemplo (precio = $100) | Resultado |
|-------|---------|-------------------------|-----------|
| **Perecedero** | `precio × 1.40` | $100 × 1.40 | **$140.00** |
| **NoPerecedero** | `precio × 1.15` | $100 × 1.15 | **$115.00** |
| **Electronico** (sin descuento) | `precio × 1.10` | $100 × 1.10 | **$110.00** |
| **Electronico** (con 10% descuento) | `precio × 1.10 × 0.90` | $100 × 1.10 × 0.90 | **$99.00** |
| **Abarrotes** | `precio × 1.15` (heredado) | $100 × 1.15 | **$115.00** |

---

## Ventajas del Polimorfismo

1. **Mismo método, diferentes comportamientos**: Todos los productos tienen `calcularPrecioVenta()`, pero cada uno calcula diferente.

2. **Código más limpio**: No necesitamos `if/else` o `switch` para determinar el tipo de producto.

3. **Extensibilidad**: Si agregamos un nuevo tipo de producto, solo creamos la clase y el resto del código funciona automáticamente.

4. **Reutilización**: La clase `Caja` puede trabajar con cualquier `Producto*` sin conocer su tipo específico.

---

## Resumen

**Polimorfismo en Producto significa:**
- ✅ Todos los productos tienen el método `calcularPrecioVenta()`
- ✅ Cada tipo de producto calcula el precio de forma diferente
- ✅ Se puede tratar todos los productos de manera uniforme usando `Producto*`
- ✅ El método correcto se ejecuta automáticamente según el tipo real del objeto

**Ejemplo visual:**

```
Producto* p = new Perecedero(...);
p->calcularPrecioVenta();  // Ejecuta Perecedero::calcularPrecioVenta()

Producto* p = new Electronico(...);
p->calcularPrecioVenta();  // Ejecuta Electronico::calcularPrecioVenta()
```

El mismo código (`p->calcularPrecioVenta()`) ejecuta diferentes métodos según el tipo real del objeto. **Eso es polimorfismo**.
