# Entrada 

horas= int(input("Digite o valor das horas: "))

# Processamento

dias= horas // 24
horas_reais= horas % 24
semanas= dias // 7
dias_reais= dias% 7

# Saída 

print("{} semanas, {} dias e {} horas".format(semanas, dias_reais, horas_reais))