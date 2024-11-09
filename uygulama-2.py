from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import datetime
import time

# tarih aralığı
city = "kocaeli" 
start_date = datetime.date(2011, 1, 1)  # Başlangıç tarihi
end_date = datetime.date(2024, 1, 1)    # Bitiş tarihi

chrome_options = Options()
chrome_options.add_argument("--incognito")

# WebDriver başlatma
driver = webdriver.Chrome(options=chrome_options)

# Tarih aralığında döngüsü
date = start_date
while date <= end_date:
    formatted_date = date.strftime("%Y-%m-%d")  # YYYY-MM-DD formatında tarih
    url = f"https://www.wunderground.com/history/daily/tr/{city}/date/{formatted_date}"
    
    # Web sayfasını açma
    driver.get(url)
    print(f"{formatted_date} için veriler çekiliyor...")
    
    # Sayfanın tamamen yüklenmesini bekleme
    try:
        # Tablo yüklendiğinde devam et
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="inner-content"]/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]/table')
            )
        )
        
        # Tabloyu bul ve verileri al
        table = driver.find_element(By.XPATH, '//*[@id="inner-content"]/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]/table')
        
        if table:
            print("Tablo bulundu, veri çekiliyor...")

            # Sütun adları
            headers = driver.find_elements(By.XPATH, '//*[@id="inner-content"]/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]/table/thead/tr/th')
            header_names = [header.text for header in headers]
            print("Sütun Adları:", header_names)

            # Tablo verileri
            rows = driver.find_elements(By.XPATH, '//*[@id="inner-content"]/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]/table/tbody/tr')
            
            table_data = []
            for row in rows:
                columns = row.find_elements(By.TAG_NAME, "td")
                row_data = [column.text for column in columns]
                table_data.append(row_data)
            
            # Tablo verilerini yazdır
            print(f"{formatted_date} için veri:")
            for data in table_data:
                print(data)
        
        else:
            print(f"{formatted_date} için tablo bulunamadı.")
        
    except Exception as e:
        print(f"{formatted_date} için veri alınamadı: {e}")
    
    # Bir sonraki güne geç
    date += datetime.timedelta(days=1)

# Tarayıcıyı kapat
driver.quit()
