# Entrada

anos_cigarro= int(input("Digite o numero de anos que ele fuma: "))
cigarros_dia= int(input("Digite o numero de cigarros por dia: "))
preço= int(input("Digite o preço da cartela: "))

# Processamento

dias= anos_cigarro * 365
cigarros= cigarros_dia * dias
cartela= cigarros / 20
gasto_total= cartela * preço

# Saída

print("O total gasto é {}".format(gasto_total))