# Entrada

quantia= int(input("Digite o valor da quantia: "))

# Processamento

nota50 = quantia // 50
quantia1 = quantia % 50
nota10 = quantia1 // 10
quantia2 = quantia1 % 10
nota5 = quantia2 // 5
quantia3 = quantia2 % 5
nota1 = quantia3 // 1

# Saída

print("{} notas de 50, {} notas de 10, {} notas de 5 e {} notas de 1 real.".format(nota50, nota10, nota5, nota1))