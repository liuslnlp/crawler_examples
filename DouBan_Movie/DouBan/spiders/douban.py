from DouBan.items import DoubanItem
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request

class DouBanSpider(CrawlSpider):
    name = 'doubanSpider'
    start_urls = [
    'http://movie.douban.com/top250',
    ]
    
    t_url = 'http://movie.douban.com/top250'

    def parse(self, response):
        item = DoubanItem()
        sel = Selector(response)

        movie_infos = sel.xpath('//div[@class="info"]')
        for movie_info in movie_infos:
            title = movie_info.xpath('div[@class="hd"]/a/span[@class="title"]/text()').extract()
            # 电影介绍内有许多无关字符，所以需要清理一下
            t_info = movie_info.xpath('div[@class="bd"]/p/text()').extract()
            t1_info = t_info[0].replace("\n", '')
            info = t1_info.replace(" ", '')
            star = movie_info.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
            evaNum = movie_info.xpath('div[@class="bd"]/div[@class="star"]/span[4]/text()').extract()
            quote = movie_info.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()

            item['title'] = title
            item['info'] = info
            item['star'] = star
            item['evaNum'] = evaNum
            item['quote'] = quote

            yield item

        url = sel.xpath('//span[@class="next"]/link/@href').extract()
        if url:
            url = url[0]
            print(url)
            yield Request(self.t_url + url, callback=self.parse)

