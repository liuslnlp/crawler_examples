from doubanmovie.items import DoubanmovieItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor


class DouBanSpider(CrawlSpider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = [
        'https://movie.douban.com/tag/',
    ]

    rules = (
        Rule(LinkExtractor(allow=('tag/'))),
        Rule(LinkExtractor(allow=('&type=T'), deny=('subject/'))),
        Rule(LinkExtractor(allow=('subject/',)), callback='parse_item'),
    )

    def parse_item(self, response):
        item = DoubanmovieItem()
        sel = Selector(response)

        title = sel.xpath('//*[@id="content"]/h1/span[1]/text()').extract()[0]
        year = sel.xpath('//*[@id="content"]/h1/span[2]/text()').extract()[0]
        commit_num = sel.xpath(
            '//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()').extract()[0]
        star = sel.xpath(
            '//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract()[0]
        director = sel.xpath(
            '//*[@id="info"]/span[1]/span[2]/a/text()').extract()[0]
        screenwriter = sel.xpath(
            '//*[@id="info"]/span[2]/span[2]/a/text()').extract()[0]

        item['title'] = title
        item['date'] = year
        item['star'] = star
        item['commit_num'] = commit_num
        item['director'] = director
        item['screenwriter'] = screenwriter

        return item
