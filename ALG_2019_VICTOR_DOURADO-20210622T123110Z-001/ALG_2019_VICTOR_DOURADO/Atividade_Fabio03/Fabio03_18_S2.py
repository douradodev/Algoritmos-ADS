def main():
	n = int(input("Digite um valor: "))
	soma = 0
	for c in range(1, n+1):
		print("{}/{}".format( c, n))
		seq = c/n
		soma = soma + seq
		n = n - 1
	print("A soma é {:.2f}".format(soma))
main()
		