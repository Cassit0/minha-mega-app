import streamlit as st
import random
from datetime import datetime

# --- LÓGICA DE GERAÇÃO (Igual à que criamos) ---
def possui_sequencia_longa(jogo, limite=2):
    consecutivos = 1
    for i in range(len(jogo) - 1):
        if jogo[i+1] == jogo[i] + 1:
            consecutivos += 1
            if consecutivos > limite: return True
        else: consecutivos = 1
    return False

def gerar_jogo_avancado(ultimos_numeros):
    todos = list(range(1, 61))
    pares = [n for n in todos if n % 2 == 0]
    impares = [n for n in todos if n % 2 != 0]
    while True:
        jogo = random.sample(pares, 3) + random.sample(impares, 3)
        jogo.sort()
        # Filtros de Soma, Sequência e Frequência
        if (150 <= sum(jogo) <= 220) and not possui_sequencia_longa(jogo):
            frios = [n for n in jogo if n not in ultimos_numeros]
            if len(frios) >= 3:
                return jogo, sum(jogo)

# --- INTERFACE DO APP ---
st.set_page_config(page_title="Mega Estratégica", page_icon="🍀")

st.title("🍀 Mega da Virada 2025")
st.markdown("Gerador de apostas baseado em **estatística e balanço**.")

# Input para os últimos números (opcional)
st.sidebar.header("Configurações")
qtd_jogos = st.sidebar.slider("Quantos jogos gerar?", 1, 50, 5)

if st.button("GERAR APOSTAS AGORA"):
    st.subheader("Seus Números da Sorte:")
    
    # Simulando os últimos sorteios para o filtro
    ultimos = [4, 12, 32, 45, 49, 58, 1, 15, 23, 33, 42, 50]
    
    for i in range(qtd_jogos):
        jogo, soma = gerar_jogo_avancado(ultimos)
        # Exibe cada jogo de forma bonita
        st.info(f"**Jogo {i+1:02d}:** {' - '.join(map(str, jogo))}  (Soma: {soma})")
    
    st.balloons() # Efeito visual de comemoração
