def main():
	
	angulo = int(input("Digite um angulo: "))
	
	if angulo <= 90:
		print("Primeiro quadrante")
	elif angulo > 90 and angulo <= 180:
		print("Segundo quadrante")
	elif angulo > 180 and angulo <= 270:
		print("Terceiro quadrante")
	else:
		print("Quarto quadrante")
main()