from scrapy import Item,Field,Spider

class News(Item):
   link = Field()
   manchete = Field()

class JNprecisadeTalco(Spider):
   name="JN_Precisa_de_Talco_para_Sobreviver"
   start_urls = ['https://jovemnerd.com.br/']
   #parse method
   def parse(self,response):
      for info in response.css('article.entry-card.entry-card__nerdnews  .entry-card__content  .entry-card__content-title a'):
         jornal = News()
         jornal['link'] = info.css('a').xpath('@href').extract()
         jornal['manchete'] = info.css('a::text').extract()
         yield jornal
