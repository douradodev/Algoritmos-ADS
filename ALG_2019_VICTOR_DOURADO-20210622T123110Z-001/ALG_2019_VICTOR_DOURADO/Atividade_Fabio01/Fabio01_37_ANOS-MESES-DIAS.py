# Entrada

dias= int(input("Digite seu numero de dias: "))

# Processamento

meses= dias//30
dias_reais= dias % 30
anos= meses // 12
meses_reais= meses % 12

# Saída

print("{} anos, {} meses e {} dias ".format(anos, meses_reais, dias_reais))