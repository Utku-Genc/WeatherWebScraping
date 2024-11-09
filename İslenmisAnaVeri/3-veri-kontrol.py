import pandas as pd

# Doldurulmuş veriyi okuma
df = pd.read_csv("İslenmisAnaVeri/tr_weather_data_filled.csv")

# Sütünlarda ki boş değer sayısını hesaplama
nan_values = df.isnull().sum()

# Toplam boş değer sayısını hesaplama
total_nan_values = nan_values.sum()

# Sütunlardaki boş değer sayısı
print("Sütunlardaki boş değer sayıları:\n", nan_values)

# Toplam boş değer sayısı
print("\nToplam boş değer sayısı:", total_nan_values)


# En son mesaj boş var-yok
if df.isnull().values.any():
    print("Veri setinde boş değerler var.")
else:
    print("Veri setinde boş değer yok.")
