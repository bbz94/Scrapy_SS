import scrapy
from ss.items import multivan

class MultivanSpider(scrapy.Spider):
    name = 'multivan'
    start_urls = ['https://www.ss.lv/lv/transport/cars/volkswagen/multivan/']

    def parse(self, response):
        # table coloums of all the movies 
        columns = response.css('table[id="page_main"] tr')
        for col in columns:
            # Get the required text from element.
            sludinajums = col.css("td[class='msg2'] a::text,b::text").get()
            if sludinajums:
                sludinajums = col.css("td[class='msg2'] a::text,b::text").get()
                gads = col.css("td[class='msga2-o pp6'] ::text").extract()[0]
                tilp = col.css("td[class='msga2-o pp6'] ::text").extract()[1]
                cena = col.css("td[class='msga2-o pp6'] ::text ").extract()[2]
                if cena == "-":
                    cena = col.css("td[class='msga2-o pp6'] ::text ").extract()[3]                    
                nobraukums = col.css("td[class='msga2-r pp6'] ::text ").get()
                url = "https://www.ss.lv"+col.css("td[class='msg2'] a::attr(href)").get()
                yield scrapy.Request(url, callback=self.parseDetailItem, meta={'sludinajums' : sludinajums,'gads' : gads,'tilp' : tilp,'cena' : cena,'nobraukums' : nobraukums,'url' : url})

            next_page = response.css('div.td2 a::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)

    # calls every time, when the movie is fetched from table.
    def parseDetailItem(self, response):
        # create a object of movie.
        item = multivan()
        # fetch the rating meta.
        item["sludinajums"] = response.meta["sludinajums"]
        item["gads"] = response.meta["gads"]
        item["tilp"] = response.meta["tilp"]
        item["cena"] = response.meta["cena"]
        item["url"] = response.meta["url"]
        item["nobraukums"] = response.meta["nobraukums"]

        # create a list of cast of movie.
        item["aprikojums"] = list()

        # fetch all the cast of movie from table except first row.
        for aprikojums in response.css("td[class='auto_c_column'] b::text").getall():
            item["aprikojums"].append(aprikojums)

        # Get the required text from element.
        item['datums'] = response.css("td[class='msg_footer'] ::text")[4].get()
        return item         
        
#scrapy crawl multivan -o multivan.json -t json