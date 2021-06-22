def main():
	n1 =int(input("Digite a nota1: "))
	n2 = int(input("Digite a nota2: "))
	media =( n1 + n2) / 2
	
	if media >= 7:
		print("Aluno aprovado!")
	else:
		print("aluno de recuperação!")
		recu = int(input("Digite a nota de recuperacao: "))
		nova_media = (media + recu)/ 2
		
		if nova_media >= 5:
			print("Aluno aprovado")
		else:
			print("Aluno reprovado")
main()
		