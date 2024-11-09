import pandas as pd

df = pd.read_csv('İslenmisAnaVeri/tr_weather_data_filled.csv')

# Tarih sütununu datetime formatına çevirme
df['Date (Tarih)'] = pd.to_datetime(df['Date (Tarih)'])

# Sayısal olmayan sütunları işlem dışı bırakmak
numerical_columns = df.select_dtypes(include=['number']).columns

# O tarih içinde ki en çok olan rüzgar yönü ile Hava Durumu
wind_mode = df.groupby(df['Date (Tarih)'])['Wind (Rüzgar Yönü)'].agg(lambda x: x.mode()[0])
condition_mode = df.groupby(df['Date (Tarih)'])['Condition (Durum)'].agg(lambda x: x.mode()[0])

# Sayısal sütunlar için ortalama değerleri hesaplama çok basamaklı olduğunda 2 basamak yaptık yuvarlama ile
df_grouped = df.groupby(df['Date (Tarih)'])[numerical_columns].mean().round(2)

# Rüzgar yönü ve durum verilerini ortalama veri çerçevesine ekleme
df_grouped['Wind (Rüzgar Yönü)'] = wind_mode
df_grouped['Condition (Durum)'] = condition_mode

# Console'da gösterme
print(df_grouped)

df_grouped.to_csv('YeniVeriOrneklem/daily_weather_data.csv')