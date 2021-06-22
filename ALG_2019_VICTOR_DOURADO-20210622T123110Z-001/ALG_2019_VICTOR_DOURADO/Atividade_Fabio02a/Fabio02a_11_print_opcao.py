def main():
	opcao = int(input("Digite 1, 2 ou 3: "))
	
	num1 = int(input("Digite um 1° numero: "))
	num2 = int(input("Digite um 2° numero: "))
	num3 = int(input("Digite um 3° numero qualquer: "))
	
	while opcao <1 and opcao >3 :
		opcao = int(input("Digite corretamente: "))
	
	if opcao == 1:
		print(num1)
	elif opcao == 2:
		print(num2)
	else:
		print(num3)
	
main()
	