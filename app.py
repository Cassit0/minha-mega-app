import streamlit as st
import random
import pandas as pd

# --- CONFIGURAÇÃO ATUALIZADA (20/12/2025) ---
ultimos_5_sorteios = [
    [16, 17, 18, 40, 45, 54], # Concurso 2954
    [1, 12, 33, 41, 45, 59], # Concurso 2953
    [18, 12, 19, 41, 15, 29], # Concurso 2952
    [11, 22, 34, 44, 51, 16], # Concurso 2951
    [4, 15, 23, 33, 42, 50]   # Concurso 2950
]

def possui_sequencia_longa(jogo, limite=2):
    consecutivos = 1
    for i in range(len(jogo) - 1):
        if jogo[i+1] == jogo[i] + 1:
            consecutivos += 1
            if consecutivos > limite: return True
        else: consecutivos = 1
    return False

def gerar_jogo_avancado():
    numeros_viciados = set([n for sorteio in ultimos_5_sorteios for n in sorteio])
    todos = list(range(1, 61))
    pares = [n for n in todos if n % 2 == 0]
    impares = [n for n in todos if n % 2 != 0]
    while True:
        jogo = random.sample(pares, 3) + random.sample(impares, 3)
        jogo.sort()
        if (150 <= sum(jogo) <= 220) and not possui_sequencia_longa(jogo) and \
           len([n for n in jogo if n not in numeros_viciados]) >= 3:
            return jogo, sum(jogo)

# --- INTERFACE ---
st.set_page_config(page_title="Mega da Virada 2025", page_icon="🍀")

# Estilo CSS para as bolinhas e o painel de preço
st.markdown("""
    <style>
    .bola {
        display: inline-block;
        width: 38px;
        height: 38px;
        line-height: 38px;
        border-radius: 50%;
        background-color: #209869;
        color: white;
        text-align: center;
        font-weight: bold;
        margin: 4px;
        font-size: 16px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }
    .container-jogo {
        padding: 10px;
        border-bottom: 1px solid #eee;
    }
    .preco-total {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #209869;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🍀 Mega da Virada 2025")

# Sidebar
st.sidebar.header("Configurações")
qtd = st.sidebar.slider("Quantos jogos gerar?", 1, 100, 5)
preco_unidade = 6.00
total_pago = qtd * preco_unidade

# Exibe o valor total logo no topo para facilitar
st.markdown(f"""
    <div class="preco-total">
        <span style="font-size: 20px; color: #209869;><strong>Resumo do Investimento:</strong></span><br>
        Quantidade: {qtd} jogos<br>
        <span style="font-size: 20px; color: #209869;"><strong>Total a pagar: R$ {total_pago:,.2f}</strong></span>
    </div>
""", unsafe_allow_html=True)

if st.button("GERAR APOSTAS AGORA"):
    for i in range(qtd):
        jogo, soma = gerar_jogo_avancado()
        bolinhas_html = "".join([f'<div class="bola">{n:02d}</div>' for n in jogo])
        
        st.markdown(f"""
            <div class="container-jogo">
                <strong>Jogo {i+1}</strong> (Soma: {soma})<br>
                {bolinhas_html}
            </div>
        """, unsafe_allow_html=True)
    
    st.balloons()

st.info("Regras aplicadas: Balanço 3P/3Í, Soma entre 150-220 e Filtro de repetidos.")
