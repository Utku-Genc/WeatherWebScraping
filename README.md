# Hava Durumu Veri Toplama

## Proje Hakkında
Bu proje, Yazılım Geliştirme Laboratuvarı-I dersi kapsamında yapacağımız proje için hava durumu verilerini toplama, eksik - hatalı verileri işleme ve analiz etme kısımlarını içermektedir. Proje, belirli bir bölgenin belirli bir tarih aralığında hava durumu için biraz önce bahsettiğim adımları yapmaktadır.

## Projeyi Kurma 

### 1. Projeyi Klonlayın 
İlk olarak, projeyi GitHub üzerinden kendi cihazınıza klonlayın. Git yüklü değilse, [Git'i buradan](https://git-scm.com/) indirip kurabilirsiniz. 
<br>
Aşağıdaki komutları sırasıyla terminale yazarak projeyi klonlayın: 
```bash
git clone https://github.com/Utku-Genc/WeatherWebScraping.git
```
Eğer ilk komutu çalıştırdığınızda bir hata almadıysanız aşağıdaki kodu terminale yazarak projenin bulunduğu dizine geçme işlemini yapabiliriz.
```bash
cd WeatherWebScraping
```
Hata almadan işlemi tamamladıysanız aşağıda belirtilen gereksinimleri cihazınıza kurunuz. <br>
Eğer yukardaki komutu çalıştırırken hata aldıysanız projenin kurulumu doğru yapılamamış demektir. Tekrar ilk adımı deneyiniz. 

### 2. Gereksinimler

#### 2.1. Python

Proje, **Python 3.10.11** sürümü ile çalışmaktadır. İndirme sayfasına  [buradan ulaşabilirsiniz.](https://git-scm.com/) 
Python'un doğru sürümünü yüklediğinizden emin olmak için terminalde aşağıdaki komutu çalıştırarak Python sürümünü kontrol edebilirsiniz:
```bash
python --version 
```
#### 2.2. Gerekli Kütüphaneler ve Kurulum

Projede kullanılan gerekli Python kütüphanelerini yüklemek için aşağıdaki komutu terminalinize yazabilirsiniz:



```bash
pip install pandas==2.2.3 matplotlib==3.9.2 statsmodels==0.14.4 selenium==4.25.0
```

Bu komut, aşağıdaki kütüphaneleri kodumuzla uyumlu çalışacak versiyonlarını yükleyecektir:

-   **Selenium:** Veri çekme işlemleri için web tarayıcı otomasyonunu sağlar.
-   **Pandas:** Veri dosyalarını okuma, düzenleme ve analiz etme işlemleri için kullanılır.
-   **Matplotlib:** Verileri görselleştirmek (grafik, tablo vb.) için kullanılır.
-   **Statsmodels:** Zaman serisi verilerini analiz etmek için kullanılır.

## Projeyi Çalıştırma

Aşağıda projeyi çalıştırmak için izlemeniz gereken adımlar bulunmaktadır.

### 1. Veri Toplama Kısmı


#### 1.1. Tekil Veri Çekme
İlk olarak, belirli bir şehirdeki güncel hava durumu verisini kontrol etmek için `1-tekil-veri-cekme.py` dosyasını çalıştıracağız.

1. **Dosyayı açın**: `AnaVeri/1-tekil-veri-cekme.py`
2. **Şehir ismini belirleyin**: `city` değişkenine test etmek istediğiniz şehri yazın.
	
![1](https://github.com/user-attachments/assets/934f5a12-5636-4c2d-85f3-4feae4f7c660)

3.  **Kodu çalıştırın**: Terminal veya komut satırında aşağıdaki komutu çalıştırın:
    ```bash
    python AnaVeri/1-tekil-veri-cekme.py  
    ```
    
4.  **Sonuç**: Eğer veri mevcutsa, o güne ait 30 dakikalık aralıklarla güncellenmiş hava durumu verisi terminalde çıktı olarak gösterilecektir.

#### 1.2. Toplu Veri Çekme

Eğer o günün verisi mevcutsa, daha geniş bir tarih aralığı ile veri toplamak için `2-toplu-veri-cekme.py` dosyasını kullanacağız.

1.  **Dosyayı açın**: `AnaVeri/2-toplu-veri-cekme.py`
2.  **Şehir ismini belirleyin**: `city` değişkenine şehir ismini yazın.
3.  **Tarih aralığını belirleyin**: `start_date` ve `end_date` değişkenlerine veri çekmek istediğiniz tarih aralığını yazın.

![2](https://github.com/user-attachments/assets/dfd208d8-20e6-4a57-83fc-da177b6bb7e0)


5.  **Kodu çalıştırın**: Terminal veya komut satırında aşağıdaki komutu çalıştırın:
     ```bash
    python AnaVeri/2-toplu-veri-cekme.py 
    ```
    
6.  **Sonuç**: Kod çalıştıktan sonra, `AnaVeri` dizininde `{city}_weather_data_from_{start_date}.csv` adıyla bir veri dosyası oluşturulacaktır.

#### 1.3. Veri Birleştirme

Eğer parça parça veri çektiyseniz, farklı dosyaları birleştirmek için `3-veri-birlestirme.py` dosyasını kullanabilirsiniz.

1.  **Dosyayı açın**: `AnaVeri/3-veri-birlestirme.py`
2.  **Birleştirilecek dosyaları belirleyin**: `files` klasörüne birleştirilmesi gereken dosyaları ekleyin.
		
![3](https://github.com/user-attachments/assets/2cb767b8-7cd4-48d6-99b6-7181db96690e)

3.  **Kodu çalıştırın**: Terminal veya komut satırında aşağıdaki komutu çalıştırın:
    

     ```bash
    python AnaVeri/3-veri-birlestirme.py
    ```
    
4.  **Sonuç**: Birleştirilmiş veri, `AnaVeri/merged_weather_data.csv` dosyasında saklanacaktır.

### 2. Veri İşleme

#### 2.1. Veri Düzenleme

Birleştirilmiş veriyi işlemek için `İslenmisAnaVeri/1-veri-duzenleme.py` dosyasını çalıştıracağız.

1.  **Dosyayı açın**: `IslenmisAnaVeri/1-veri-duzenleme.py`
2.  **Kodu çalıştırın**: Terminal veya komut satırında aşağıdaki komutu çalıştırın:
    

	   ```bash
    python IslenmisAnaVeri/1-veri-duzenleme.py
    ```
    
3.  **Sonuç**: Bu işlem, `merged_weather_data.csv` dosyasındaki metinleri temizleyecek, Türkçeleştirecek ve Fahrenheit cinsinden gelen sıcaklıkları Celsius'a çevirecektir. Sonuç `IslenmisAnaVeri/tr_weather_data.csv` olarak kaydedilecektir Farkını aşağıda görebilirsiniz.
 
![4](https://github.com/user-attachments/assets/5413969f-f1f4-413f-8c33-ce04c928cc71)

![5](https://github.com/user-attachments/assets/7e87b7d6-fdc8-4728-960b-cc5f2ebd1e94)

#### 2.2. Boş Veri Doldurma

Boş veri olup olmadığını kontrol etmek ve eksik verileri doldurmak için `2-veri-bos-doldurma.py` dosyasını çalıştıracağız.

1.  **Dosyayı açın**: `IslenmisAnaVeri/2-veri-bos-doldurma.py`
2.  **Kodu çalıştırın**: Terminal veya komut satırında aşağıdaki komutu çalıştırın:
    
	```bash
    python IslenmisAnaVeri/2-veri-bos-doldurma.py
    ``` 
    
3.  **Sonuç**: Bu işlem sonucunda, boş veri kontrolü yapılacak ve eksik veriler uygun şekilde doldurulacaktır. Sonuç `IslenmisAnaVeri/tr_weather_data_filled.csv` olarak kaydedilecektir.

#### 2.3. Grafik Görselleştirme

İşlenmiş verilerle ilgili temel grafikler oluşturmak için `4-graphics.py` dosyasını çalıştıracağız.

1.  **Dosyayı açın**: `IslenmisAnaVeri/4-graphics.py`
2.  **Kodu çalıştırın**: Terminal veya komut satırında aşağıdaki komutu çalıştırın:
    
    ```bash
	python IslenmisAnaVeri/4-graphics.py 
    ```
    
3.  **Sonuç**: Bu işlem, işlenmiş verilerle ilgili temel grafiklerin gösterilmesini sağlar. Örnek grafiklere aşağıda görebilirsiniz.

![6](https://github.com/user-attachments/assets/d5229d76-ec32-453b-8d87-51d6de5cf74a)

![7](https://github.com/user-attachments/assets/491e9a11-73be-4790-8385-fd476ccb048e)


### 3. Yeni Veri Örneklemesi

#### 3.1. Veri Örnekleme

İşlenmiş verileri günlük ortalamalarla yeniden düzenlemek için `YeniVeriOrneklem/1-veri-ornekleme.py` dosyasını çalıştıracağız.

1.  **Dosyayı açın**: `YeniVeriOrneklem/1-veri-ornekleme.py`
2.  **Kodu çalıştırın**: Terminal veya komut satırında aşağıdaki komutu çalıştırın:

    ```bash
    python YeniVeriOrneklem/1-veri-ornekleme.py
    ```
    
3.  **Sonuç**: Bu işlem, 30 dakikalık veri dosyasından günlük veri dosyasına dönüştürülmüş yeni bir dosya oluşturur. Küçük bir örnek aşağıdadır.

![8](https://github.com/user-attachments/assets/b069d305-b243-4c60-b287-cad9f8e4093b)

#### 3.2. Decomposition (Bileşenlere Ayrılma)

Verileri mevsimsellik, trend ve rastlantısallık gibi bileşenlere ayırmak için `YeniVeriOrneklem/2-decomposition.py` dosyasını çalıştıracağız.

1.  **Dosyayı açın**: `YeniVeriOrneklem/2-decomposition.py`
2.  **CSV dosyasının yolunu girin**: `csv_file` değişkenine analiz etmek istediğiniz CSV dosyasının yolunu belirtin.
3.  **Yıl değişkenini belirleyin**: `year` değişkenine analiz etmek istediğiniz yılı yazın.
4.  **Kodu çalıştırın**: Terminal veya komut satırında aşağıdaki komutu çalıştırın:
    
	 ```bash
    python YeniVeriOrneklem/2-decomposition.py
    ```

5.  **Sonuç**: Bu işlem sonucunda, orijinal, trend, mevsimsellik ve rastlantısallık verileriyle 8 farklı grafik elde edilecektir.

![9](https://github.com/user-attachments/assets/7c93a742-b536-4c23-9a4c-87ce99b9c1db)


## Ekler
Proje Raporu: [Rapor](https://github.com/user-attachments/files/17698423/yazlab-rapor-sonhal.docx)

<br>
Proje Kapsamında Toplanan Veriler: [Veri Seti](https://drive.google.com/drive/u/0/folders/1eSPkRUiUx6AkxZYrtghkakOASbia3wuu)
