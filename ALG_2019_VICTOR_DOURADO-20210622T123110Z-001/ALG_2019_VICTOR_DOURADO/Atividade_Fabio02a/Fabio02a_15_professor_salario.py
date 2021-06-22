def main():
	h1 = int(input("Qtd horas 1: "))
	valor1= int(input("Valor recebido por hora: "))
	h2 = int(input("Qtd horas 2: "))
	valor2 = int(input("Valor recebido por hora: "))
	
	salario1 = h1 * valor1
	salario2 = h2 * valor2
	
	if salario1 > salario2:
		print("O professor 1 recebe melhor!")
	else:
		print("O professor 2 recebe melhor!")
main()