import os # Importa o módulo os, que permite executar comandos do sistema operacional
os.system("cls" if os.name == "nt" else "clear") # Limpa o terminal: Verifica o sistema operacional e usa "cls" ou "clear"

# Sistema de classificação do perfil de consumo

# Solicita ao usuário o tipo de imóvel e converte a entrada para número inteiro
imovel = int(input("Informe o tipo de imóvel (1 - Comercial, 2 - Casa ou 3 - Apartamento): "))
# Solicita ao usuário o consumo mensal de água e converte a entrada para número decimal
consumo = float(input("Informe o consumo mensal de água (m³): "))

# Verifica se o tipo de imóvel informado não está entre as opções válidas (1, 2 ou 3)
if imovel not in (1, 2, 3):
    # Informa que o tipo de imóvel é inválido
    print("Tipo de imóvel inválido.")
# Verifica se o imóvel é do tipo comercial (1)
elif imovel == 1:
    # Informa que a tarifa comercial deve ser aplicada
    print("Tarifa comercial aplicada - consulte o plano corporativo.")
# Verifica se é apartamento (3) e se o consumo é menor que 10 m³
elif imovel == 3 and consumo < 10:
    # Informa que o consumo está econômico
    print("Consumo econômico - excelente controle de água!")
# Verifica se é casa ou apartamento (2 ou 3) e se o consumo é até 25 m³
elif imovel in (2, 3) and consumo <= 25:
    # Informa que o consumo está dentro do padrão residencial
    print("Consumo moderado - dentro do padrão residencial.")
# Caso nenhuma condição anterior seja atendida (consumo acima do padrão)
else:
    # Informa que o consumo está excessivo e sugere ações
    print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")

# Fim do programa