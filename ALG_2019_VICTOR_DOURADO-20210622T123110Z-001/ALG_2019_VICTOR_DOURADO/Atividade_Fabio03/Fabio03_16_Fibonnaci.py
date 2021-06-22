def main():
	n = int(input("Digite um valor maior ou igual a 2: "))
	fibo =0
	nacci = 1
	for c in range(1, n+1):
		fibo = fibo + nacci
		nacci = fibo -nacci
		
		print(fibo)
main()		