import os # Importa o módulo os, que permite executar comandos do sistema operacional
os.system("cls" if os.name == "nt" else "clear") # Limpa o terminal: Verifica o sistema operacional e usa "cls" ou "clear"

# Sistema de desconto progressivo

valor = float(input("Informe o valor da compra: ")) # Lê o valor digitado pelo usuário e converte para número decimal (float)

if valor < 200:         # Se o valor for menor que 200...
    percentual = 5      # ...aplica 5% de desconto
elif valor < 300:       # Se o valor for menor que 300 (e maior ou igual a 200)...
    percentual = 10     # ...aplica 10% de desconto
else:                   # Para qualquer outro caso (valor >= 300)...
    percentual = 15     # ...aplica 15% de desconto

desconto = valor * (percentual / 100)   # Calcula o valor do desconto com base no percentual definido
valor_final = valor - desconto          # Subtrai o desconto do valor original para obter o valor final

print(f"{percentual}% de desconto aplicado.\nValor do desconto: R$ {desconto:.2f}\nValor final a pagar: R$ {valor_final:.2f}")
# Exibe o percentual aplicado, o valor do desconto e o valor final, formatados com 2 casas decimais

# Fim do programa