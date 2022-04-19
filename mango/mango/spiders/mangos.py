# -*- coding: utf-8 -*-
import json

import jsonpath
import scrapy
import time
import re
from lxml import etree
import copy
# http://rsj.hefei.gov.cn/zxzx/tzgg/index.html

class WjSpider(scrapy.Spider):
    name = '221'
    allowed_domains = ['rsj.hefei.gov.cn']
    # start_urls = ['']

    def start_requests(self):
        cate = [
            'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjIwfQ==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjQwfQ==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjYwfQ==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjgwfQ==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjEwMH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjEyMH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjE0MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjE2MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjE4MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjIwMH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjIyMH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjI0MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjI2MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjI4MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjMwMH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjMyMH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjM0MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjM2MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjM4MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjQwMH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjQyMH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjQ0MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjQ2MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjQ4MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjUwMH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjUyMH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjU0MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjU2MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjU4MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjYwMH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjYyMH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjY0MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjY2MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjY4MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjcwMH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjcyMH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjc0MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjc2MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjgwMH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjc4MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjgyMH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjg0MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjg2MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjg4MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjkwMH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjkyMH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjk0MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjk2MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjk4MH0==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjEwMDB9==',
            # 'eyJ2IjoiNzAzMTQxMTA4MTQ1NzMzNjM1NyIsImkiOjEwMjB9==',
        ]

        for i in cate:
        #循环135页
        #构建post请求参数
            data = {"id_type":2,"sort_type":200,"cate_id":"6809635626879549454","tag_id":"6809640400832167949","cursor":i,"limit":20}
        #发送post请求
            yield scrapy.FormRequest(
                url = 'https://api.juejin.cn/recommend_api/v1/article/recommend_cate_tag_feed?aid=2608&uuid=7003543927303341582',
                method='POST',
                body=json.dumps(data),
                headers={'Content-Type': 'application/json'},
                callback = self.parse)

    def parse(self, response):
        item1 = {}

        text = json.loads(response.text)
        article_id = jsonpath.jsonpath(text, '$..article_info.article_id')
        coverImgUrl  = jsonpath.jsonpath(text, '$..article_info.cover_image')
        articleTitle = jsonpath.jsonpath(text, '$..article_info.title')
        articleDesc = jsonpath.jsonpath(text, '$..article_info.brief_content')

        for article_id, coverImgUrl, articleTitle, articleDesc in zip(article_id,coverImgUrl,articleTitle,articleDesc):
            item1['contentUrl'] = 'https://juejin.cn/post/'+article_id
            item1['coverImgUrl'] = coverImgUrl
            item1['articleTitle'] = articleTitle
            item1['articleDesc'] = articleDesc

            # print(item['contentUrl'],item['coverImgUrl'],item['articleTitle'],item['articleDesc'])

            yield scrapy.Request(item1['contentUrl'], callback=self.parse_info, meta={'item1': copy.deepcopy(item1)},dont_filter=True)
    #
    def parse_info(self, response):
        item1= response.meta['item1']
        item1['contentHtml'] = re.findall('.+mark_content:([\s\S.]+),author_user_info', response.text)[0]
        # CONTENT=CONTENT[0]
        item1["userName"] ='shi.zy'
        item1['userPassword'] ='12345678ss'
        item = {}
        item['body'] = json.dumps(item1, ensure_ascii=False)

        item['appId'] ='string'
        item['clientType'] ='string'
        item['timestamp'] ='string'
        item['token'] ='string'
        item['userId'] ='string'
        item['version'] ='string'


        yield item


