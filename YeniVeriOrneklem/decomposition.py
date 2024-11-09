import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

#df = pd.read_csv("İslenmisAnaVeri/tr_weather_data_filled_new.csv")
df = pd.read_csv("YeniVeriOrneklem/daily_weather_data_new.csv")

yil = 2024

# 'Tarih' sütununu datetime formatına çevirme
df['Tarih'] = pd.to_datetime(df['Tarih'])

# Zaman serisi indeksini ayarlama
df.set_index('Tarih', inplace=True)

# Sıcaklık sütunundaki birimleri kaldırarak sayısal değere çevirme
df['Sıcaklık'] = df['Sıcaklık'].replace({'°C': '', '°': ''}, regex=True)  # °C birimini kaldırıyoruz
df['Sıcaklık'] = pd.to_numeric(df['Sıcaklık'], errors='coerce')  # Sayıya dönüştürme

# Yıla göre veri seçme
df_yil = df[df.index.year == yil] 

# Zaman serisi dekompozisyonu (periyot=24 saatlik veriler için)
decomposition = seasonal_decompose(df['Sıcaklık'], model='additive', period=24)  # 24 saatlik bir döngü kullanıyoruz
decomposition_yil = seasonal_decompose(df_yil['Sıcaklık'], model='additive', period=24)  # Seçilen yıl verisi için dekompozisyon

# Tüm veri için dekompozisyonları görselleştirme
plt.figure(figsize=(12, 8))

# Orijinal veri
plt.subplot(4, 2, 1)
plt.plot(df['Sıcaklık'], label='Orijinal Veri')
plt.legend(loc='best')
plt.title('Orijinal Veri')

# Orijinal veri (yila göre)
plt.subplot(4, 2, 2)
plt.plot(df_yil['Sıcaklık'], label=f'Orijinal Veri ({yil})', color='red') 
plt.legend(loc='best')
plt.title(f'Orijinal Veri ({yil})')

# Trend bileşeni
plt.subplot(4, 2, 3)
plt.plot(decomposition.trend, label='Trend Bileşeni')
plt.legend(loc='best')
plt.title('Trend Bileşeni')

# Trend bileşeni (yila göre)
plt.subplot(4, 2, 4)
plt.plot(decomposition_yil.trend, label=f'Trend Bileşeni ({yil})', color='red') 
plt.legend(loc='best')
plt.title(f'Trend Bileşeni ({yil})')

# Mevsimsellik bileşeni
plt.subplot(4, 2, 5)
plt.plot(decomposition.seasonal, label='Mevsimsellik Bileşeni')
plt.legend(loc='best')
plt.title('Mevsimsellik Bileşeni')

# Mevsimsellik bileşeni (yila göre)
plt.subplot(4, 2, 6)
plt.plot(decomposition_yil.seasonal, label=f'Mevsimsellik Bileşeni ({yil})', color='red')  
plt.legend(loc='best')
plt.title(f'Mevsimsellik Bileşeni ({yil})')

# Rastlantısallık bileşeni
plt.subplot(4, 2, 7)
plt.plot(decomposition.resid, label='Rastlantısallık Bileşeni')
plt.legend(loc='best')
plt.title('Rastlantısallık Bileşeni')

# Rastlantısallık bileşeni (yila göre)
plt.subplot(4, 2, 8)
plt.plot(decomposition_yil.resid, label=f'Rastlantısallık Bileşeni ({yil})', color='red') 
plt.legend(loc='best')
plt.title(f'Rastlantısallık Bileşeni ({yil})')


plt.tight_layout()
plt.show()