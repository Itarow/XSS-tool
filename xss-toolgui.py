#!/usr/bin/python3
from dearpygui import core, simple
from XSSFilterBypass.PayloadCrafter import PayloadCrafter
from XSSFilterBypass.GUI import PayloadCrafterGUI
from Crawler.GUI import CrawlerGUI
from Sender import GUI


def summonPCGUI(sender, data):
    pcGUI = PayloadCrafterGUI()
        
def summonSenderGUI(sender, senderGUI):
    if not senderGUI.is_summoned():
        senderGUI.summon()
    else:
        print('[~] SenderGUI has arlready been summoned.')

def summonCrawlerGUI(sender, data):
    crawlerGUI = CrawlerGUI()
        
def main(sender):
    with simple.window("Select what you want to do"):
        core.add_text("H3110 W0r1d!")
        core.add_button("Craft Payloads", callback=summonPCGUI)
        core.add_button("Send Payload", callback=summonSenderGUI, callback_data=senderGUI)
        core.add_button("Crawl website", callback=summonCrawlerGUI)
    core.set_main_window_size(800, 800)
    core.start_dearpygui()   

if __name__ == '__main__':
    senderGUI = GUI.SenderGUI()
    main(senderGUI)
