import scrapy

class CostcoSpider(scrapy.Spider):
    name = "costco"
    def start_requests(self):
        url = 'https://www.costco.ca/.product.100696941.html'
        yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        nostock = response.xpath("/html/head/meta[27]/@content").get()
        yield {
                'name': response.xpath("/html/head/meta[21]/@content").get(),
                'price': response.xpath("/html/head/meta[25]/@content").get(),
                'stock': (nostock != 'out of stock'),
                'url': response.xpath("/html/head/meta[19]/@content").get(),
                'image': response.xpath("/html/head/meta[24]/@content").get(),
            }

