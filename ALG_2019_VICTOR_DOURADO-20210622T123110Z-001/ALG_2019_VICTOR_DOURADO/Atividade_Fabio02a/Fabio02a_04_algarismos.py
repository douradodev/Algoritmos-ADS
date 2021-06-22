def main():
	n = int(input("Digite um valor de 2 digitos: "))
	
	dezena = n//10
	unidade = n%10
	
	if dezena == unidade:
		print("Os algarismos são iguais")
	else:
		print("Os algarismos não são iguais")
main()