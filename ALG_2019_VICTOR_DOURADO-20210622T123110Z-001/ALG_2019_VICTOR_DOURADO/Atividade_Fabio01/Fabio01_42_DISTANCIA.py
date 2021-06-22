# Entrada

x1= int(input("Digite o valor de um ponto qualquer: "))
y1= int(input("Digite o valor de um ponto qualquer: "))
x2= int(input("Digite o valor de um ponto qualquer: "))
y2= int(input("Digite o valor de um ponto qualquer: "))


# Processamento

d= ((x2 - x1)**2 + (y2 - y1)**2)**1/2

# Saída

print("A distancia entre os pontos é {}".format(d))