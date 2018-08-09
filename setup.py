from setuptools import setup, find_packages

class DmozSpider(BaseSpider):
    name = "preppersshop"
    allowed_domains = ["preppersshop.co.uk"]
    f = open("urls.txt")
    start_urls = [url.strip() for url in f.readlines()]
    f.close()

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)

setup(
    name         = 'project',
    version      = '1.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = A337311.settings']},
)
