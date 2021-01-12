import scrapy
from ss.items import scooters

class ScooterSpider(scrapy.Spider):
    name = 'scooters'
    start_urls = ['https://www.ss.lv/lv/transport/bycycles/scooters/']

    def parse(self, response):
        # table coloums of all the movies 
        columns = response.css('table[id="page_main"] tr')
        for col in columns:
            # Get the required text from element.
            sludinajums = col.css("td[class='msg2'] a::text,b::text").get()
            if sludinajums:
                sludinajums = col.css("td[class='msg2'] a::text,b::text").get()
                marka = col.css("td[class='msga2-o pp6'] ::text").extract()[0]
                gads = col.css("td[class='msga2-o pp6'] ::text").extract()[2]
                stavoklis = col.css("td[class='msga2-o pp6'] ::text ").extract()[3]
                cena = col.css("td[class='msga2-o pp6'] ::text ").extract()[4]                    
                url = "https://www.ss.lv"+col.css("td[class='msg2'] a::attr(href)").get()
                yield scrapy.Request(url, callback=self.parseDetailItem, meta={'sludinajums' : sludinajums,'marka' : marka,'gads' : gads,'stavoklis' : stavoklis,'cena' : cena,'url' : url})

            next_page = response.css('div.td2 a::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)

    # calls every time, when the movie is fetched from table.
    def parseDetailItem(self, response):
        # create a object of movie.
        item = scooters()
        # fetch the rating meta.
        item["sludinajums"] = response.meta["sludinajums"]
        item["marka"] = response.meta["marka"]
        item["gads"] = response.meta["gads"]
        item["stavoklis"] = response.meta["stavoklis"]
        item["cena"] = response.meta["cena"]
        item["url"] = response.meta["url"]

        # create a list of cast of movie.
        # item["aprikojums"] = list()

        # # fetch all the cast of movie from table except first row.
        # for aprikojums in response.css("td[class='auto_c_column'] b::text").getall():
        #     item["aprikojums"].append(aprikojums)

        # Get the required text from element.
        item['datums'] = response.css("td[class='msg_footer'] ::text")[4].get()
        return item         
        
#scrapy crawl scooters -o scooters.json -t json