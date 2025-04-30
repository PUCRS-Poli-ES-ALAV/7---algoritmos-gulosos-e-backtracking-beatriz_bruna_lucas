def troco_guloso(valor):
    tipos_moeda = [100, 50, 25, 10, 5, 1]
    troco = []

    for moeda in tipos_moeda:
        while valor >= moeda:
            troco.append(moeda)
            valor -= moeda
    return troco


valor = float(input("Digite o valor do troco (em centavos): ")) * 100;

resultado = troco_guloso(valor)
print("Moedas usadas:", resultado)