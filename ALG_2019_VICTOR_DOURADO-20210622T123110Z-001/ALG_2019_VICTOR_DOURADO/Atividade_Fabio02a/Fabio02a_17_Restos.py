def main():
	n1= int(input("Digite um valor: "))
	n2= int(input("Digite outro valor: "))
	
	if n1 % n2 == 1 :
		print(n1 + n2 + (n1 % n2))
	elif n1 % n2 == 2:
		
		if n1 % 2 == 0:
			print("{} é par".format(n1))
		else:
			print("{} é impar".format(n1))
		if n2 % 2 == 0:
			print("{} é par".format(n2))
		else:
			print("{} é impar".format(n2))
			
	elif n1 % n2 == 3:
		print((n1+n2)* n1)
	elif n1 % n2 == 4:
		print((n1 + n2) / n2)
	else:
		print(n1**2, n2**2)
		
		
		
		
main()