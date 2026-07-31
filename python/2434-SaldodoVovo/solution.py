dias, saldo_inicio = map(int, input().split())
soma = int(saldo_inicio)
for i in range(dias):
    n = int(input())
    soma += n
    if saldo_inicio < soma:
        menor_saldo = saldo_inicio
    else:
        menor_saldo = soma
        saldo_inicio = soma
    
print(menor_saldo)
