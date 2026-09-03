# ⚡ Calculadora de Consumo Elétrico

> 💡 Descubra quanto seus aparelhos elétricos consomem — e quanto isso custa no bolso! 💰

Este projeto em **Python** consiste em estimar quanto um determinado aparelho gasta de energia elétrica por mês.

---

### ⚙️ Como o cálculo funciona

O programa calcula o **consumo mensal estimado do aparelho em quilowatts-hora (kWh)** no mês e seu **custo mensal total em reais**.

Para isso usuário precisa informar:

| 🧾 Dado | 📥 Descrição |
|---------|--------------|
| 🔌 Tipo de aparelho | Nome/identificação do aparelho |
| ⚡ Potência (W) | Potência do aparelho em watts |
| ⏱️ Uso diário (h) | Tempo médio de uso por dia, em horas |

---

### 🧮 Consumo mensal

O cálculo do consumo mensal é a potência do aparelho em watts (W) × tempo médio do uso diário, em horas × 30, dividido por 1000:

```
consumo mensal = potência (W) * uso diário (h) * 30 / 1000
```

---

### 💵 Custo mensal total

Já o cálculo do custo total estimado é realizado com o resultado do consumo mensal × a tarifa cobrada por kWh:

```
custo total estimado = consumo mensal * tarifa
```

> ⚠️ **Obs:** Neste programa o valor da tarifa está fixado em **R$ 0,78 por kWh** (valor médio cobrado pela EDP São Paulo), mas ela tarifa varia de região para região. Para que o resultado fique mais próximo da sua realidade, você pode alterar o valor da tarifa diretamente no código-fonte. 🛠️

---

### 🚀 Como executar

```
python calculadora.py
```
