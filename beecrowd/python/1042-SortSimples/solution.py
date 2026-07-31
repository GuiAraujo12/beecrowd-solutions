a, b, c = map(int, input().split())
valores = [a, b, c]
for i in range(2):
    for j in range(2):
        if valores[j] > valores[j+1]:
            valores[j], valores[j+1] = valores[j+1], valores[j]
print(valores[0])
print(valores[1])
print(valores[2])
print()
print(a)
print(b)
print(c)
