# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
import json

class mySpider(scrapy.Spider):
    name ="tutsplus"


    start_urls = ["https://code.tutsplus.com/tutorials"]
    #i=0
    M=10
    for i in range(M):
        i=i+2
        domain_url='https://tutsplus.com/tutorials?page='+str(i)
        start_urls.append(domain_url)
    print(start_urls)

    def parse(self, response):
        externalLinks = response.css("article header a.posts__post-title::attr(href)")
        for link in externalLinks:
            yield response.follow(link, self.parse_page)

    def parse_page(self, response):
        # auther= response.xpath("/html/body/div[2]/main/article/div[1]/div[1]/div[1]/div[1]/span")
        #length = response.xpath("/html/body/div[3]/main/article/div[1]/div[1]/div[1]/div[2]/span[2]/span[2]/text()")
        title = response.xpath("/html/body/div[3]/main/div[1]/div/div[2]/h1/text()")

        author=response.xpath('//span[@class="content-heading__author-name"]//text()').extract()
        length=response.xpath('//span[@class="content-heading__value"]//text()')
        published_date=response.xpath('//time//text()')
        language = response.xpath('//span[@class="content-heading__value url-selector view view--loaded"]//text()')
        #print(i+1)
        # print(auther)
        print(title)
        print(author)
        print(length)
        print(published_date)
        #print(language)
        print("================================================================================")
