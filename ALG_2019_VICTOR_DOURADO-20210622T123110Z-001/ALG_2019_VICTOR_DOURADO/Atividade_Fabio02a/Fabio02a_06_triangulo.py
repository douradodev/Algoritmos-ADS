def main():
	a = int(input("Digite um angulo: "))
	b = int(input("Digite um angulo: "))
	c = int(input("Digite um angulo: "))
	
	if (a + b + c) != 180:
		print("Triangulo não existe!")
	else:
		if a < 90 and b <90 and c < 90:
			print("Triangulo acutangulo!")
		elif a == 90 or b == 90 or c == 90:
			print("Triangulo retangulo!")
		elif a > 90 or b > 90 or c > 90:
			print("Triangulo obtusangulo")
		else:
			print("Triangulo nao existe")
main()