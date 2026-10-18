# 📈 Controle de Níveis de Água

Programa de terminal em Python que recebe o volume atual de um reservatório e informa em qual nível ele se encontra (de 1 a 5), exibindo o resultado em cores.

## 📋 Sobre o projeto

A capacidade do reservatório pode ser alterada por meio da constante definida no ínico do código, as faixas terão seus valores divididos em 5 níveis conforme o volume total.

Para representar a situação vamos definir a capacidade total do reservatório em **30.000 L**. Essa capacidade será dividida em 5 faixas iguais de 6.000 litros, e cada faixa corresponde a um nível com uma cor própria no terminal.

### 📊 Níveis

| Volume (litros) | Nível | Situação | Cor |
|---|---|---|---|
| 0 – 5.999 | 1 | Muito baixo (crítico) | 🔴 Vermelho |
| 6.000 – 11.999 | 2 | Baixo | 🟡 Amarelo |
| 12.000 – 17.999 | 3 | Médio | 🟢 Verde |
| 18.000 – 23.999 | 4 | Alto | 🔵 Ciano |
| 24.000 – 30.000 | 5 | Muito alto (alerta) | 🔵 Azul |

## 💻 Exemplo de uso

```
=== Monitoramento do Reservatório ===

Informe o volume atual (0 a 30000 L): 15000
Volume: 15,000 L (50.0% da capacidade)
Nível 3 - Médio
```

A última linha é exibida em verde no terminal.

## 🛠️ Requisitos

- Python 3.6 ou superior
- Biblioteca [colorama](https://pypi.org/project/colorama/)