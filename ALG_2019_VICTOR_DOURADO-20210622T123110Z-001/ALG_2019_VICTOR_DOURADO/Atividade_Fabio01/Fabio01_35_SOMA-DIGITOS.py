# Entrada

numero= int(input("Digite um numero de 4 digitos: "))

# Processamento
 
 #Calc.
numero1 = numero // 1000
sobra1 = numero % 1000
numero2 = sobra1 // 100
sobra2= sobra1 % 100
numero3 = sobra2 // 10
numero4 = sobra2 % 10
#Soma
soma= numero1 + numero2 + numero3 + numero4

print("A soma de seus digitos é {}".format(soma))
