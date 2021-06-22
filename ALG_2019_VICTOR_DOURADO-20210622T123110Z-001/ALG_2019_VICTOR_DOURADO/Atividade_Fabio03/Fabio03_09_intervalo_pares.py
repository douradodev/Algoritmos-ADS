def main():
	limite_inf = int(input("Limite inferior: "))
	limite_sup = int(input("Limite superior: "))
	
	for c in range(limite_inf+1 ,limite_sup):
		if c % 2 == 0:
			print(c)
main()