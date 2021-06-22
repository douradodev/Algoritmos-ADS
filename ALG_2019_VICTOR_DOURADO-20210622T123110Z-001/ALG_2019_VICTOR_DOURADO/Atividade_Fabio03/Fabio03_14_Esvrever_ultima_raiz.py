def main():
	n  = int(input("Digite um valor: "))
	quad = 0
	certo = 0
	for c in range(1, n +1):
		quad = c**2
		if quad <= n:
			certo = quad
	if certo<= n:
		print(certo)
main()