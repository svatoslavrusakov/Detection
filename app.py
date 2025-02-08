import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Crypto Fraud Detector", layout="wide")

st.title("🕵️‍♂️ Поиск крипто-мошенников")

# 1. Создаем вкладки
# Мы "распаковываем" результат функции в три переменные
tab_data, tab_analysis, tab_info = st.tabs(["📂 Данные", "📈 Анализ (EDA)", "ℹ️ О проекте"])

# --- Вкладка 1: Данные ---
with tab_data:
    st.header("Загрузка датасета")
    uploaded_file = st.file_uploader("Загрузите CSV файл с транзакциями", type="csv")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Первые 5 строк:")
        st.dataframe(df.head())
    else:
        st.info("Жду файл... Пока показываю пример:")
        # Фейковые данные для примера
        example_df = pd.DataFrame(np.random.randn(10, 5), columns=('col %d' % i for i in range(5)))
        st.dataframe(example_df)

# --- Вкладка 2: Анализ ---
with tab_analysis:
    st.header("Визуализация поведения")
    st.write("Здесь будут твои красивые графики из Seaborn и Matplotlib.")
    
    # Пример графика средствами Streamlit
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.line_chart(chart_data)
    
    st.warning("⚠️ Сюда мы добавим тот самый график с черной дырой (ERC20) позже!")

# --- Вкладка 3: Инфо ---
with tab_info:
    st.header("О проекте")
    st.markdown("""
    Это пет-проект по выявлению мошеннических транзакций в сети Ethereum.
    
    **Используемый стек:**
    *   Python 3.11
    *   Pandas & NumPy
    *   CatBoost (ML Model)
    *   Streamlit (Frontend)
    
    **Автор:** Твое Имя
    """)