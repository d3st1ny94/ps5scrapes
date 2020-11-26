import scrapy

class AmazonSpider(scrapy.Spider):
    name = "amazon"

    def start_requests(self):
        urls = ['https://www.amazon.ca/dp/B08GSC5D9G/','https://www.amazon.ca/dp/B08GS1N24H']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        nostock = response.xpath("/html/body/div/div[2]/div[4]/div[4]/div[1]/div[2]/div/div/div/div/div/form/div/div/div[1]/span/text()").get()
        name = response.xpath("/html/head/meta[5]/@content").get().split(' - ')[0]
        yield {
                'name': name,
                'price': ('499.99','629.99')[name != 'PlayStation 5 Console'],
                'stock': (nostock != 'Currently unavailable.'),
                'url': response.url,
                'image': response.xpath("/html/body/div/div[2]/div[4]/div[4]/div[3]/div/div[1]/div/div/div[2]/div[1]/div/ul/li[1]/span/span/div/img/@src").get(),
            }

