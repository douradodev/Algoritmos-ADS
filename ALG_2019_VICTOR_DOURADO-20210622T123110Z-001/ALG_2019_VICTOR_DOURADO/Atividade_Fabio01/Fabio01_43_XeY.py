# Entrada

a = int(input(" Digite um valor: "))
b = int(input(" Digite um valor: "))
c = int(input(" Digite um valor: "))
d = int(input(" Digite um valor: "))
e = int(input(" Digite um valor: "))
f = int(input(" Digite um valor: "))

# Processamento

x = (c*e - b*f) / (a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)


# Saída

print(" X = {} e Y = {}".format(x,y))