import pandas as pd

# Doldurulmuş veriyi okuma
df = pd.read_csv("tr_weather_data_filled.csv")

# Sütunlardaki boş (NaN) değer sayısını al
nan_values = df.isnull().sum()

# Toplam boş değer sayısını al
total_nan_values = nan_values.sum()

# Sütunlardaki boş değer sayısını yazdır
print("Sütunlardaki boş değer sayıları:\n", nan_values)

# Toplam boş değer sayısını yazdır
print("\nToplam boş değer sayısı:", total_nan_values)

# Eğer tüm DataFrame'deki boş değer olup olmadığını kontrol etmek isterseniz
if df.isnull().values.any():
    print("Veri setinde boş değerler var.")
else:
    print("Veri setinde boş değer yok.")
