# Entrada

segundos= int(input("Digite o numero de segundos: "))

# Processamento
minutos= segundos // 60
horas= minutos // 60
segundo_reais= segundos % 60
minuto_reais= minutos% 60

# Saída

print(" {} horas, {} minutos e {} segundos".format(horas,minuto_reais,segundo_reais))