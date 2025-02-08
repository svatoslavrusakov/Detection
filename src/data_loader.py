import pandas as pd
import os

class DataLoader:
    """
    Класс для загрузки данных. 
    """
    _instance = None
    _data = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataLoader, cls).__new__(cls)
        return cls._instance

    def load_data(self, file_path="data/transaction_dataset.csv"):
        if self._data is None:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Файл не найден по пути {file_path}")
            
            # Читаем CSV. В этом датасете обычно есть лишняя колонка с индексами, уберем её
            self._data = pd.read_csv(file_path, index_col=0)
            print(f"--- Данные загружены: {self._data.shape[0]} строк, {self._data.shape[1]} колонок ---")
        return self._data

if __name__ == "__main__":
    # Короткий тест: проверим, что всё работает
    loader = DataLoader()
    df = loader.load_data()
    print(df.head())