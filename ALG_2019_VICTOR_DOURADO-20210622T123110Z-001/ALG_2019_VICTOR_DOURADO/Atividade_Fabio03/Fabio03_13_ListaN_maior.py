def main():
	n = int(input("Digite um valor: "))
	maior = 0
	for n in range (n):
		n = int(input("Digite: "))
		if n > maior:
			maior = n
	print(maior)
	
main()