# 💰 Sistema Bancário com Robô Consultor Inteligente

Este projeto apresenta um **sistema bancário interativo** desenvolvido em **Python**, inspirado no desafio da [DIO (Digital Innovation One)](https://www.dio.me/) do bootcamp de **Backend com Python do Santander**. 

O objetivo é criar uma aplicação simples que permite aos usuários realizar operações bancárias essenciais, como **depósitos, saques e consulta de extrato**, de forma intuitiva e eficiente.  

Além da proposta inicial, este projeto foi ampliado com recursos avançados voltados para **educação financeira** e **inteligência de dados**, oferecendo uma experiência enriquecedora. Destacam-se funcionalidades como um **Robô Consultor Inteligente**, gráficos interativos e categorização de transações, permitindo ao usuário uma melhor gestão e tomada de decisão financeira.  

## 🚀 Melhorias implementadas e Funcionalidades

| Funcionalidade                      | Descrição | 📄 Código Executado | 🎞️ Resultado |
|------------------------------------|-----------|----------------------|--------------|
| 🤖 **Robô Consultor Inteligente**      | Um assistente virtual que aparece na tela apenas quando o usuário aceita investir. Ele simula a aplicação e exibe uma imagem personalizada, tornando a experiência mais interativa e educativa. | [Robô Consultor](py/robo_consultor.py) | <a href="imagens/robozinho_em_acao.gif"><img src="imagens/robozinho_em_acao.gif" width="150"/></a> |
| 📊 **Gráficos Interativos e Animados** | Gráficos de pizza e barras com animações temporais por mês e categoria, facilitando a análise de tendências e padrões de gastos. | [Transações - Opção [m]](py/transacoes_bancarias.py) | <a href="imagens/grafico_movimentacoes.gif"><img src="imagens/grafico_movimentacoes.gif" width="150"/></a> |
| 🏷️ **Classificação por Categoria**     | O usuário pode classificar transações como alimentação, transporte, lazer, entre outras, o que auxilia no acompanhamento dos gastos. | [Transações - Opção [g]](py/transacoes_bancarias.py) | <a href="imagens/grafico_categoria.gif"><img src="imagens/grafico_categoria.gif" width="150"/></a> |
| 🧠 **Assistente Financeiro**           | Oferece alertas sobre hábitos de consumo, sugestões de economia e simula potenciais ganhos com investimentos baseados no saldo atual. | [Transações - Opção [a]](py/transacoes_bancarias.py) | <a href="imagens/assistente_financeiro.gif"><img src="imagens/assistente_financeiro.gif" width="150"/></a> |
| 💡 **Sugestões de Investimento**      | Caso o saldo ultrapasse determinado valor, o sistema sugere uma divisão inteligente entre Tesouro, Fundos e Ações. | [Transações - Opção [i]](py/transacoes_bancarias.py) | <a href="imagens/sugestoes_investimentos.gif"><img src="imagens/sugestoes_investimentos.gif" width="150"/></a> |
| 🚨 **Alertas Financeiros Inteligentes**| O sistema emite avisos automáticos quando os gastos ultrapassam um limite mensal predefinido. | [Alertas Inteligentes](py/alertas_inteligentes.py) | <a href="imagens/alertas_inteligentes.gif"><img src="imagens/alertas_inteligentes.gif" width="150"/></a> |
| ✅ **Depósitos, Saques e Extrato** | Funções básicas do sistema bancário com validações, limite de saques e extrato com saldo atualizado em tempo real. | [Transações Bancárias](py/transacoes_bancarias.py) | <a href="imagens/transacoes_basicas1.png"><img src="imagens/transacoes_basicas1.png" width="150"/></a> <a href="imagens/transacoes_basicas2.png"><img src="imagens/transacoes_basicas2.png" width="150"/></a><br><a href="imagens/transacoes_basicas3.png"><img src="imagens/transacoes_basicas3.png" width="150"/></a> <a href="imagens/transacoes_basicas4.png"><img src="imagens/transacoes_basicas4.png" width="150"/></a> |


## 📌 Observações
- Sistema simulado para um único usuário.
- Movimentações armazenadas apenas em memória durante a execução.
- Foco educacional: decisões financeiras reais devem ser feitas com auxílio profissional.

## 🖼️ Demonstração visual

<p align="center">
  <img src="imagens/robozinho_consultor.png" alt="Robô Consultor Inteligente" width="250" />
</p>

## 🎬 Demonstração em GIF

<p align="center">
  <img src="robozinho_demo.gif" alt="Demonstração do Robô Consultor" width="250" />
</p>

## 🛠️ Tecnologias Utilizadas

- Python 3
- Jupyter Notebook
- Pandas
- NumPy
- Plotly
- ChatGPT — Assistente de IA que auxiliou na estruturação do projeto, dúvidas e sugestões.
- GitHub Copilot — Assistente de codificação que acelerou a implementação das funcionalidades.

## ▶️ Como Usar

1. Clone este repositório:

```bash
git clone https://github.com/LidianeSouza/sistema-bancario-inteligente.git
```

2. Navegue até o diretório e abra o notebook:

```bash
cd sistema-bancario-inteligente
jupyter notebook sistema_bancario_inteligente.ipynb
```

3. Execute célula por célula para interagir com o sistema.


📂 Estrutura do Projeto

```bash
📁 sistema-bancario-inteligente/
├── 📁 notebook/
│   └── sistema_bancario_inteligente.ipynb   # Notebook principal
├── 📁 imagens/
│   ├── robozinho_consultor.png              # Imagem do assistente virtual
│   └── robozinho_demo.gif                   # GIF do Robô Consultor em ação
├── 📁 py/
│   └── funcoes_auxiliares.py                # (Exemplo) Arquivo com funções Python
├── README.md                                # Documentação do projeto
```

## 📧 Contato

Desenvolvido por **Lidiane Souza**  
🔗 LinkedIn: [linkedin.com/in/lidiane-souza88](https://linkedin.com/in/lidiane-souza88)





