import os # Importa o módulo os, que permite executar comandos do sistema operacional
os.system("cls" if os.name == "nt" else "clear") # Limpa o terminal: Verifica o sistema operacional e usa "cls" ou "clear"

# Importa do colorama: Fore (cores do texto) e Style (estilos, como o reset)
from colorama import Fore, Style

# Constante com a capacidade total do reservatório em litros.
CAPACIDADE_RESERVATORIO = 30_000

# Lista com as mensagens de cada nível.
NIVEIS = [  # O índice 0 corresponde ao nível 1, o índice 1 ao nível 2 e assim por diante
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED       # Muito baixo: vermelho
    elif nivel == 2:
        return Fore.YELLOW    # Baixo: amarelo
    elif nivel == 3:
        return Fore.GREEN     # Médio: verde
    elif nivel == 4:
        return Fore.CYAN      # Alto: ciano
    elif nivel == 5:
        return Fore.BLUE      # Muito alto: azul

def definir_situacao(nivel):
    cor = definir_cor(nivel)            # Descobre a cor do nível
    mensagem = NIVEIS[nivel - 1]        # Pega o texto (nível 1 = índice 0)
    print(f"{cor}{mensagem}{Style.RESET_ALL}")  # Imprime colorido e reseta a cor

'''A função definir_situacao estava imprimindo a lista inteira de NIVEIS,
foi perguntado a IA e ela corrigiu mensagem = NIVEIS para mensagem = NIVEIS[nivel -1],
imprimindo assim só a mensagem do nível correspondente'''

def calcular_nivel(volume):
    faixa = CAPACIDADE_RESERVATORIO / len(NIVEIS)  # Tamanho de cada faixa do nível
    nivel = int(volume // faixa) + 1               # Divisão inteira + 1 (para começar em 1, não em 0)
    return min(nivel, len(NIVEIS))                 # Limita a 5 (caso o reservatório esteja 100% cheio)

'''A função calcular_nivel não estava retornando nada,
foi perguntado a IA e ela sugeriu a divisão inteira + 1 e corregiu o return'''

def main():
    print("=== Monitoramento do Reservatório ===\n")

    # Pede o volume ao usuário e converte o texto em número decimal
    volume = float(input(f"Informe o volume atual (0 a {CAPACIDADE_RESERVATORIO} L): "))
    
    nivel = calcular_nivel(volume)                          # Calcula o nível (1 a 5)
    percentual = volume / CAPACIDADE_RESERVATORIO * 100     # Calcula a porcentagem de enchimento

    print(f"Volume: {volume:,.0f} L ({percentual:.1f}% da capacidade)")
    definir_situacao(nivel)  # Mostra o nível, colorido

main()