refeiçoes = list(map(int, input().split()))
pedidos = list(map(int, input().split()))
soma = 0 
for i in range(len(refeiçoes)):
    if refeiçoes[i] < pedidos[i]:
        soma += pedidos[i] - refeiçoes[i]
    elif pedidos[i] == refeiçoes[i]:
        soma += 0
print(soma)
