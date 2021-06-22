def main():
	# Entrada
	n1 = int(input("Valor 1: "))
	n2 = int(input("Valor 2: "))
	n3 = int(input("Valor 3: "))
	
	# Processamento e Saída
	if n1 == n2 == n3:
		print("Existem 3 valores iguais")
	elif n1 == n2 or n1 == n3:
		print("Existem 2 valores iguais")
	elif n2 == n1 or n2 == n3:
		print("Existem 2 valores iguais")
	elif n3 == n1 or n3 == n2:
		print("Existem 2 valores iguais")
	else:
		print("Todos os valores são diferentes")
main()