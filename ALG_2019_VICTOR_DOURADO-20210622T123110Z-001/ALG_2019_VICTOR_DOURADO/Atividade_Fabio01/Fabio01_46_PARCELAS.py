# Entrada

valor_mercadoria = int(input(" Digite o valor da mercadoria: "))

# Processamento

divisao = valor_mercadoria // 3
resto = valor_mercadoria % 3
entrada = divisao + resto

# Saída 

print(" A entrada é {} e as outras duas parcelas são {}".format(entrada, divisao))