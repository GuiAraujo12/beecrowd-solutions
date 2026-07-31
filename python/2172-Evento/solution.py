aumento_exp, exp_atual = map(int, input().split())
novo_exp = aumento_exp*exp_atual
while aumento_exp and exp_atual != 0:
    print(novo_exp)
    aumento_exp, exp_atual = map(int, input().split())
    novo_exp = aumento_exp*exp_atual
