import time

class Contador:
    def __init__(self):
        self.iteracoes = 0
        self.tempo_inicio = 0
        self.tempo_fim = 0

    def iniciar_timer(self):
        self.tempo_inicio = time.time()

    def parar_timer(self):
        self.tempo_fim = time.time()

    def tempo_execucao(self):
        return self.tempo_fim - self.tempo_inicio

def resolver_n_rainhas(n, contador):
    def pode_colocar(rainhas, linha, coluna):
        for r, c in enumerate(rainhas):
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
                backtrack(linha + 1, rainhas, solucoes)
                rainhas.pop()

    contador.iniciar_timer()
    solucoes = []
    backtrack(solucoes=solucoes)
    contador.parar_timer()
    return solucoes

def imprimir_tabuleiros(solucoes, n, limite=None):
    if limite:
        solucoes = solucoes[:limite]  # Para limitar a quantidade impressa
    for idx, sol in enumerate(solucoes):
        print(f"Solução {idx + 1}:")
        print("  " + " ".join(str(i) for i in range(n))) 
        for linha, coluna in enumerate(sol):
            linha_str = " ".join("Q" if i == coluna else "." for i in range(n))
            print(f"{linha} {linha_str}")
        print()

contador = Contador()
solucoes = resolver_n_rainhas(4, contador)

print(f"\n{len(solucoes)} soluções encontradas para N=4\n")
print("Iterações:", contador.iteracoes)
print("Tempo de execução (ms):", round(contador.tempo_execucao()*1000, 6))
imprimir_tabuleiros(solucoes, 4, limite=1)