def main():
	n1 = int(input("Digite o valor1: "))
	n2= int(input("Digite o valor2: "))
	
	op  = int(input("""
	1- Adicao
	2- Subtracao
	3- Multiplicacao
	4- Divisao 
	: """))
	if op == 1:
		print(n1 + n2)
	elif op == 2:
		print(n1 - n2)
	elif op == 3:
		print(n2 * n1)
	elif op == 4:
		print(n1 / n2)
		
main()
	