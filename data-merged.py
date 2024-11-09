import pandas as pd

# Yalnızca ihtiyaç duyulan sütunları seçin
columns_to_use = [
    "Date", "Time", "Temperature", "Dew Point", "Humidity", 
    "Wind", "Wind Speed", "Pressure", "Condition"
]

# Birleştirilecek dosyaların isimlerini liste halinde belirtin
files = [
    "weather_data.csv",
    "weather_data_from_2017-12-05.csv",
    "weather_data_from_2018-10-24.csv",
    "weather_data_from_2024-05-12.csv"
]

# Dosyaları birleştirirken sadece gerekli sütunları al
dataframes = [pd.read_csv(file, usecols=columns_to_use, on_bad_lines='skip') for file in files]
merged_df = pd.concat(dataframes, ignore_index=True)

# Birleştirilmiş veriyi yeni bir CSV dosyasına kaydet
merged_df.to_csv("merged_weather_data.csv", index=False)

print("Dosyalar başarıyla birleştirildi ve 'merged_weather_data.csv' olarak kaydedildi.")
