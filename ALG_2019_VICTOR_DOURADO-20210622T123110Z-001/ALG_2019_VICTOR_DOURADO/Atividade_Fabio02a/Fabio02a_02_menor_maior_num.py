def main():
	# Entrada
	n1 = int(input("Valor 1: "))
	n2 = int(input("Valor 2: "))
	
	# Processamento e saída
	if n1 > n2:
		print("O menor numero é {} e o maior é {}".format(n2, n1))
	else:
		print("O menor numero é {} e o maior é {}".format(n1, n2))
		
main()