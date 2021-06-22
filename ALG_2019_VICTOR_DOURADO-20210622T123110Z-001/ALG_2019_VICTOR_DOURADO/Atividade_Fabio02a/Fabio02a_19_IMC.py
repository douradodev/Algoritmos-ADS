def main():
	altura = float(input("Digite sua altura: "))
	peso = float(input("Digite seu peso: "))
	
	imc = peso / (altura**2)
	
	if imc < 25:
		print("IMC NORMAL")
	elif imc >= 25 and imc <= 30:
		print("PESSOA OBESA")
	else:
		print("OBESIDADE MORBIDA")
main()