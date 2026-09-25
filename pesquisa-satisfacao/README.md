# Pesquisa de Satisfação ao Cliente

Script simples em Python para coletar e resumir avaliações de atendimento ao cliente via terminal.

## 📋 Como funciona

O programa solicita, para cada entrevistado o nome, a idade e uma avaliação do atendimento recebido. Ao final da coleta, exibe um resumo com a quantidade de respostas em cada categoria: **Excelente**, **Bom** e **Ruim**.

## ⚙️ Funcionamento

1. O script executa um laço que percorre um número fixo de entrevistados (atualmente definido pelo `range(1, 51)`).

2. Para cada entrevistado, o programa solicita: **Nome**, **Idade** e **Avaliação do atendimento**, sendo:

    - `1` → Excelente
    - `2` → Bom
    - `3` → Ruim

3. Usa a estrutura `match/case` para contabilizar a avaliação escolhida.

4. Ao término, imprime o resumo com o total de respostas em cada categoria.

## ▶️ Como executar

### Pré-requisitos

- Python 3.10 ou superior (necessário para suporte a estrutura `match/case`)

## 💻 Exemplo de uso

```
PESQUISA DE SATISFAÇÃO
===================================
Digite seu nome: Juan
Informe sua idade: 28
Avalie o seu atendimento
1- EXCELENTE, 2- BOM ou 3- RUIM: 1

PESQUISA DE SATISFAÇÃO
===================================
Digite seu nome: Maria
Informe sua idade: 32
Avalie o seu atendimento
1- EXCELENTE, 2- BOM ou 3- RUIM: 2

RESUMO DAS RESPOSTAS
===================================
EXCELENTE: 1 | BOM: 1 | RUIM: 0
```