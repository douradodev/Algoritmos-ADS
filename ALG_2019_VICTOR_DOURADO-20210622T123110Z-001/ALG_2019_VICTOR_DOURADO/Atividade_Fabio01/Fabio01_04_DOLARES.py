# Entrada

valor_dolar= float(input("Digite o valor do dolar: "))
quantidade_dolar= int(input("Quantidade de dolares: "))

# Processamento

reais= valor_dolar * quantidade_dolar

# Saída

print("O valor equivale a {:.2f} reais".format(reais))