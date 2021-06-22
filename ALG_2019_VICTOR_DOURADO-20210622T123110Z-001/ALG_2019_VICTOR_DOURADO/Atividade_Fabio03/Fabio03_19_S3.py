def main():
	n = int(input("Digite um valor: "))
	seq = 0
	soma = 0
	for c in range(1, n+1):
		if c % 2 != 0:
			seq = c / n
			soma = soma + seq
			print(" +{}/{}".format(c, n))
		else:
			seq = -n / c
			soma = soma + seq
			print(" -{}/{}".format(n, c))
		n = n -1
	print("{:.2f}".format(soma))
main()
			
		
			