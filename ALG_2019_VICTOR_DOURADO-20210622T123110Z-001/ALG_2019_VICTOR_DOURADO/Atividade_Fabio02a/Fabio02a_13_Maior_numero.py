def main():
	n1, n2, n3, n4, n5 = input("Digite 5 valores separados por espaço: ").split()
	if n1 > n2 and n1 > n3 and n1 > n4 and n1> n5:
		print(n1)
	elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
		print(n2)
	elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
		print(n3)
	elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
		print(n4)
	else:
		print(n5)
	
		
main()