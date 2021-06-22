# Entrada

numerador1= int(input("Digite um numerador: "))
denominador1= int(input("Digite um denominador: "))
numerador2= int(input("Digite outro numerador: "))
denominador2= int(input("Digite outro denominador: "))

# Processamento

mmc= denominador1 * denominador2
num1= numerador1 * denominador2
num2= numerador2 * denominador1
numerador_novo= num1+ num2 


# Saída

print("A soma de frações é {}/{}".format(numerador_novo, mmc))