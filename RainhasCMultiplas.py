def resolver_n_rainhas(n):
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
            if pode_colocar(rainhas, linha, coluna):
                rainhas.append(coluna)
                backtrack(linha + 1, rainhas, solucoes)
                rainhas.pop()

    solucoes = []
    backtrack(solucoes=solucoes)
    return solucoes

def imprimir_tabuleiros(solucoes, n, limite=None):
    if limite:
        solucoes = solucoes[:limite] #para evitar infinitas soluções
    for idx, sol in enumerate(solucoes):
        print(f"Solução {idx + 1}:")
        print("  " + " ".join(str(i) for i in range(n))) 
        for linha, coluna in enumerate(sol):
            linha_str = " ".join("Q" if i == coluna else "." for i in range(n))
            print(f"{linha} {linha_str}")
        print()

n = 7
todas_solucoes = resolver_n_rainhas(n)
print(f"\n{len(todas_solucoes)} soluções encontradas para N = {n}:\n")
imprimir_tabuleiros(todas_solucoes, n, limite=5)
