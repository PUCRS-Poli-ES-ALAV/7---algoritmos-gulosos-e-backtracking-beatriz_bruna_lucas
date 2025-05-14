def resolver_n_rainhas(n):
    def pode_colocar(rainhas, linha, coluna):
        for r, c in enumerate(rainhas):
            if c == coluna or abs(c - coluna) == abs(r - linha):
                return False
        return True

    def backtrack(linha=0, rainhas=[], solucao=[]):
        if linha == n:
            solucao.append(rainhas[:])
            return
        for coluna in range(n):
            if pode_colocar(rainhas, linha, coluna):
                rainhas.append(coluna)
                backtrack(linha + 1, rainhas, solucao)
                rainhas.pop()

    solucao = []
    backtrack(solucao=solucao)
    return solucao

def imprimir_tabuleiro(solucoes, n):
    for idx, sol in enumerate(solucoes):
        print(f"Solução {idx + 1}:")
        print("  " + " ".join(str(i) for i in range(n)))
        for linha, coluna in enumerate(sol):
            linha_str = " ".join("Q" if i == coluna else "." for i in range(n))
            print(f"{linha} {linha_str}")
        print()

n = 4
solucoes = resolver_n_rainhas(n)
print(f"{len(solucoes)} soluções encontradas para N={n}:\n")
imprimir_tabuleiro(solucoes, n)
