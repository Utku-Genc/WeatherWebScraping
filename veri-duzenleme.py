import pandas as pd

df = pd.read_csv("merged_weather_data.csv")

# Rüzgar yönü Türkçeye çevirme
wind_translation = {
    "VAR": "Değişken", 
    "NNE": "Kuzeydoğu-Kuzey", 
    "NE": "Kuzeydoğu",
    "CALM": "Rüzgarsız", 
    "SSE": "Güneydoğu-Güney",
    "S": "Güney",
    "SSW": "Güneybatı-Güney",
    "WSW": "Batı-Güneybatı", 
    "SW": "Güneybatı",
    "W": "Batı",
    "SE": "Güneydoğu",
    "ESE": "Doğu-Güneydoğu", 
    "E": "Doğu", 
    "N": "Kuzey", 
    "ENE": "Kuzeydoğu-Doğu", 
    "WNW": "Batı-Kuzeybatı", 
    "NNW": "Kuzey-Kuzeybatı", 
    "NW": "Kuzeybatı", 
    "nan": "Bilinmiyor"
}

df["Wind"] = df["Wind"].replace(wind_translation)

# Time sütununu 24 saatlik sisteme çevirme
df["Time"] = pd.to_datetime(df["Time"], format='%I:%M %p').dt.strftime('%H:%M')

# Sıcaklık ve çiğ noktasını Celsius'a çevirme
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

df["Temperature"] = df["Temperature"].apply(lambda x: f"{fahrenheit_to_celsius(float(x.split()[0])):.2f} °C" if "°F" in x else x)
df["Dew Point"] = df["Dew Point"].apply(lambda x: f"{fahrenheit_to_celsius(float(x.split()[0])):.2f} °C" if "°F" in x else x)

# Nem değeriniden % kaldırma
df["Humidity"] = df["Humidity"].apply(lambda x: x.replace(" %", "") if "%" in x else x)

# Rüzgar hızında küsüratlı sayı olmadığı için direkt metni kaldırttık
df["Wind Speed"] = df["Wind Speed"].apply(lambda x: ''.join(filter(str.isdigit, x)))
# Basınç in ksımını kaldırma için sayı ile kelimeyi böldük
df["Pressure"] = df["Pressure"].apply(lambda x: f"{float(x.split()[0]):.2f}" if isinstance(x, str) else x)

# Hava durumunu türkçeye çevirme
condition_translation = {
    "Fair": "Açık", 
    "Partly Cloudy": "Parçalı Bulutlu", 
    "Mostly Cloudy": "Çoğunlukla Bulutlu",
    "Fair / Windy": "Açık / Rüzgarlı", 
    "Cloudy": "Bulutlu", 
    "Cloudy / Windy": "Bulutlu / Rüzgarlı",
    "Mostly Cloudy / Windy": "Çoğunlukla Bulutlu / Rüzgarlı", 
    "Mist": "Sislilik", 
    "Partly Cloudy / Windy": "Parçalı Bulutlu / Rüzgarlı", 
    "Rain Shower": "Yağmur Yağışı", 
    "Patches of Fog": "Sisli Bölge", 
    "Fog": "Sis", 
    "Light Drizzle": "Hafif Çiseleme", 
    "Light Rain": "Hafif Yağmur", 
    "T-Storm": "Fırtına", 
    "Heavy T-Storm": "Şiddetli Fırtına", 
    "Thunder": "Gök Gürültüsü", 
    "Thunder in the Vicinity": "Yakınlarda Gök Gürültüsü", 
    "Light Rain Shower": "Hafif Yağmur Yağışı", 
    "Rain": "Yağmur", 
    "Light Snow": "Hafif Kar", 
    "Snow Shower": "Kar Yağışı", 
    "Haze": "Dumanlı", 
    "Drizzle": "Çiseleme", 
    "Light Rain Shower / Windy": "Hafif Yağmur Yağışı / Rüzgarlı", 
    "Partial Fog": "Parçalı Sis", 
    "Smoke / Windy": "Duman / Rüzgarlı", 
    "Smoke": "Duman", 
    "Wintry Mix": "Karla Karışık Yağmur", 
    "Light Snow Shower": "Hafif Kar Yağışı", 
    "Rain / Windy": "Yağmur / Rüzgarlı", 
    "Fog / Windy": "Sis / Rüzgarlı", 
    "Mist / Windy": "Sis / Rüzgarlı", 
    "Snow / Windy": "Kar / Rüzgarlı", 
    "Light Snow / Windy": "Hafif Kar / Rüzgarlı", 
    "Snow": "Kar", 
    "Rain Shower / Windy": "Yağmur Yağışı / Rüzgarlı", 
    "Heavy Rain Shower": "Şiddetli Yağmur Yağışı", 
    "Small Hail": "Küçük Dolu", 
    "Shallow Fog": "Yüzeysel Sis", 
    "Drizzle / Windy": "Çiseleme / Rüzgarlı", 
    "Heavy Snow Shower": "Şiddetli Kar Yağışı", 
    "Funnel Cloud": "Dönme Bulutu", 
    "Haze / Windy": "Dumanlı / Rüzgarlı", 
    "Light Rain with Thunder": "Hafif Yağmur ve Gök Gürültüsü",
    "T-Storm / Windy": "Fırtına / Rüzgarlı"
}

df["Condition"] = df["Condition"].replace(condition_translation)

# Sütun isimlerini düzenleme
df.rename(columns={
    "Date": "Date (Tarih)",
    "Time": "Time (Saat)",
    "Temperature": "Temperature (Sıcaklık)",
    "Dew Point": "Dew Point (Çiğ Noktası)",
    "Humidity": "Humidity (Nem) %",
    "Wind": "Wind (Rüzgar Yönü)",
    "Wind Speed": "Wind Speed (Rüzgar Hızı) (mph)",
    "Pressure": "Pressure (Basınç) (in)",
    "Condition": "Condition (Durum)"
}, inplace=True)

df.to_csv("tr_weather_data.csv", index=False)

print("Veri düzenleme işlemi tamamlandı ve 'tr_weather_data.csv' olarak kaydedildi.")
