from csdnblog.items import CsdnblogItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors import LinkExtractor


class CSDNSpider(CrawlSpider):

    name = 'csdn'
    allowed_domains = ['blog.csdn.net']
    start_urls = [
        'http://blog.csdn.net/peoplelist.html',
    ]

    rules = (
        Rule(LinkExtractor(allow=(
            'http://blog.csdn.net/[a-zA-Z\d]+', 'page=', 'article/list/'), deny=('article/details'))),
        Rule(LinkExtractor(allow=('article/details/',)), callback='parse_item'),
    )

    def parse_item(self, response):
        item = CsdnblogItem()
        sel = Selector(response)
        try:
            item['title'] = sel.xpath('//*[@id="article_details"]/div[1]/h1/span/a/text()').extract()[
                1].replace("\r\n", "").replace(" ", "")
        except:
            item['title'] = sel.xpath('//*[@id="article_details"]/div[1]/h1/span/a/text()').extract()[
                0].replace("\r\n", "").replace(" ", "")

        item['content'] = sel.xpath('//*[@id="article_content"]').extract()[0]

        item['author'] = sel.xpath(
            '//*[@id="blog_userface"]/span/a/text()').extract()[0]

        try:
            item['date'] = sel.xpath(
                '//*[@id="article_details"]/div[2]/div[2]/span[1]/text()').extract()[0]
        except:
            item['date'] = "NoData"

        try:
            item['read_num'] = sel.xpath(
                '//*[@id="article_details"]/div[2]/div[2]/span[2]/text()').extract()[0]
        except:
            item['read_num'] = "NoData"

        item['tags'] = sel.xpath(
            '//span[@class="link_categories"]//a/text()').extract()

        try:
            item['digg_num'] = sel.xpath(
                '//*[@id="btnDigg"]/dd/text()').extract()[0]
            item['bury_num'] = sel.xpath(
                '//*[@id="btnBury"]/dd/text()').extract()[0]
        except:
            item['digg_num'] = '0'
            item['bury_num'] = '0'

        return item
