p = int(input())
soma = 0
for i in range(p):
    produto, quant = map(int,input().split())
    if produto == 1001:
        soma += quant*1.50
    elif produto == 1002:
        soma += quant*2.50
    elif produto == 1003:
        soma += quant*3.50
    elif produto == 1004:
        soma += quant*4.50
    elif produto == 1005:
        soma += quant*5.50
        
print(f"{soma:.2f}")
    
