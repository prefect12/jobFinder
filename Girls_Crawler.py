from bs4 import BeautifulSoup
from urllib.request import urlopen,urlretrieve
import re
import urllib.parse
import hashlib

class down_pic():
    def __init__(self):
        self.down_loaded = []
        self.header = [('Host', 'www.meizitu.com'),
                   ('Connection', 'keep-alive'),
                   ('Cache-Control', 'max-age=0'),
                   ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'),
                   ('User-Agent',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'),
                   ('Accept-Encoding', 'gzip,deflate,sdch'),
                   ('Accept-Language', 'zh-CN,zh;q=0.8'),
                   ('If-None-Match', '60644ed24a82d31:104f'),
                   ('Referer','http://www.meizitu.com/a/sexy_8.html'),
                   ('If-Modified-Since', 'Sun, 31 Dec 2017 15:19:59 GMT')]
        self.md5 = hashlib.md5()

    def get_page(self,root_page):
        pages = []
        soup = self.get_soup(root_page)
        links = soup.find('div',id="wp_page_numbers").find_all('a')
        for link in links:
            pages.append(link['href'])
        return pages

    def get_sub_page(self,page):
        sub_page = []
        soup = self.get_soup(page).find('ul',class_="wp-list clearfix")
        links = soup.find_all('a',href = re.compile(r"/a/[1-9]\d*"))
        for link in links:
            sub_page.append(link['href'])
        return sub_page

    def get_new_urls(self,soup):
        new_urls = []
        links = soup.find('div',id = 'picture').find_all('img')
        print(links)
        for link in links:
            new_urls.append(link['src'])
        return new_urls

    def get_soup(self,root_url):
        headers = self.header
        opener = urllib.request.build_opener()
        opener.addheaders = headers
        url_open = opener.open(root_url,timeout=5000)
        soup = BeautifulSoup(url_open, 'html5lib')
        return soup

    def down_loar(self,urls):
        headers = self.header
        for url in urls:
            try:
                if url not in self.down_loaded:
                    opener = urllib.request.build_opener()
                    opener.addheaders = headers
                    data = opener.open(url,timeout=5000)
                    self.md5.update(str(url).encode("utf8"))
                    path = "F:\\temp\\%s.jpg"%(str(self.md5.hexdigest()))
                    self.down_loaded.append(url)
                    f = open(path, "wb")
                    f.write(data.read())
                    print(url)
                    f.close()
            except Exception as e:
                print(e)

def main():
    sub_page = []
    for i in range(10,33):
        root_url = "http://www.meizitu.com/a/sexy_"+str(i)+".html"
        download = down_pic()
        page = download.get_sub_page(root_url)
        for i in page:
            if i not in sub_page:
                sub_page.append(i)

    for n in sub_page:

        try:
            new_urls = download.get_new_urls(download.get_soup(n))
            download.down_loar(new_urls)

        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
