# Entrada

numero = int(input("Digite um numero de 3 digitos: "))

# Processamento

digito1= numero // 100
digito2 = (numero % 100) //10
digito3 = numero - (digito1 * 100) - (digito2 * 10)

# Saída 

print(" O numero é {}{}{} ".format(digito3,  digito2, digito1))