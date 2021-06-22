def main():
	n = int(input("Digite um valor: "))
	limite_inf = int(input("Limite inferior: "))
	limite_sup = int(input("Limite superior: "))
	
	for c in range(limite_inf+1 ,limite_sup):
		if c % n == 0:
			print(c)
main()