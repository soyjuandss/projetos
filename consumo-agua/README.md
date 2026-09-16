# 💧 Sistema de Classificação do Consumo de Água

Script simples em Python que classifica o perfil de consumo mensal de água de um imóvel com base no seu tipo (comercial, casa ou apartamento).

## 📋 Como funciona

O programa solicita duas informações ao usuário:


1. **Tipo de imóvel (comercial, casa ou apartamento)**
2. **Consumo mensal de água (em m³)**

Com base nesses dados, o script exibe uma mensagem classificando o consumo:

| Condição | Resultado |
|---|---|
| Imóvel comercial | 🏪 Tarifa comercial aplicada — consulte o plano corporativo |
| Apartamento e consumo < 10 m³ | 🟢 Consumo econômico — excelente controle de água |
| Casa ou apartamento e consumo ≤ 25 m³ | 🟡 Consumo moderado — dentro do padrão residencial |
| Casa ou apartamento e consumo > 25 m³ | 🔴 Consumo excessivo — adote medidas de economia e verifique vazamentos |

## ▶️ Como executar

Pré-requisito: ter o Python 3 instalado.

```
python classificacao_consumo.py
```

## 💻 Exemplo de uso

```
Informe o tipo de imóvel (1 - Comercial, 2 - Casa ou 3 - Apartamento): 3
Informe o consumo mensal de água (m³): 8
Consumo econômico - excelente controle de água!
```
