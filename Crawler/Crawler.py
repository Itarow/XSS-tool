from bs4 import BeautifulSoup
import requests
import threading

class Crawler:
    def __init__(self, url):
        if not url.startswith("http://") and not url.startswith("https://"):
            print("It seems that http:// is not present in the url you typed.")
        else:
            self.url = url
            self.visited = [self.url]
            self.toVisit = []
            self.contain_form = []
            self.crawl(url)

    def crawl(self, url):
        with open('logs.txt', 'a') as f:
            f.write(f"[~] Visited url: {url}\n")
        site = requests.get(url)
        form_finder = threading.Thread(target=self.check_forms, args=(url,))
        soup = BeautifulSoup(site.text, 'lxml')
        links = []

        for link in soup.findAll('a'):
            links.append(link.get('href'))
        for link in soup.findAll('link'):
            links.append(link.get('href'))
            
        for link in links:
            if str(link).startswith('.'):
                self.toVisit.append(self.url + link[1:])   
            elif str(link).startswith('?'):
                self.toVisit.append(self.url + link)
            elif str(link).startswith('/'):
                url = self.url.split('/')[0] + '//' + self.url.split('/')[2] 
                self.toVisit.append(url + link)
            elif str(link).startswith('http'):
                url = link
                self.toVisit.append(url)
        
        for link in self.toVisit:
            if not link in self.visited and not link == self.url and "http" in link:
                self.visited.append(link)
                thread = threading.Thread(target=self.crawl, args=(link,))
                thread.start()
    
    def check_forms(self, url):
        try:
           r = requests.get(url)
           if 'form' in r.text:
               self.contain_form.append(url)
        except:
            print('[~] URL is invalid.')

    def get_crawled(self):
        return self.visited
