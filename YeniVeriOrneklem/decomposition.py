import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# CSV dosyasını yükleme (dosya yolunu değiştirin)
df = pd.read_csv("tr_weather_data_filled_new.csv")

# 'Tarih' sütununu datetime formatına çevirme
df['Tarih'] = pd.to_datetime(df['Tarih'])

# Zaman serisi indeksini ayarlama
df.set_index('Tarih', inplace=True)

# Sıcaklık sütunundaki birimleri kaldırarak sayısal değere çevirme
# °C birimini kaldırıyoruz ve sayıya dönüştürüyoruz
df['Sıcaklık'] = df['Sıcaklık'].replace({'°C': '', '°': ''}, regex=True)  # °C birimini kaldırıyoruz
df['Sıcaklık'] = pd.to_numeric(df['Sıcaklık'], errors='coerce')  # Sayıya dönüştürme

# Zaman serisi dekompozisyonu (periyot=24 saatlik veriler için)
decomposition = seasonal_decompose(df['Sıcaklık'], model='additive', period=24)  # 24 saatlik bir döngü kullanıyoruz

# Dekompoze edilmiş bileşenleri görselleştirme
plt.figure(figsize=(10, 8))

# Orijinal veri
plt.subplot(411)
plt.plot(df['Sıcaklık'], label='Orijinal Veri')
plt.legend(loc='best')
plt.title('Orijinal Veri')

# Trend bileşeni
plt.subplot(412)
plt.plot(decomposition.trend, label='Trend Bileşeni')
plt.legend(loc='best')
plt.title('Trend Bileşeni')

# Mevsimsellik bileşeni
plt.subplot(413)
plt.plot(decomposition.seasonal, label='Mevsimsellik Bileşeni')
plt.legend(loc='best')
plt.title('Mevsimsellik Bileşeni')

# Rastlantısallık bileşeni
plt.subplot(414)
plt.plot(decomposition.resid, label='Rastlantısallık Bileşeni')
plt.legend(loc='best')
plt.title('Rastlantısallık Bileşeni')

plt.tight_layout()
plt.show()
