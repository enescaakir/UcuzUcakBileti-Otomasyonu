import scrapy


class ScrapedItem(scrapy.Item):
    havayolu = scrapy.Field()
    kalkis_sehir = scrapy.Field()
    kalkis_havalimani = scrapy.Field()
    kalkis_havalimani_kodu = scrapy.Field()
    varis_sehir = scrapy.Field()
    varis_havalimani = scrapy.Field()
    varis_havalimani_kodu = scrapy.Field()
    tarih = scrapy.Field()
    fiyat = scrapy.Field()