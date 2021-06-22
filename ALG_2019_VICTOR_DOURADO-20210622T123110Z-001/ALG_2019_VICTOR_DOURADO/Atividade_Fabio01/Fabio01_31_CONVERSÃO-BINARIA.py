# Entrada

binario= int(input("Digite um numero binario: "))

# Processamento

numero1 = binario // 1000
sobra1 = binario % 1000
numero2 = sobra1 // 100
sobra2= sobra1 % 100
numero3 = sobra2 // 10
numero4 = sobra2 % 10

# Calc. bin

decimal1= numero1 * (2**3)
decimal2= numero2 * (2**2)
decimal3= numero3 * (2**1)
decimal4= numero4 * (2**0)
base10= decimal1 + decimal2 + decimal3 + decimal4
# Saída

print(" O numero em decimal é {} ".format(base10))
