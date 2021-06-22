def main():
	a0 = int(input("Termo inicial: "))
	limite = int(input("termo final"))
	R = int(input("Razao: "))
	
	for c in range(a0, limite, R):
		print(c)
		
main()