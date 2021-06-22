# Entrada 

nota1= float(input("Digite sua 1° nota: "))
nota2= float(input("Digite sua 2° nota: "))
nota3= float(input("Digite sua 3°nota: "))
peso1= int(input("Digite o peso da 1° nota: "))
peso2= int(input("Digite o peso da 2° nota: "))
peso3= int(input("Digite o peso da 3° nota: "))
# Processamento

media= (nota1*peso1 + nota2*peso2 + nota3 *peso3) /3

# Saída 

print("A média ponderada é {}".format(media))