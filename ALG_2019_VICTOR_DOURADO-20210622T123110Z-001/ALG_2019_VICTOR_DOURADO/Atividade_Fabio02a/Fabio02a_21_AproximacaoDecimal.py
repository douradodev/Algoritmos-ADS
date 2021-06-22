def main():
	n = float(input("Digite um numero decimal: "))
	if n % 1 > 0.5:
		print((n // 1)+ 1)
	else:
		print(n//1)
main()