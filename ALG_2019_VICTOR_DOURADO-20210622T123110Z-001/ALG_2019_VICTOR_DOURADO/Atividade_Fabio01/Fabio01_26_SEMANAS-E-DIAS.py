# Entrada

dias= int(input("Digite um numero inteiro de dias: "))

# Processamento

semanas= dias // 7
dias_reais= dias % 7

# Saída 

print("O valor é de {} semanas e {} dias.".format(semanas, dias_reais))