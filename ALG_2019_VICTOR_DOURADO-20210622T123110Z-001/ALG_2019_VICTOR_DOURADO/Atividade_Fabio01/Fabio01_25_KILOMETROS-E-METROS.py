# Entrada

metros= int(input("Digite um numero de metros: "))

# Processamento

km= metros // 1000
metros_reais= metros% 1000

# Saída

print("O valor corresponde a {}km e {}m".format(km, metros_reais))
