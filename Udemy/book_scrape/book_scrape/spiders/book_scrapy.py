import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = [
        http://books.toscrape.com/
    ]

#     def start_requests(self): # the method name is required, not user-defined
#         return [
#             scrapy.Request(url = "http://books.toscrape.com/", callback = self.parse)
#         ]

    def parse(self, response):
        with open("books.html", "wb") as file:
            file.write(response.body)
