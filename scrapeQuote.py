import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'myQuotes'
    start_urls = ['https://solve-programming.blogspot.com/']
    ##========================================= Crawling Title Only ==========================================
    ##def parse(self, response):
        ##title = response.css('title::text').extract
        ##yield {
            ##'titletext' : title
        ##}
    ##========================================= Crawling Post Title and Image Only ==========================================
    def parse(self, response):
        SET_SELECTOR = '.post.hentry'
        for titlepageh2loop in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'a::text'
            IMAGE_SELECTOR = 'img.post-thumbnail'
            yield {
                'TITLE' : titlepageh2loop.css(NAME_SELECTOR).extract(),
                'IMAGE' : titlepageh2loop.css(IMAGE_SELECTOR).extract(),
            }

