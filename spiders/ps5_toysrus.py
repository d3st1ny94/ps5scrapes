import scrapy

class ToyRUsPs5StockSpider(scrapy.Spider):
    name = "toysrus"

    def start_requests(self):
        url = 'https://www.toysrus.ca/en/PlayStation-5-Console/C443A89B.html'
        yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        nostock = response.xpath('//html//body//div[1]//main//div//div[2]//div[2]//div//div[8]//div//ul//li//text()').get()
        yield {
                'name': response.xpath("/html/head/meta[8]/@content").get(),
                'price': response.xpath("/html/head/meta[5]/@content").get(),
                'stock': (nostock != 'Out of Stock'),
                'url': response.xpath("/html/head/meta[10]/@content").get(),
                'image': response.xpath("/html/head/meta[4]/@content").get(),
            }

