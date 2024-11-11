from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import datetime
import time

# Bugünün tarihini almak
today = datetime.date.today()
formatted_date = today.strftime("%Y-%m-%d")  # YYYY-MM-DD formatına getirme

# Dinamik URL
city = "kocaeli"  # Şehir adını burada değiştirin
url = f"https://www.wunderground.com/history/daily/tr/{city}/date/{formatted_date}"

# Chrome ayarları
chrome_options = Options()
chrome_options.add_argument("--incognito")

# WebDriver başlatma
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# Sayfanın tamamen yüklenmesini bekle
try:
    # Sayfanın yüklendiğindiğini anlamak için WebDriverWait 
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="inner-content"]/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]/table')))
    
    # Tablonun varlığını kontrol et
    table = driver.find_element(By.XPATH, '//*[@id="inner-content"]/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]/table')
    
    if table:
        print("Tablo bulundu, veri çekiliyor...")

        # Sütun adlarını al
        headers = driver.find_elements(By.XPATH, '//*[@id="inner-content"]/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]/table/thead/tr/th')
        header_names = [header.text for header in headers]
        print("Sütun Adları:", header_names)

        # Tablo verilerini al
        rows = driver.find_elements(By.XPATH, '//*[@id="inner-content"]/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]/table/tbody/tr')
        
        table_data = []
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            row_data = [column.text for column in columns]
            table_data.append(row_data)
        
        # kontrol için tablo verilerini yazdırma
        for data in table_data:
            print(data)
    
    else:
        print("Tablo bulunamadı.")
    
finally:
    # tarayıcıyı kapat
    driver.quit()
