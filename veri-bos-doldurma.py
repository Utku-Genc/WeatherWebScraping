import pandas as pd

# 'weather_data_tr.csv' dosyasını oku
df = pd.read_csv("tr_weather_data.csv")

# Sütunlardaki boş (NaN) değer sayısını al
nan_values = df.isnull().sum()

# Toplam boş değer sayısını al
total_nan_values = nan_values.sum()

# Sütunlardaki boş değer sayısını yazdır
print("Sütunlardaki boş değer sayıları:\n", nan_values)

# Toplam boş değer sayısını yazdır
print("\nToplam boş değer sayısı:", total_nan_values)

# Boş değer içeren satırları yazdır (Wind sütununda)
wind_null_rows = df[df["Wind (Rüzgar Yönü)"].isnull()]

# Eğer boş değer içeren satır varsa yazdır
if not wind_null_rows.empty:
    print("\nBoş Wind (Rüzgar Yönü) içeren satırlar:\n", wind_null_rows)
else:
    print("\nWind (Rüzgar Yönü) sütununda boş değer yok.")

# Boş değerleri önceki veya sonraki sütunlardan doldurma
def fill_na_with_adjacent(row, col):
    if pd.isna(row[col]):
        # Eğer önceki sütun boş değilse, önceki sütunun değeri ile doldur
        if col - 1 >= 0 and not pd.isna(row.iloc[col - 1]):
            return row.iloc[col - 1]
        # Eğer sonraki sütun boş değilse, sonraki sütunun değeri ile doldur
        elif col + 1 < len(row) and not pd.isna(row.iloc[col + 1]):
            return row.iloc[col + 1]
    return row[col]

# Boş değerleri doldurmak için sütunlar üzerinde iterasyon
for col in df.columns:
    df[col] = df.apply(lambda row: fill_na_with_adjacent(row, df.columns.get_loc(col)), axis=1)

# Veriyi düzenledikten sonra CSV dosyasına kaydet
df.to_csv("tr_weather_data_filled.csv", index=False)

print("\nVeri düzenleme işlemi tamamlandı ve 'tr_weather_data_filled.csv' olarak kaydedildi.")
