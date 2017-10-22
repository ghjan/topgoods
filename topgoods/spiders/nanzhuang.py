# -*- coding: utf-8 -*-
import scrapy
from topgoods.items import TopgoodsItem


class NanzhuangSpider(scrapy.Spider):
    name = 'nanzhuang'
    allowed_domains = ['list.tmall.com']
    start_urls = [
        'https://list.tmall.com/search_product.htm?spm=a221t.1710963.8073444875.14.1aeaec9eJYYbaT&new=1&cat=54468002&active=1&acm=lb-zebra-7499-292762.1003.4.427962&style=g&from=sn_1_cat&shopType=any&sort=s&search_condition=71&scm=1003.4.lb-zebra-7499-292762.OTHER_14748224486196_427962']

    def parse(self, response):
        brand_list = response.xpath('//div[@id="J_ItemList"]')
        divs = brand_list.xpath('div[@class="product"]')
        items = []
        for div in divs:
            item = TopgoodsItem()
            item['GOODS_PRICE'] = div.css('p.productPrice > em::attr(title)').extract_first()
            item['GOODS_NAME'] = div.css('p.productTitle > a::attr(title)').extract_first()
            item['GOODS_URL'] = div.css('p.productTitle > a::attr(href)').extract_first()
            item['SHOP_NAME'] = div.css('div.productShop > a::text').extract_first()
            item['SHOP_URL'] = div.css('div.productShop > a::attr(href)').extract_first()
            item['PRODUCT_SELLED_MONTHLY'] = div.css('p.productStatus > span:nth-child(1) > em::text').extract_first()
            items.append(item)
        return items
