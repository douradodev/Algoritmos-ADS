def main():
	seq = 1
	soma = 0
	for c in range(1, 100, 2):
		print("{}/{}".format(seq, c))
		seq = seq + 1
		s = seq/c
		soma = soma + s
	print("A soma é {:.2f}".format(soma))
main()