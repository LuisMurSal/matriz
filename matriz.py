# Definición de la matriz de costos (13x13)
cost_matrix = [
    [-3, -3, 2, -3, 3, -2, -2, 1, 2, 0, 2, 0, 1],
    [2, 3, -1, -1, -1, 3, 2, 0, -3, -3, 2, 2, 1],
    [1, -3, -3, 2, 3, 1, 3, 3, 2, 1, -2, -2, 3],
    [0, 0, 3, 0, 3, -3, -2, -3, 0, 2, 2, 1, 1],
    [2, -1, -1, -3, 3, 3, 0, -3, 1, -2, 2, 0, 1],
    [0, 3, -1, 1, -1, -2, 2, -2, 2, -1, -2, -3, 0],
    [0, 3, 2, 0, 1, 1, 2, 3, -1, -2, 0, 0, -2],
    [3, 3, -3, -2, 3, -3, 1, -3, 3, -2, 2, -2, -1],
    [-2, -2, 1, 0, -1, 0, 3, 0, 0, -2, 2, -3, -1],
    [-3, 3, 0, -1, -3, 1, 2, -3, 2, -3, 0, 2, -2],
    [-3, -3, -3, 3, -2, 0, -2, -3, 1, 0, 1, -1, -2],
    [-1, 0, 1, 2, 1, 0, -2, 0, -3, 3, 3, -2, -1],
    [1, -3, 1, 0, 1, 2, 3, 1, -2, 3, 3, 0, 4]
]

start = (0, 0)  # Coordenadas de inicio (I)
end = (12, 12)  # Coordenadas de fin (F)

def is_valid_move(x, y, visited):
    return 0 <= x < 13 and 0 <= y < 13 and (x, y) not in visited

def dfs(x, y, current_cost, visited, costs):
    # Si alcanzamos el destino, agregamos el costo a la lista
    if (x, y) == end:
        costs.append(current_cost)
        return

    # Marcar la celda como visitada
    visited.add((x, y))

    # Posibles movimientos: abajo, arriba, derecha, izquierda
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for move in moves:
        new_x, new_y = x + move[0], y + move[1]
        if is_valid_move(new_x, new_y, visited):
            dfs(new_x, new_y, current_cost + cost_matrix[new_x][new_y], visited, costs)

    # Desmarcar la celda antes de retroceder
    visited.remove((x, y))

def find_routes():
    costs = []
    visited = set()
    dfs(start[0], start[1], cost_matrix[start[0]][start[1]], visited, costs)

    if costs:
        min_cost = min(costs)
        max_cost = max(costs)
        return min_cost, max_cost
    else:
        return None, None

# Ejecución del algoritmo
min_cost, max_cost = find_routes()
print(f'Minimo costo: {min_cost}')
print(f'Maximo costo: {max_cost}')
