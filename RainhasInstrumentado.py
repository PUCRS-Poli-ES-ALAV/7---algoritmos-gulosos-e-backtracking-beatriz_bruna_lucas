import time

class Contador:
    def __init__(self):
        self.iteracoes = 0
        self.instrucoes = 0

def resolver_n_rainhas(n, contador):
    def pode_colocar(rainhas, linha, coluna):
        for r, c in enumerate(rainhas):
            contador.instrucoes += 1
            if c == coluna or abs(c - coluna) == abs(r - linha):
                return False
        return True

    def backtrack(linha=0, rainhas=[], solucoes=[]):
        if linha == n:
            solucoes.append(rainhas[:])
            return
        for coluna in range(n):
            contador.iteracoes += 1
            if pode_colocar(rainhas, linha, coluna):
                rainhas.append(coluna)
                contador.instrucoes += 1
                backtrack(linha + 1, rainhas, solucoes)
                rainhas.pop()
                contador.instrucoes += 1

    solucoes = []
    backtrack(solucoes=solucoes)
    return solucoes

contador = Contador()
inicio = time.time()
solucoes = resolver_n_rainhas(4, contador)
fim = time.time()

print(f"{len(solucoes)} soluções encontradas para N=4")
print("Iterações:", contador.iteracoes)
print("Instruções:", contador.instrucoes)
print("Tempo de execução (s):", round(fim - inicio, 6))
