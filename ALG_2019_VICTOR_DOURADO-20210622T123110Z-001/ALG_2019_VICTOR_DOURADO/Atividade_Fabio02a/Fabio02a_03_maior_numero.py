def main():
	# Entrada
	n1 = int(input("Valor 1: "))
	n2 = int(input("Valor 2: "))
	n3 = int(input("Valor 3: "))
	
	# Processamento e saída
	if n1 > n2 and n1 > n3:
		print("Maior valor: {}".format(n1))
	elif n2 > n1 and n2 > n3:
		print("Maior valor: {}".format(n2))
	else:
		print("Maior valor: {}".format(n3))
main()