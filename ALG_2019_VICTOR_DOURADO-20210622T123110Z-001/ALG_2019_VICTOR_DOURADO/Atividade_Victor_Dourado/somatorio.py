def main():
    n = int(input("Digite o numero que deseja saber se é perfeito: "))
                  
    divisor = 1
    somatorio = 0

    while divisor < n:
        if n % divisor == 0:
            print(divisor)
            somatorio = somatorio + divisor
        divisor += 1
        
    if somatorio == n:
        print("O numero é perfeito")
        

main()
        
    
