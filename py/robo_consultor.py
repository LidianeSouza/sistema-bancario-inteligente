# ## 🤖 Robô Consultor em Ação

import os
import sys
import time

# Supondo que você tenha esta variável global
try:
    saldo
except NameError:
    saldo = 1000  # valor padrão caso esteja testando isoladamente

# Lista de movimentações usada pelo sistema
try:
    movimentacoes
except NameError:
    movimentacoes = []

# Função para exibir imagem compatível com notebook e .py
def exibir_imagem_compativel(caminho_imagem):
    try:
        if "ipykernel" in sys.modules:
            from IPython.display import display as notebook_display, Image as NotebookImage
            notebook_display(NotebookImage(filename=caminho_imagem))
        else:
            from PIL import Image as PILImage
            imagem = PILImage.open(caminho_imagem)
            imagem.show()
    except Exception as e:
        print(f"⚠️ Não foi possível exibir a imagem: {e}")

# Caminho da imagem (relativo à pasta raiz)
caminho_imagem = os.path.join("..", "imagens", "robozinho_consultor.png") if "ipykernel" in sys.modules else os.path.join("imagens", "robozinho_consultor.png")

# Interação com usuário
input("Pressione ENTER para receber uma sugestão do nosso 🤖 Robô Consultor")
aceitou = input("Você gostaria de investir R$ 200,00? (s/n): ").strip().lower()

if aceitou == 's':
    if saldo >= 200:
        print("🤖💬 Calculando o melhor investimento...")
        time.sleep(1.2)
        print("🤖💬 Analisando mercado 📈...")
        time.sleep(1.2)
        print("🤖💬 Preparando a aplicação 🏦...")
        time.sleep(1.2)
        print("🤖✅ Investimento realizado com sucesso! 💰")

        exibir_imagem_compativel(caminho_imagem)

        movimentacoes.append({
            "Data": datetime.today(),
            "Valor": -200,
            "Tipo": "Saque",
            "Categoria": "Investimento"
        })

        df = pd.DataFrame(movimentacoes)
        df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce")
        df = df.dropna(subset=["Valor"])
        saldo = df["Valor"].sum()

        print(f"💰 Novo saldo disponível: R$ {saldo:.2f}")
    else:
        print("❌ Saldo insuficiente para realizar o investimento.")
else:
    print(f"✅ Seu saldo continua o mesmo: R$ {saldo:.2f}")