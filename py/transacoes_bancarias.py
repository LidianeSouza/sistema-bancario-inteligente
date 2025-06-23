# ## 💰 Transações Bancárias

# Carrega bibliotecas principais
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Configurações iniciais
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
movimentacoes = []

menu = """\n
🔹 [d] Depositar
🔹 [s] Sacar
🔹 [e] Extrato
🔹 [g] Gráfico Movimentações Categoria
🔹 [m] Gráfico Geral das Movimentações
🔹 [a] Assistente Financeiro
🔹 [i] Sugestão de Investimentos
🔹 [q] Sair

=> """

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))
        categoria = input("Informe a categoria do depósito: ")

        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            movimentacoes.append({'Data': datetime.today(), 'Valor': valor, 'Tipo': 'Depósito', 'Categoria': categoria})
            print("✅ Depósito realizado com sucesso.")
        else:
            print("❌ Valor inválido para depósito.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$ "))
        categoria = input("Informe a categoria do saque: ")

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("❌ Saldo insuficiente.")
        elif excedeu_limite:
            print("❌ Valor excede o limite de R$ 500.00.")
        elif excedeu_saques:
            print("❌ Limite de saques diários atingido.")
        elif valor > 0:
            saldo -= valor
            extrato.append(f"Saque:    R$ {valor:.2f}")
            movimentacoes.append({'Data': datetime.today(), 'Valor': -valor, 'Tipo': 'Saque', 'Categoria': categoria})
            numero_saques += 1
            print("✅ Saque realizado com sucesso.")
        else:
            print("❌ Valor inválido para saque.")

    elif opcao == "e":
        HEADER = "\033[95m"
        OKGREEN = "\033[92m"
        FAIL = "\033[91m"
        OKBLUE = "\033[94m"
        WARNING = "\033[93m"
        ENDC = "\033[0m"
        BOLD = "\033[1m"

        print("\n" + HEADER + "="*30 + ENDC)
        print(BOLD + "       EXTRATO BANCÁRIO" + ENDC)
        print(HEADER + "="*30 + ENDC)
        if not extrato:
            print(WARNING + "Não foram realizadas movimentações." + ENDC)
        else:
            for item in extrato:
                if "Depósito" in item:
                    print(OKGREEN + item + ENDC)
                elif "Saque" in item:
                    print(FAIL + item + ENDC)
                else:
                    print(item)
        print(OKBLUE + "-"*30 + ENDC)
        print(BOLD + f"Saldo atual |  R$ {saldo:10.2f}" + ENDC)
        print(HEADER + "="*30 + ENDC)

    elif opcao == "g":
        df = pd.DataFrame(movimentacoes)

        if not df.empty:
            df_ordenado = df.drop_duplicates(subset="Categoria", keep="first")
            ordem_personalizada = df_ordenado["Categoria"].tolist()
            agrupado = df.groupby("Categoria")["Valor"].sum().reindex(ordem_personalizada)

            plt.figure(figsize=(8, 6))
            cores = ["steelblue", "tomato", "seagreen", "orchid", "goldenrod"]
            barras = plt.bar(agrupado.index, agrupado.values, color=cores[:len(agrupado)])

            plt.title("Evolução das Movimentações por Categoria")
            plt.xlabel("Categoria")
            plt.ylabel("Valor (R$)")
            plt.grid(axis="y", linestyle="--", alpha=0.5)
            for barra in barras:
                altura = barra.get_height()
                plt.text(
                    barra.get_x() + barra.get_width() / 2,
                    altura + 50 if altura >= 0 else altura - 100,
                    f"{altura:.2f}",
                    ha='center',
                    va='bottom' if altura >= 0 else 'top'
                )

            plt.tight_layout()
            plt.show()

        else:
            print("❌ Nenhuma movimentação registrada para gerar o gráfico.")

    elif opcao == "m":
        df = pd.DataFrame(movimentacoes)
        if not df.empty:
            df_pizza = df.copy()
            df_pizza["Valor"] = df_pizza["Valor"].abs()
            valores_pizza = df_pizza.groupby("Tipo")["Valor"].sum()
            valores_barra = df.groupby("Tipo")["Valor"].sum()
            cores_premium = ["#00416A", "#F00000"]
            explode = [0.1 if i == valores_pizza.idxmax() else 0 for i in valores_pizza.index]

            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

            ax1.pie(valores_pizza,
                    labels=valores_pizza.index,
                    autopct="%1.1f%%",
                    startangle=90,
                    colors=cores_premium,
                    explode=explode,
                    wedgeprops={"edgecolor": "black"})
            ax1.set_title("Distribuição das Movimentações", fontsize=14, fontweight="bold", color="#00416A")

            ax2.bar(valores_barra.index,
                    valores_barra.values,
                    color=cores_premium,
                    edgecolor="black")
            ax2.set_title("Valores por Tipo de Movimentação", fontsize=14, fontweight="bold", color="#00416A")
            ax2.set_xlabel("Tipo de Operação", fontsize=12, color="#00416A")
            ax2.set_ylabel("Valor (R$)", fontsize=12, color="#00416A")
            ax2.axhline(0, color="black", linewidth=0.8)
            ax2.grid(axis="y", linestyle="--", alpha=0.4)
            ax2.set_xticks(range(len(valores_barra.index)))
            ax2.set_xticklabels(valores_barra.index, rotation=0)

            plt.tight_layout()
            plt.show()
        else:
            print("❌ Nenhuma movimentação registrada para gerar os gráficos.")

    elif opcao == "a":
        df = pd.DataFrame(movimentacoes)

        if not df.empty:
            df["Valor"] = df["Valor"].abs()
            total_depositos = df[df["Tipo"] == "Depósito"]["Valor"].sum()
            total_saques = df[df["Tipo"] == "Saque"]["Valor"].sum()
            saldo_atual = total_depositos - total_saques

            print("\n🧠 Assistente Financeiro")
            print("-" * 30)

            if total_saques > total_depositos * 0.6:
                print("⚠️ Você está gastando mais de 60% do que deposita. Considere rever seus gastos.")
            else:
                print("✅ Ótimo! Seus gastos estão equilibrados com seus depósitos.")

            meta_economia = saldo_atual * 0.2
            print(f"🎯 Sugestão: reserve pelo menos R$ {meta_economia:.2f} como meta de economia futura.")

            rentabilidade_mensal = 0.008
            valor_investido = saldo_atual * 0.3
            rendimento_estimado = valor_investido * rentabilidade_mensal
            print(f"📈 Se investir R$ {valor_investido:.2f}, você pode ganhar cerca de R$ {rendimento_estimado:.2f} por mês.")
        else:
            print("❌ Nenhuma movimentação registrada para análise financeira.")

    elif opcao == "i":
        df = pd.DataFrame(movimentacoes)

        if not df.empty:
            saldo_atual = df["Valor"].sum()

            print("\n💡 Sugestão de Investimentos")
            print("-" * 30)

            if saldo_atual > 1000:
                print("✅ Sugerimos dividir seu saldo da seguinte forma:")
                print("- 40% em Tesouro Direto ou CDB")
                print("- 30% em Fundos Multimercado")
                print("- 30% em Ações ou ETFs")
            else:
                print("⚠️ Saldo baixo. Recomendamos focar em redução de despesas.")
        else:
            print("❌ Nenhuma movimentação registrada para análise financeira.")

    elif opcao == "q":
        print("👋 Saindo do sistema.")
        break

    else:
        print("❌ Opção inválida.")