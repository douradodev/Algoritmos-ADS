def main():
	n1 = int(input("digite um valor: "))
	n2 = int(input("digite um valor: "))
	n3 = int(input("digite um valor: "))
	n4 = int(input("digite um valor: "))
	n5 = int(input("Digite um valor:"))
	media = (n1 + n2 + n3 + n4 + n5)/5
	
	if n1 > media:
		print(n1)
	elif n2 > media:
		print(n2)
	elif n3 > media:
		print(n3)
	elif n4 > media:
		print(n4)
	else:
		print(5)
	
		
main()