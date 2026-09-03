# Autor do projeto: Juan Santos
print("CALCULADORA DE CONSUMO ELÉTRICO")
print() # linha em branco

# Entrada de dados
aparelho = input("Qual é o seu aparelho? ")
potencia = int(input("Qual a potência dele em watts (W)? "))
horasDia = float(input("Quantas horas por dia você o utiliza? "))
print() # linha em branco

# Processamento
consumoMensal = (potencia * horasDia * 30) / 1000
tarifa = float(0.78) # valor da tarifa em reais
custoMensal = consumoMensal * tarifa

# Saída de dados
print(f"Aparelho: {aparelho} \nConsumo estimado: {consumoMensal:.0f} kWh/mês \nCusto mensal estimado: R$ {custoMensal:.2f}")
