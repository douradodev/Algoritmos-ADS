# Entrada

custo_fabrica= int(input("Digite o custo de fábrica: "))

# Processamento

percentagem = custo_fabrica * 0.28

imposto= custo_fabrica * 0.45

custo_consumidor= custo_fabrica + percentagem + imposto

# Saída

print("O custo ao consumidor é {}".format(custo_consumidor))

