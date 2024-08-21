![Kapak Fotoğrafı](https://i.hizliresim.com/re6fj55.jpg "Kapak Fotoğrafı")


# UcuzUcakBileti-Otomasyonu

UcuzaBilet'in sunduğu fırsat uçak biletlerini belirli aralıklarla kontrol ederek istenilen rota-tarih ve fiyata uygun uçak bileti bulunduğunda haber veren bir konsol otomasyonudur.

## Nasıl Çalıştırılır?

1- Dosyaları ana bilgisayarınıza klonlayın

    git clone https://github.com/enescaakir/UcuzUcakBileti-Otomasyonu.git

2- Bilgisayarınıza python yükleyin: [Python İndir](https://www.python.org/downloads/)

3- Klonladığınız dosyaların bulunduğu ana klasöre giderek aşağıdaki komut ile _main.py_'i çalıştırın

    python main.py

> [!WARNING] 
"_python_ komutu bulunamadı" gibi bir hata alırsanız yüklediğiniz python versiyonunun major sürümüyle beraber kullanmayı deneyiniz. Python sürümününüz öğrenmek için:

    python --version
    Version: Python 3.12.5

> [!NOTE]
Major versiyon ile konsolun çalıştırılması:
  
    python3 main.py

## Filtreler

* Kalkış - Varış havalimanı seçimi (zorunlu)
* Uçuş tarihi seçimi (isteğe bağlı)
* Fiyat limiti (isteğe bağlı)

## Özellikler

* Uygun uçuş bulunduğunda konsol ekranına uçuş bilgilerini gösterir
* Uygun uçuş bulunduğunda bildirim sesi çalar
* (DAHA EKLENMEDİ) Uygun uçuş bulunduğunda email gönderir
