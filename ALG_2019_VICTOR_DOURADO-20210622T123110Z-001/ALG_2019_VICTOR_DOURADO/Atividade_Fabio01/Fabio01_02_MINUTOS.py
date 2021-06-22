# Entrada

horas= int(input("Digite as horas: "))
minutos= int(input("Digite os minutos: "))

#Processamento

minutos_hora = horas*60
minutos_reais= minutos_hora + minutos

#Saída

print("Os minutos totais são {} min.".format(minutos_reais))