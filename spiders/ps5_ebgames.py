import scrapy

class EbSpider(scrapy.Spider):
    name = "ebgames"

    def start_requests(self):
        urls = ['https://www.ebgames.ca/PS5/Games/877523','https://www.ebgames.ca/PS5/Games/877522']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        nostock = response.xpath("/html/body/div[4]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/table//a[1]//@style").get()
        name = response.xpath("/html/head/meta[8]/@content").get(),
        price = ('499.99','629.99')[name[0] != 'PlayStation 5 Digital Edition']
        yield {
                'name': name[0],
                'price': price,
                'stock': (nostock != 'display:none;'),
                'url': response.url,
                'image': response.xpath("/html/body/div[4]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/a/img/@src").get(),
            }

