# ⚡ Calculadora de Consumo Elétrico

> 💡 Descubra quanto seus aparelhos elétricos consomem — e quanto isso custa no bolso! 💰

Este projeto em **Python** consiste em estimar quanto um determinado aparelho gasta de energia elétrica por mês. O programa solicita que o usuário informe:

- 🔌 **O tipo de aparelho**
- ⚡ **A potência do aparelho em watts (W)**
- ⏱️ **O tempo médio do uso diário em horas**

---

### ⚙️ Como funciona o cálculo

A calculadora entrega o consumo estimado de energia do aparelho em **quilowatts-hora (kWh)** no mês e seu **custo total estimado em reais**, de acordo com os dados que o usuário informar.

O programa solicita:

| 🧾 Dado | 📥 Descrição |
|---------|--------------|
| 🔌 Tipo de aparelho | Nome/identificação do aparelho |
| ⚡ Potência (W) | Potência do aparelho em watts |
| ⏱️ Uso diário (h) | Tempo médio de uso por dia, em horas |

---

### 🧮 Consumo mensal em kWh

O cálculo do consumo mensal em kWh é a potência do aparelho em watts (W) × tempo médio do uso diário em horas × 30 (dias no mês), dividido por 1000 para converter:

```
consumo mensal de kWh = potência (W) * uso diário (h) * 30 / 1000
```

---

### 💵 Custo total estimado

Já o cálculo do custo total estimado é realizado com o resultado do consumo mensal de kWh × a tarifa cobrada pela concessionária de energia por kWh:

```
custo total estimado = consumo mensal de kWh * tarifa por kWh
```

> ⚠️ **Obs:** Neste programa o valor está fixado em **R$ 0,78 por kWh** (valor médio cobrado pela EDP São Paulo), mas a tarifa varia de região para região. Para que o resultado fique mais próximo da sua realidade, você pode alterar o valor da tarifa diretamente no código-fonte. 🛠️

---

### 🚀 Como executar

```terminal
python calculadora.py
```