def e_primo():
    n = int(input("Digite um numero: "))
    i = 1
    primo = 0
    
    while i <= n:
        if n % i == 0:
            primo += 1
        i += 1
    
    if primo == 2:
        print("{} é primo".format(n))
    else:
        print("{} não é primo".format(n))


e_primo()
        
        
    
