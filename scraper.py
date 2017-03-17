# -*- coding:utf-8 -*-
from __future__ import print_function, unicode_literals

import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver

class Scraper():
    def __init__(self, log_path=os.path.devnull):
        self.driver = webdriver.PhantomJS(service_log_path=log_path)

    def get_soup(self):
        html = self.driver.page_source.encode('utf-8')
        soup = BeautifulSoup(html, 'lxml')
        return soup

    def get(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(3)
        self.soup = self.get_soup()

    def tags(self, name):
        return self.driver.find_elements_by_tag_name(name)

    def classes(self, name):
        return self.driver.find_elements_by_class_name(name)

    def quit(self):
        self.driver.quit()

def main():
    url = 'http://qiita.com'
    scraper = Scraper()
    scraper.get(url)

if __name__=='main':
    main()
