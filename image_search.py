from icrawler.examples import GoogleImageCrawler
from icrawler.examples import BingImageCrawler
from icrawler.examples import BaiduImageCrawler


a = input("Enter search keyword")

google_crawler = GoogleImageCrawler('./save/')
google_crawler.crawl(keyword=a, offset=0, max_num=10,
                     date_min=None, date_max=None, feeder_thr_num=1,
                     parser_thr_num=1, downloader_thr_num=4,
                     min_size=(200,200), max_size=None)
bing_crawler = BingImageCrawler('./save/')
bing_crawler.crawl(keyword=a, offset=0, max_num=10,
                   feeder_thr_num=1, parser_thr_num=1, downloader_thr_num=4,
                   min_size=None, max_size=None)
baidu_crawler = BaiduImageCrawler('./save/')
baidu_crawler.crawl(keyword=a, offset=0, max_num=10,
                    feeder_thr_num=1, parser_thr_num=1, downloader_thr_num=4,
                    min_size=None, max_size=None)