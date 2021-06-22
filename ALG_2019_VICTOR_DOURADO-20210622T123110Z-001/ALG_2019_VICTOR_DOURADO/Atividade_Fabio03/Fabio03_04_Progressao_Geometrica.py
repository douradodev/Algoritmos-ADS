def main():
	a0 = int(input("Termo inicial: "))
	limite = int(input("Termo final: "))
	R = int(input("Razao: "))
	t = a0
	for c in range(a0,limite+1):
		if t <= limite:
			print(t)
		t = t* R
main()