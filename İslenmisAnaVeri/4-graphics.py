import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. CSV dosyasını yükleme
data = pd.read_csv("İslenmisAnaVeri/tr_weather_data_filled_new.csv")

# 2. Sütun isimlerindeki boşlukları temizleme
data.columns = data.columns.str.strip()

# 3. Tarih ve Saat sütunlarını birleştirip Datetime formatına dönüştürme
data['DateTime'] = pd.to_datetime(data['Tarih'] + ' ' + data['Saat'], errors='coerce')

# 4. Rüzgar Hızı sütununu sayısal birimlere dönüştürme
data['Rüzgar Hızı (mph)'] = data['Rüzgar Hızı (mph)'].astype(float)

# 5. Hava Durumu koşullarının dağılımını görselleştirme

weather_distribution = data['Durum'].value_counts()

# 6. Hava Durumu dağılımını gösteren pasta grafiği
top_categories = 4
weather_distribution = data['Durum'].value_counts()
other_categories = weather_distribution[top_categories:].sum()
weather_distribution = weather_distribution[:top_categories]
weather_distribution['Diğer'] = other_categories

# Pasta grafiği çizimi
plt.figure(figsize=(10, 10))
weather_distribution.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'orange', 'lightcoral', 'lightgrey'])
plt.title('Hava Durumu Dağılımı')
plt.ylabel('')
plt.show()


# 7. Rüzgar hızını zamanla görselleştirme
plt.figure(figsize=(14, 7))
plt.plot(data['DateTime'], data['Rüzgar Hızı (mph)'], label='Rüzgar Hızı (mph)', color='tab:blue')
plt.xlabel("Tarih ve Saat")
plt.ylabel("Rüzgar Hızı (mph)")
plt.title("Zamana Göre Rüzgar Hızı")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# 8. Sıcaklık sütununu sayısal birimlere dönüştürme
data['Sıcaklık'] = pd.to_numeric(data['Sıcaklık'].str.replace('°C', '').str.strip(), errors='coerce')

# 9. Sıcaklık değişimini görselleştirme
plt.figure(figsize=(14, 7))
plt.plot(data['DateTime'], data['Sıcaklık'], label="Sıcaklık (°C)", color='tab:red')
plt.xlabel("Tarih")
plt.ylabel("Sıcaklık (°C)")
plt.title("Zamana Göre Sıcaklık Değişimi")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 10. Nem oranını sayısal birimlere dönüştürme
data['Nem %'] = pd.to_numeric(data['Nem %'], errors='coerce')

# 11. Nem değişimini görselleştirme
plt.figure(figsize=(14, 7))
plt.plot(data['DateTime'], data['Nem %'], label="Nem (%)", color='tab:green')
plt.xlabel("Tarih")
plt.ylabel("Nem (%)")
plt.title("Zamana Göre Nem Değişimi")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 12. Çiğ Noktası sütununu sayısal birimlere dönüştürme
data['Çiğ Noktası'] = pd.to_numeric(data['Çiğ Noktası'].str.replace('°C', '').str.strip(), errors='coerce')

# 13. Sıcaklık ve Çiğ Noktası değişimini aynı grafikte görselleştirme
plt.figure(figsize=(14, 7))
plt.plot(data['DateTime'], data['Sıcaklık'], label="Sıcaklık (°C)", color='tab:red')
plt.plot(data['DateTime'], data['Çiğ Noktası'], label="Çiğ Noktası (°C)", color='tab:blue')
plt.xlabel("Tarih")
plt.ylabel("Sıcaklık (°C)")
plt.title("Zamana Göre Sıcaklık ve Çiğ Noktası Değişimi")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 14. Basıncı sayısal birimlere dönüştürme
data['Basınç (in)'] = pd.to_numeric(data['Basınç (in)'], errors='coerce')

# 15. Basınç değişimini görselleştirme
plt.figure(figsize=(14, 7))
plt.plot(data['DateTime'], data['Basınç (in)'], label="Basınç (in)", color='tab:purple')
plt.xlabel("Tarih")
plt.ylabel("Basınç (in)")
plt.title("Zamana Göre Basınç Değişimi")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 16. Rüzgar Yönü analizleri

# Rüzgar yönlerini sayısal açılara dönüştürme
wind_directions = {
    'Kuzey': 0, 'Kuzeydoğu-Kuzey': 22.5, 'Kuzeydoğu': 45, 'Kuzeydoğu-Doğu': 67.5,
    'Doğu': 90, 'Güneydoğu-Doğu': 112.5, 'Güneydoğu': 135, 'Güneydoğu-Güney': 157.5,
    'Güney': 180, 'Güneybatı-Güney': 202.5, 'Güneybatı': 225, 'Güneybatı-Batı': 247.5,
    'Batı': 270, 'Kuzeybatı-Batı': 292.5, 'Kuzeybatı': 315, 'Kuzeybatı-Kuzey': 337.5
}
data['Wind Direction Angle'] = data['Rüzgar Yönü'].map(wind_directions)

# Kutupsal (polar) grafikte rüzgar yönü dağılımı
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
wind_counts = data['Wind Direction Angle'].value_counts().sort_index()

# Kutupsal grafikte gösterim
acilar = np.deg2rad(wind_counts.index)
ax.bar(acilar, wind_counts.values, color='lightblue', edgecolor='black', alpha=0.7, width=0.3)

# Grafik başlığı ve ayarları
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_xticks(np.deg2rad(list(wind_directions.values())))
ax.set_xticklabels(list(wind_directions.keys()))
plt.title('Rüzgar Yönü Dağılımı (Polar Grafik)')
plt.show()

# Çubuk grafikte rüzgar yönü dağılımı
plt.figure(figsize=(10, 6))
data['Rüzgar Yönü'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Rüzgar Yönü Dağılımı')
plt.xlabel('Rüzgar Yönü')
plt.ylabel('Frekans')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
