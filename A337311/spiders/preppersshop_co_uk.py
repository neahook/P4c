from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class PreppersshopCoUk(BasePortiaSpider):
    name = "www.preppersshop.co.uk"
    allowed_domains = [u'www.preppersshop.co.uk']
    start_urls = [
        u'https://www.preppersshop.co.uk/baofeng-uv-5r-dual-band-uhfvhf-radio-9351-p.asp']
    rules = [
        Rule(
            LinkExtractor(
                allow=(),
                deny=('.*')
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                PortiaItem,
                None,
                u'.cf:nth-child(5)',
                [
                    Field(
                        u'Image1',
                        'div:nth-child(1) > .main-image > a > span > img::attr(src)',
                        []),
                    Field(
                        u'Image2',
                        'div:nth-child(1) > .product-thumbnails > div:nth-child(1) > a > img::attr(src)',
                        []),
                    Field(
                        u'Image3',
                        'div:nth-child(1) > .product-thumbnails > div:nth-child(2) > a > img::attr(src)',
                        []),
                    Field(
                        u'Product_Name',
                        'form > div:nth-child(2) > h1 > span *::text',
                        []),
                    Field(
                        u'Product_Desc',
                        'form > div:nth-child(2) > div > div:nth-child(2) > .tabCont > .product-description > span > span > span *::text',
                        []),
                    Field(
                        u'prod_Brand',
                        'form > div:nth-child(2) > div > div:nth-child(2) > .tabCont > .attribute > span > span *::text',
                        []),
                    Field(
                        u'RRP',
                        'form > div:nth-child(3) > .cf > div:nth-child(1) > font > span > font > strike > span *::text',
                        []),
                    Field(
                        u'Price',
                        'form > div:nth-child(3) > .cf > div:nth-child(2) > span > .price-alt > span::attr(content)',
                        []),
                    Field(
                        u'Points',
                        'form > div:nth-child(3) > .cf > div:nth-child(3) > strong > span *::text',
                        [])])]]
