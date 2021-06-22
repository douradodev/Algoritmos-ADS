def main():
	limite_inf = int(input("Limite inferior: "))
	limite_sup = int(input("Limite superior: "))
	
	for i in range(limite_inf, limite_sup+1):
		h = 0
		for c in range(1,i +1 ):
			if i % c == 0:
				h += 1
		if h == 2:
			print(c)
main()