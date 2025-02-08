import pandas as pd
import os
#from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    print("🚀 Начинаем процесс обучения...")

    # 1. ЗАГРУЗКА ДАННЫХ
    # Если твой файл называется по-другому, поменяй путь здесь
    csv_path = 'data/transaction_dataset.csv'
    
    if not os.path.exists(csv_path):
        print(f"❌ Ошибка: Файл {csv_path} не найден!")
        return

    df = pd.read_csv(csv_path)
    print(f"✅ Данные загружены. Размер: {df.shape}")

    # 2. ПРОСТАЯ ОЧИСТКА (Pre-processing)
    # Удаляем мусорные колонки
    df = df.drop(columns=['Index', 'Unnamed: 0', 'Address'], errors='ignore')
    
    # Для простейшей модели оставим ТОЛЬКО числа (чтобы не возиться с текстом токенов)
    df = df.select_dtypes(include=['number'])
    
    # Заполняем все пропуски нулями
    df = df.fillna(0)
    
    # Разделяем на Признаки (X) и Ответы (y)
    X = df.drop(columns=['FLAG'])
    y = df['FLAG']

    # Разделяем на обучение и тест (80% на обучение, 20% на проверку)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


if __name__ == "__main__":
    main()