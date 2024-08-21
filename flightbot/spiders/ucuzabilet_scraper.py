import scrapy
from flightbot.items import ScrapedItem


class UcuzaBiletScraper(scrapy.Spider):
    name = "ucuzabilet_scraper"
    start_urls = [
        'https://www.ucuzabilet.com/en-ucuz-ucak-bileti-ic-hatlar',
    ]

    def parse(self, response):
        for flight in response.css('tr[data-flight-type="yurtici"]'):
            item = ScrapedItem()
            item['havayolu'] = flight.css('td:nth-child(2) > span::text').extract_first()
            item['kalkis_sehir'] = flight.css("::attr(data-from-city)").extract_first()
            item['kalkis_havalimani'] = flight.css("::attr(data-from-airport)").extract_first()
            item['kalkis_havalimani_kodu'] = flight.css("::attr(data-from-airport-code)").extract_first()
            item['varis_sehir'] = flight.css("::attr(data-to-city)").extract_first()
            item['varis_havalimani'] = flight.css("::attr(data-to-airport)").extract_first()
            item['varis_havalimani_kodu'] = flight.css("::attr(data-to-airport-code)").extract_first()
            item['tarih'] = flight.css('::attr(data-flight-date)').extract_first()
            item['fiyat'] = flight.css("::attr(data-price)").extract_first()
            yield item