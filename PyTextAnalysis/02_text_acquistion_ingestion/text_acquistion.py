import bs4
import requests
from multiprocessing.dummy import Pool
from slugify import slugify

sources = ['https://www.wahsingtonpost.com',
           'http://www.nytimes.com/',
           'http://www.chicagotribune.com/',
           'http://www.bostonherald.com/',
           'http://www.sfchronicle.com/']
TAGS = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'p', 'li']

def crawl(url):
    domain = url.split('//www.')[-1].split('/')[0]
    html = requests.get(url).content
    soup = bs4.BeautifulSoup(html, 'lxml')
    links = set(soup.find_all('a', href=True))

    for link in links:
        sub_url = link['href']
        page_name = link.string

        if domain in sub_url:
            try:
                page = requests.get(sub_url).content
                filename = slugify(page_name).lower() + '.html'
                with open(filename, 'wb') as f:
                    f.write(page)
            except:
                pass


def multiproc_crawl(url_list, processes=2):
    pool = pool(processes)
    pool.map(crawl, url_list)
    pool.close()
    pool.join()


def html2text(path):
    with open(path, 'r') as f:
        html = f.read()
        soup = bs4.BeautifulSoup(html, 'lxml')
        for tag in soup.find_all(TAGS):
            yield tag.get_text()
    

if __name__ == '__main__':
    for url in sources:
        #crawl(url)
        multiproc_crawl(sources, 4)
