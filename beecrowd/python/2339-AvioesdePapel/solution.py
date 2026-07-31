num_comp, quant_folhas, folhas_comp = map(int, input().split())
if quant_folhas/num_comp < folhas_comp:
    print("N")
else:
    print("S")
