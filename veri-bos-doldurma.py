import pandas as pd

df = pd.read_csv("tr_weather_data.csv")

# Sütünlarda ki boş değer sayısını hesaplama
nan_values = df.isnull().sum()

# Toplam boş değer sayısını hesaplama
total_nan_values = nan_values.sum()

# Sütunlardaki boş değer sayısı
print("Sütunlardaki boş değer sayıları:\n", nan_values)

# Toplam boş değer sayısı
print("\nToplam boş değer sayısı:", total_nan_values)

# Boş değerleri doldurma
def fill_na_with_adjacent(row, col):
    if pd.isna(row[col]):
        # Eğer önceki sütun boş değilse, önceki sütunun değeri ile doldur
        if col - 1 >= 0 and not pd.isna(row.iloc[col - 1]):
            return row.iloc[col - 1]
        #  Sonraki sütun
        elif col + 1 < len(row) and not pd.isna(row.iloc[col + 1]):
            return row.iloc[col + 1]
    return row[col]

# Boş değerleri için sütunlar gezme
for col in df.columns:
    df[col] = df.apply(lambda row: fill_na_with_adjacent(row, df.columns.get_loc(col)), axis=1)

df.to_csv("tr_weather_data_filled.csv", index=False)

print("\nVeri düzenleme işlemi tamamlandı ve 'tr_weather_data_filled.csv' olarak kaydedildi.")
