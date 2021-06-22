def main():
	n = int(input("Digite um valor: "))
	soma = 0
	
	for c in range(1, n+1):
		c = int(input("Digite: "))
		soma = soma + c
	media = soma/n
	print("A soma é {}".format(soma))
	print("A média é {}".format(media))
main()
		