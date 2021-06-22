# Entrada

minutos= int(input(" Digite o numero de minutos: "))

# Processamento

horas= minutos // 60
minutos_reais= minutos % 60
dias = horas // 24
horas_reais= horas% 24

# Saída

print("{} dias, {} horas e {} minutos ".format(dias, horas_reais, minutos_reais))