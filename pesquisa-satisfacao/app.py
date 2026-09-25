import os # Importa o módulo os, que permite executar comandos do sistema operacional
os.system("cls" if os.name == "nt" else "clear") # Limpa o terminal: Verifica o sistema operacional e usa "cls" ou "clear"

# Pesquisa de satisfação ao cliente

excelente = 0   # Contador para respostas "EXCELENTE"
bom = 0         # Contador para respostas "BOM"
ruim = 0        # Contador para respostas "RUIM"

for entrevistados in range (1, 11): # Laço que repete a pesquisa para um determinado número de entrevistados

    print("PESQUISA DE SATISFAÇÃO")
    print("=" * 35) # Exibe uma linha separadora
    
    nome = input("Digite seu nome: ")           # Solicita e armazena o nome do entrevistado
    idade = int(input("Informe sua idade: "))   # Solicita a idade e converte para número inteiro
    
    # Solicita a avaliação e converte para número inteiro
    avaliacao = int(input("Avalie o seu atendimento\n1- EXCELENTE, 2- BOM ou 3- RUIM: "))
    
    match avaliacao:        # Estrutura de decisão que compara o valor de "avaliacao"
        case 1:             # Se a avaliação for 1
            excelente += 1  # Incrementa o contador de "excelente" em 1
        case 2:             # Se a avaliação for 2
            bom += 1        # Incrementa o contador de "bom" em 1
        case 3:             # Se a avaliação for 3
            ruim += 1       # Incrementa o contador de "ruim" em 1

    print() # Imprime uma linha em branco para separar as respostas

print("RESUMO DAS RESPOSTAS")
print("=" * 35) # Exibe uma linha separadora
print(f"EXCELENTE: {excelente} | BOM: {bom} | RUIM: {ruim}") # Exibe o total de cada tipo de avaliação

# Fim do programa