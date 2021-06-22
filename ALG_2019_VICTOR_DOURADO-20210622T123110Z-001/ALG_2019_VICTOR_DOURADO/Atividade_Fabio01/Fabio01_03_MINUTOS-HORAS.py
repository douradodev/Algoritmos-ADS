# Entrada 

minutos= int(input("Digite um valor em minutos: "))

# Processamento

horas= minutos//60
minutos_horas= minutos%60

# Saída

print(" {} Horas e {} Minutos".format(horas, minutos_horas))

