import time
import os
import requests
from datetime import datetime
from flightbot.spiders.ucuzabilet_scraper import UcuzaBiletScraper as scraper

def play_sound():
    if os.name == 'nt':  # Windows
        import winsound
        frequency = 2500
        duration = 1000
        winsound.Beep(frequency, duration)
    else:  # macOS ve Linux
        os.system('afplay /System/Library/Sounds/Glass.aiff')

def get_input(prompt, validate=None):
    while True:
        user_input = input(prompt)
        if validate is None or validate(user_input):
            return user_input
        print("Hatalı giriş yaptınız. Lütfen tekrar deneyiniz:")

def is_valid_date(date_str):
    if not date_str:
        return True
    try:
        datetime.strptime(date_str, '%d-%m-%Y')
        return True
    except ValueError:
        return False

def is_valid_price(price_str):
    if not price_str:
        return True
    elif price_str.isdigit():
        return True
    else:
        return False

def fetch_flights():
    spider_name = scraper.name
    url = f"http://localhost:9080/crawl.json?spider_name={spider_name}&start_requests=true"
    max_retry = 3
    retries = 0
    try:
        for _ in range(max_retry):
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json().get('items', [])
                if not data:
                    raise ValueError("Uçuşlar alınamadı. Daha sonra tekrar deneyiniz.")
                return data
            retries += 1
            time.sleep(5)
    except:
        raise ConnectionError("Uçuşlar alınamadı. Scrapyrt sunucusunun çalıştığından emin olduktan sonra tekrar deneyiniz.")

def filter_flights(flights, from_airport, to_airport, flight_date=None, price=None):
    return [
        flight for flight in flights
        if flight["kalkis_havalimani_kodu"].lower() == from_airport.lower() and 
           flight["varis_havalimani_kodu"].lower() == to_airport.lower() and 
           (not flight_date or flight["tarih"] == flight_date) and
           (not price or float(flight["fiyat"]) <= float(price))
    ]

def task():
    print("Uçak bileti takip sistemine hoşgeldiniz.")
    
    from_airport_code = get_input("\nKalkış havalimanı kodunu giriniz: ")
    to_airport_code = get_input("\nVarış havalimanı kodunu giriniz: ")
    flight_date = get_input("\nUçuş tarihini (Gün-Ay-Yıl) formatında giriniz.\nEn yakın tarih için bilet araştırması yapıyorsanız boş bırakınız: ", is_valid_date)
    price = get_input("\nBilet fiyatı limitini giriniz (Örnek: 2000).\nBu limitin altında uygun bilet araması yapılacaktır:", is_valid_price)
    
    while True:
        print("Girdiğiniz bilgilere uygun uçuşlar aranıyor... Tarih: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        try:
            flights = fetch_flights()
        except Exception as e:
            print(str(e))
            break

        matched_flights = filter_flights(flights, from_airport_code, to_airport_code, flight_date, price)

        if matched_flights:
            play_sound()
            print("Uygun uçuşlar bulundu.")
            
            cheapest_flight = matched_flights[0]
            print(f"{cheapest_flight['tarih']} tarihli uçuş için en ucuz bilet fiyatı: {cheapest_flight['fiyat']} TL")
            break

        time.sleep(60)

task()
