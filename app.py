import streamlit as st
import random
import pandas as pd
from datetime import datetime

# --- CONFIGURAÇÃO: É AQUI QUE ATUALIZAS OS NÚMEROS ---
# Substitui estes números pelos sorteios mais recentes quando quiseres
ultimos_5_sorteios = [
    [4, 11, 23, 34, 44, 58], # Concurso 2809
    [5, 12, 25, 28, 36, 57], # Concurso 2808
    [1, 4, 10, 22, 53, 54],  # Concurso 2807
    [18, 20, 30, 32, 33, 50],
    [2, 12, 28, 36, 45, 59]
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
    # Cria uma lista de todos os números que saíram recentemente
    numeros_viciados = set([n for sorteio in ultimos_5_sorteios for n in sorteio])
    todos = list(range(1, 61))
    pares = [n for n in todos if n % 2 == 0]
    impares = [n for n in todos if n % 2 != 0]

    while True:
        # Tenta equilibrar 3 pares e 3 ímpares
        jogo = random.sample(pares, 3) + random.sample(impares, 3)
        jogo.sort()
        
        # Filtros: Soma ideal, Sem sequências longas e números novos
        if (150 <= sum(jogo) <= 220) and \
           not possui_sequencia_longa(jogo) and \
           len([n for n in jogo if n not in numeros_viciados]) >= 3:
            return jogo, sum(jogo)

# --- INTERFACE STREAMLIT ---
st.set_page_config(page_title="Mega da Virada Estratégica", page_icon="🍀")

st.title("🍀 Gerador Mega da Virada")
st.markdown("Este app gera jogos equilibrando **Pares/Ímpares**, **Somas** e evitando números muito repetidos.")

# Menu lateral
st.sidebar.header("Configurações")
qtd = st.sidebar.slider("Quantos jogos queres?", 1, 50, 5)

if st.button("GERAR APOSTAS AGORA"):
    jogos_lista = []
    for i in range(qtd):
        num, soma = gerar_jogo_avancado()
        jogos_lista.append({"Jogo": i+1, "Números": " - ".join(map(str, num)), "Soma": soma})
    
    # Exibe os resultados numa tabela bonita
    df = pd.DataFrame(jogos_lista)
    st.table(df)
    
    st.success(f"Foram gerados {qtd} jogos com sucesso!")
    st.balloons()

st.info("Dica: Atualiza os 'ultimos_5_sorteios' no GitHub para manter o app calibrado!")
st.info("Se deixar de ser diversão, PARE!!")
