def main():
	n = int(input("digite um valor: "))
	soma = 0
	for c in range(1, n+1):
		soma = soma + c
		print("{} + {} = {}".format( soma-c, c,soma))
	print("O RESULTADO FINAL É",soma)
main()