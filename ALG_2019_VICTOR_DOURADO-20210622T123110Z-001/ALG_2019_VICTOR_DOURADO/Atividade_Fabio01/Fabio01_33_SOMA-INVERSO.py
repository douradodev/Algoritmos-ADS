# Entrada

numero = int(input("Digite um numero de 3 digitos: "))

# Processamento

# Calc. 
digito1= numero // 100
digito2 = (numero % 100) //10
digito3 = (numero % 100) % 10
# Inverso 
numerostr= str(digito3)+ str(digito2) + str(digito1)
inverso= int(numerostr)
# Soma
soma= numero + inverso

# Saída
print("A soma de {} e {} é {}".format(numero, inverso, soma))