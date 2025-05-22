import time
import itertools

class Contador:
    def __init__(self):
        self.iteracoes = 0

def encontrar_todos_subconjuntos_zero(nums, contador):
    subconjuntos = []
    n = len(nums)
    for i in range(1, n + 1):
        for combo in itertools.combinations(nums, i):
            contador.iteracoes += 1
            if sum(combo) == 0:
                subconjuntos.append(list(combo))
    return subconjuntos

conjunto = [-7, -3, -2, 5, 8]
contador = Contador()
inicio = time.time()
resultado = encontrar_todos_subconjuntos_zero(conjunto, contador)
fim = time.time()

print("\nConjunto:", conjunto)
print("\nSubconjuntos com soma zero:", resultado)
print("Iterações:", contador.iteracoes)
print("Tempo de execução (s):", round(fim - inicio, 6))
print("Soluções encontradas:", len(resultado))