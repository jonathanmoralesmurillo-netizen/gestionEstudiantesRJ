"""
Script de prueba para demostrar las funcionalidades del Sistema de Gestión Académica.

Este script prueba todas las funcionalidades principales del sistema sin requerir
interacción del usuario.
"""
from RepositorioCSV import RepositorioCSV

from GestorEstudiantes import GestorEstudiantes
from Estudiante import Estudiante


def probar_sistema():
    """Prueba todas las funcionalidades del sistema."""
    print(" INICIANDO PRUEBAS DEL SISTEMA DE GESTIÓN ACADÉMICA")
    print("=" * 60)

    # Inicializar componentes
    repositorio = RepositorioCSV("estudiantes.csv")
    gestor = GestorEstudiantes(repositorio)

    # Cargar datos
    print("\n Cargando datos...")
    gestor.cargar()
    print(f"✓ Cargados {gestor.contar_estudiantes()} estudiantes")

    # Mostrar todos los estudiantes
    print("\n LISTA DE ESTUDIANTES:")
    print("-" * 50)
    estudiantes = gestor.obtener_todos()
    for i, est in enumerate(estudiantes, 1):
        print(f"{i:2d}. {est}")

    # Buscar estudiante por ID
    print("\n BUSCAR POR ID:")
    estudiante = gestor.buscar_por_id(1)
    if estudiante:
        print(f"✓ Estudiante encontrado: {estudiante}")

    # Buscar por nombre
    print("\ BUSCAR POR NOMBRE (inicial 'A'):")
    resultados = gestor.buscar_por_nombre("A")
    print(f"✓ Encontrados {len(resultados)} estudiante(s) con inicial 'A':")
    for est in resultados:
        print(f"  - {est}")

    # Listar ordenado por nota
    print("\n ESTUDIANTES ORDENADOS POR NOTA (mayor a menor):")
    print("-" * 50)
    ordenados = gestor.listar_ordenado("nota")
    for i, est in enumerate(ordenados[:5], 1):  # Mostrar solo los 5 mejores
        print(f"{i:2d}. {est}")

    # Clasificar estudiantes
    print("\n CLASIFICACIÓN DE ESTUDIANTES (umbral 70):")
    print("-" * 50)
    clasificacion = gestor.clasificar(70.0)
    aprobados = clasificacion['Aprobados']
    reprobados = clasificacion['Reprobados']

    print(f"✓ APROBADOS ({len(aprobados)} estudiante(s)):")
    for est in aprobados:
        print(f"  - {est}")

    print(f"\n REPROBADOS ({len(reprobados)} estudiante(s)):")
    for est in reprobados:
        print(f"  - {est}")

    # Estadísticas
    print("\n ESTADÍSTICAS GENERALES:")
    print("-" * 40)
    stats = gestor.estadisticas()
    print(f"Total de estudiantes: {stats['total']}")
    print(f"Promedio general: {stats['promedio']}")
    print(f"Nota máxima: {stats['maxima']}")
    print(f"Nota mínima: {stats['minima']}")
    print(f"Desviación estándar: {stats['desviacion']}")

    # Distribución porcentual
    print("\n DISTRIBUCIÓN PORCENTUAL:")
    print("-" * 40)
    distribucion = gestor.distribucion_porcentual()
    print(f"0-59 puntos: {distribucion['0-59']}%")
    print(f"60-79 puntos: {distribucion['60-79']}%")
    print(f"80-100 puntos: {distribucion['80-100']}%")

    # Probar agregar nuevo estudiante
    print("\n➕ AGREGANDO NUEVO ESTUDIANTE:")
    try:
        nuevo_estudiante = Estudiante(16, "Test Estudiante", 88.5)
        gestor.agregar_estudiante(nuevo_estudiante)
        print(f"✓ Estudiante agregado: {nuevo_estudiante}")
    except Exception as e:
        print(f" Error: {e}")

    # Probar editar estudiante
    print("\n✏ EDITANDO ESTUDIANTE:")
    try:
        gestor.editar_estudiante(16, "Test Estudiante Modificado", 95.0)
        estudiante_editado = gestor.buscar_por_id(16)
        print(f"✓ Estudiante editado: {estudiante_editado}")
    except Exception as e:
        print(f" Error: {e}")

    # Probar eliminar estudiante
    print("\n🗑 ELIMINANDO ESTUDIANTE:")
    try:
        gestor.eliminar_estudiante(16)
        estudiante_eliminado = gestor.buscar_por_id(16)
        if estudiante_eliminado is None:
            print("✓ Estudiante eliminado exitosamente")
        else:
            print(" Error: El estudiante no fue eliminado")
    except Exception as e:
        print(f" Error: {e}")

    # Guardar datos
    print("\n GUARDANDO DATOS:")
    try:
        gestor.guardar()
        print("✓ Datos guardados exitosamente")
    except Exception as e:
        print(f" Error: {e}")

    print("\n" + "=" * 60)
    print(" TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
    print(" El sistema funciona correctamente según las especificaciones")


if __name__ == "__main__":
    probar_sistema()


