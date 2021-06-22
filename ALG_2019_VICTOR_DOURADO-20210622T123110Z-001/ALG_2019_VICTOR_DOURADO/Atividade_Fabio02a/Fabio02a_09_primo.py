def main():
	primo = int(input("Digite um numero entre 1 e 100: "))
	cont= 1
	divisor = 0
	while cont <= primo:
		if primo % cont == 0:
			divisor += 1
		cont +=1
	if divisor == 0:
		print("Numero é primo")
	else:
		print("Numero nao é primo")
main()