

class UcuzaBiletPipeline(object):
    def process_item(self, item, spider):
        item["tarih"] = item["tarih"].replace(".", "-")
        return item
