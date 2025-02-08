import pandas as pd
import os
#from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    print("🚀 Начинаем процесс обучения...")

    # 1. ЗАГРУЗКА ДАННЫХ
    csv_path = 'data/transaction_dataset.csv'
    
    if not os.path.exists(csv_path):
        print(f"❌ Ошибка: Файл {csv_path} не найден!")
        return

    df = pd.read_csv(csv_path)
    print(f"✅ Данные загружены. Размер: {df.shape}")


if __name__ == "__main__":
    main()