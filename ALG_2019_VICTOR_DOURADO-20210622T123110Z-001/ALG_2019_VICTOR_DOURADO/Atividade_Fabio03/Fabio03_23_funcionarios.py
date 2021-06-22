def main():
	n = int(input("Digite numero de funcionarios: "))
	
	for c in range(1, n+1):
		h = int(input("Horas trabalhadas: "))
		n = int(input("Numero de dependentes: "))
		salario = (h *12) + (40*n)
		inss = salario * 0.085
		ir = salario * 0.05
		salario_novo = salario - inss -ir
		print("FUNCIONADIO {} recebe {:.2f}R$".format(c, salario_novo))
		print("Desconto INSS: {:.2f}R$".format(inss))
		print("Desconto IR: {:.2f}R$".format(ir))
main()