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


class TmGoodsSpider(scrapy.Spider):
    name = "tm_goods"
    allowed_domains = ["http://www.tmall.com"]
    start_urls = (
        'http://list.tmall.com/search_product.htm?type=pc&totalPage=100&cat=50025135&sort=d&style=g&from=sn_1_cat-qp&active=1&jumpto=10#J_Filter',
    )
    # 记录处理的页数
    count = 0

    def parse(self, response):

        TmGoodsSpider.count += 1

        divs = response.xpath("//div[@id='J_ItemList']/div[@class='product']/div")
        if not divs:
            self.log("List Page error--%s" % response.url)

        for div in divs:
            item = TopgoodsItem()
            # 商品价格
            item["GOODS_PRICE"] = div.xpath("p[@class='productPrice']/em/@title")[0].extract()
            # 商品名称
            item["GOODS_NAME"] = div.xpath("p[@class='productTitle']/a/@title")[0].extract()
            # 商品连接
            pre_goods_url = div.xpath("p[@class='productTitle']/a/@href")[0].extract()
            item["GOODS_URL"] = pre_goods_url if "http:" in pre_goods_url else ("http:" + pre_goods_url)

            yield scrapy.Request(url=item["GOODS_URL"], meta={'item': item}, callback=self.parse_detail,
                                 dont_filter=True)

    def parse_detail(self, response):

        div = response.xpath('//div[@class="extend"]/ul')
        if not div:
            self.log("Detail Page error--%s" % response.url)

        item = response.meta['item']
        div = div[0]
        # 店铺名称
        item["SHOP_NAME"] = div.xpath("li[1]/div/a/text()")[0].extract()
        # 店铺连接
        item["SHOP_URL"] = div.xpath("li[1]/div/a/@href")[0].extract()
        # 公司名称
        item["COMPANY_NAME"] = div.xpath("li[3]/div/text()")[0].extract().strip()
        # 公司所在地
        item["COMPANY_ADDRESS"] = div.xpath("li[4]/div/text()")[0].extract().strip()

        yield item
