# Entrada

meses = int(input("Digite o valor de meses: "))

# Processamento

anos= meses // 12
meses_reais= meses % 12

# Saída

print("{} ano e {} meses".format(anos, meses_reais))