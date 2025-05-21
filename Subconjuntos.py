from itertools import combinations

def encontrar_subconjunto_zero(nums):
    """
    Retorna o primeiro subconjunto não-vazio cuja soma seja zero.
    """
    n = len(nums)
    for i in range(1, n + 1):
        for combo in combinations(nums, i):
            if sum(combo) == 0:
                return list(combo)
    return None

def todos_subconjuntos_zero(nums):
    """
    Retorna todos os subconjuntos não-vazios cuja soma seja zero.
    """
    subconjuntos = []
    n = len(nums)
    for i in range(1, n + 1):
        for combo in combinations(nums, i):
            if sum(combo) == 0:
                subconjuntos.append(list(combo))
    return subconjuntos

# =========================
# EXEMPLOS DE USO
# =========================

conjunto = [-7, -3, -2, 5, 8]

# Exemplo 1: Apenas um subconjunto com soma zero
um_subconjunto = encontrar_subconjunto_zero(conjunto)
print("Um subconjunto com soma zero:", um_subconjunto)

# Exemplo 2: Todos os subconjuntos com soma zero
todos = todos_subconjuntos_zero(conjunto)
print("Todos os subconjuntos com soma zero:")
for s in todos:
    print(s)
