# Fase 5 - Evaluación Final POA
# Estudiante: Ferney Santiago Calvo Mora
# Grupo: 213022B_2204
# Problema 3: Control de inventario y reabastecimiento

# Matriz de inventario: [Código del artículo, Nombre del artículo, Stock actual, Stock mínimo requerido]
INVENTARIO = [
    ["ART-001", "Teclado mecánico", 8, 15],
    ["ART-002", "Mouse inalámbrico", 25, 20],
    ["ART-003", "Monitor LED 24 pulgadas", 4, 10],
    ["ART-004", "Cable HDMI 2m", 30, 30],
    ["ART-005", "Memoria USB 64GB", 12, 25],
]


def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Determina la cantidad exacta a solicitar para reabastecer un artículo.
    Si el stock actual es menor al mínimo requerido, retorna la diferencia;
    de lo contrario, retorna 0.
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


def generar_informe_reabastecimiento(matriz_inventario):
    """Recorre la matriz de inventario y muestra la lista de cantidades a pedir."""
    print("=== INFORME DE REABASTECIMIENTO DE INVENTARIO ===\n")
    for articulo in matriz_inventario:
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        cantidad_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)

        print(f"Artículo: {nombre} ({codigo}) | Cantidad a solicitar: {cantidad_pedir}")


if __name__ == "__main__":
    generar_informe_reabastecimiento(INVENTARIO)
