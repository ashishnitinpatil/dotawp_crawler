# This is the scrapy spider that is run.
# The parse_item method of the DotawpSpider extracts the image data
# from the site's pages which are then downloaded & stored by ImagePipeline

from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from DotaWp.items import DotawpItem
from scrapy.log import ScrapyFileLogObserver, logging
from urlparse import urlparse


class DotawpSpider(CrawlSpider):

    name = 'dotawp'
    allowed_domains = ['www.dotawp.com']
    start_urls = ['http://www.dotawp.com/']
    rules = (
            Rule(
                SgmlLinkExtractor(
                    allow = ('dotawp.com/[\w-]+'),
                    unique = True
            ),
            callback = 'parse_item',
            follow = True
        ),
    )

    def parse_item(self, response):
        sel = Selector(response)
        item = DotawpItem()
        if not 'tag' in response.url and \
           not 'page' in response.url and \
           not 'category' in response.url:

            title = sel.xpath('//h1/text()').extract()[0]
            item['title'] = title.strip()
            item['image_urls'] = [sel.xpath('//p/a/img/@src').extract()[0]]

        return item
