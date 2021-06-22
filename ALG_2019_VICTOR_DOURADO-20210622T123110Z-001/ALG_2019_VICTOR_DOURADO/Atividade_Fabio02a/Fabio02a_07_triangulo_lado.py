def main():
	a = int(input("Lado 1: "))
	b = int(input("Lado 2: "))
	c = int(input("Lado 3: "))
	
	if a > b+c or b > a+c or c > a+b:
		print("O triangulo não existe ")
	else:
		print("O triangulo existe!")
		if a == b and b == c:
			print("O triangulo é equilatero !")
		elif a == b or a == c:
			print("O triangulo é isosceles")
		elif b == c or b == a:
			print("O triangulo é isosceles")
		elif c == b or c == a:
			print("O triangulo é isosceles")
		else:
			print("O triangulo é escaleno")
main()
	