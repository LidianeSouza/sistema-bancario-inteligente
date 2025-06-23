# ## 🚨 Alertas Financeiros Inteligentes

# Criando DataFrame com as movimentações
gastos = pd.DataFrame(movimentacoes)

# Filtrando apenas os saques do mês atual
gasto_mensal = gastos[(gastos["Data"].dt.month == datetime.today().month) & (gastos["Tipo"] == "Saque")]["Valor"].sum()

# Definindo limite de gastos
limite_gastos = 3000

if gasto_mensal > limite_gastos:
    print(f"🚨 ALERTA: Seus gastos do mês já somam R$ {gasto_mensal:.2f} e ultrapassaram o limite de R$ {limite_gastos}.")
else:
    print(f"✅ Gastos do mês sob controle: R$ {gasto_mensal:.2f}")