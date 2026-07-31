numero = list(map(int, input().split()))
numero_maior = 0 
for i in numero:
    if i == 0:
        break
    elif i > numero_maior:
        numero_maior = i
print(numero_maior) 
