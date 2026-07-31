abas, num_acoes = map(int, input().split())
for i in range(num_acoes):
    acoes = input()
    if acoes == "fechou":
        abas += 1
    if acoes == "clicou":
        abas -= 1
print(abas)
