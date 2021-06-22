def main():
	n = int(input("Digite um valor: "))
	seq = 1
	soma = 0
	for c in range(1, n+1):
		print("{}/{}".format(seq, c))
		s = seq/c
		soma = soma + s
	print("A soma é {:.2f}".format(soma))
main()
		