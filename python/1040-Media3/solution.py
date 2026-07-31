n1, n2, n3, n4 = map(float, input().split())
nota1 = ((n1*2) + (n2*3) + (n3*4) + (n4*1)) / 10
print(f"Media: {nota1:.1f}")
if nota1 >= 7:
    print("Aluno aprovado.")
elif nota1 < 5:
    print("Aluno reprovado.")
elif nota1 >= 5 and nota1 < 6.9:
    print("Aluno em exame.")
    notaexame = float(input())
    print(f"Nota do exame: {notaexame:.1f}")
    notafim = (notaexame + nota1) / 2
    if notafim >= 5:
        print("Aluno aprovado.")
    elif notafim <= 4.9:
        print("Aluno reprovado.")
    print(f"Media final: {notafim:.1f}")   
