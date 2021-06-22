# Entrada

anos= int(input("Digite seu numero de anos: "))
meses= int(input("Digite seu numero de meses: "))
dias= int(input("Digite seu numero de dias: "))

# Processamento

dias_anos= anos*365
dias_meses= meses*30
dias_reais = dias_anos + dias_meses + dias

# Saída

print(" Você viveu {} dias".format(dias_reais))