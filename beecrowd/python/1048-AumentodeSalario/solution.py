salario = float(input())
if 0 < salario <= 400:
    salarionew = ((salario*15)/100) + salario
    print(f"Novo salario: {salarionew:.2f}")
    print(f"Reajuste ganho: {(salarionew - salario):.2f}")
    print(f"Em percentual: 15 %")
elif 400.01 <= salario <= 800:
    salarionew = ((salario*12)/100) + salario
    print(f"Novo salario: {salarionew:.2f}")
    print(f"Reajuste ganho: {(salarionew - salario):.2f}")
    print(f"Em percentual: 12 %")
elif 800.01 <= salario <= 1200:
    salarionew = ((salario*10)/100) + salario
    print(f"Novo salario: {salarionew:.2f}")
    print(f"Reajuste ganho: {(salarionew - salario):.2f}")
    print(f"Em percentual: 10 %") 
elif 1200.01 <= salario <= 2000:
    salarionew = ((salario*7)/100) + salario
    print(f"Novo salario: {salarionew:.2f}")
    print(f"Reajuste ganho: {(salarionew - salario):.2f}")
    print(f"Em percentual: 7 %")
elif salario > 2000:
    salarionew = ((salario*4)/100) + salario
    print(f"Novo salario: {salarionew:.2f}")
    print(f"Reajuste ganho: {(salarionew - salario):.2f}")
    print(f"Em percentual: 4 %")
