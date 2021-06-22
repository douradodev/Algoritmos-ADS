# Entrada 

numero_int= int(input("Digite um valor de 3 digitos: "))

# Processamento

numero1= numero_int// 100
numero2= (numero_int%100)//10
numero3= numero_int - (numero1*100)- (numero2 *10)

soma= numero1 + numero2 + numero3
# Saída

print("{} + {} + {} = {}".format(numero1,numero2,numero3,soma))

