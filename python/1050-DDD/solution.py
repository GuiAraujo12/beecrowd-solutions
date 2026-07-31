ddd = int(input())
procurando_ddd = False
soma = -1
list_ddd = [61, 71, 11, 21, 32, 19, 27, 31]
list_city = ["Brasilia", 
             "Salvador", 
             "Sao Paulo", 
             "Rio de Janeiro", 
             "Juiz de Fora", 
             "Campinas", 
             "Vitoria", 
             "Belo Horizonte"]
for i in list_ddd:
    soma += 1
    if ddd == i:
        print(list_city[soma])
        procurando_ddd = True 
        
if procurando_ddd == False:
    print("DDD nao cadastrado")
