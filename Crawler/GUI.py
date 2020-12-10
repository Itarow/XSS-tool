from dearpygui import core, simple

from Crawler.Crawler import Crawler


class CrawlerGUI:
    def __init__(self):
        with simple.window("Crawler"):
            core.add_text("Welcome to the crawler.")
            core.add_input_text("Select a target url", source="target")
            core.add_button("Crawl", callback=self.startCrawling)
        
    def startCrawling(self, sender, data):
        data = core.get_value("target")
        if "http" in str(data):
            crawler = Crawler(data)
        else:
            with simple.window("Crawler"):
                core.add_text("Please enter a url", color=(255, 0, 0))