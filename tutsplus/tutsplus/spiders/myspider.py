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
        pageName = response.url.split("/")[-1]
        filename = 'page-%s.json' % pageName

        pageFile = {}


        pageFile["fileName"] =  pageName.strip()
        pageFile["title"] = response.xpath("/html/body/div[2]/main/div[1]/div/div[2]/h1/text()").extract()
        pageFile["author"] = response.xpath('//span[@class="content-heading__author-name"]//text()').extract()
        pageFile["auther_details"] = response.xpath("/html/body/div[2]/main/article/div[2]/div[4]/a/div[1]/div[2]/text()").extract()
        pageFile["length"] = response.xpath('//span[@class="content-heading__value"]//text()').extract()
        pageFile["body"] = response.xpath("/html/body/div[2]/main/article/div[2]/div[2]/div/div/p//text()").extract().strip()
        pageFile["pubished_date"]= response.xpath('//time//text()').extract()

        title = response.xpath("/html/body/div[2]/main/div[1]/div/div[2]/h1/text()").extract()
        author=response.xpath('//span[@class="content-heading__author-name"]//text()').extract()
        auther_details=response.xpath("/html/body/div[2]/main/article/div[2]/div[4]/a/div[1]/div[2]/text()").extract()
        length=response.xpath('//span[@class="content-heading__value"]//text()').extract()
        published_date=response.xpath('//time//text()').extract()
        #language = response.xpath('//span[@class="content-heading__value url-selector view view--loaded"]//text()')
        b=response.xpath("/html/body/div[2]/main/article/div[2]/div[2]/div/div/p[3]").extract()[0]
        #print(i+1)
        print(auther_details)
        print(title)
        print(author)
        print(length)
        print(published_date)
        #print(language)
        print(b)
        print("================================================================================")



        with open(filename, 'w+') as f:
            json_data = json.dumps(pageFile)
            f.write((json_data))
        self.log('Saved file %s' % filename)