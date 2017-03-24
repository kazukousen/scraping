# -*- coding:utf-8 -*-
from __future__ import print_function, unicode_literals

import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver

class Scraper():
    def __init__(self, user_agent=None, log_path=os.path.devnull):
        if user_agent:
            from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
            dcap = dict(DesiredCapabilities.PHANTOMJS)
            dcap["phantomjs.page.settings.userAgent"] = (user_agent)
            self.driver = webdriver.PhantomJS(desired_capabilities=dcap, service_log_path=log_path)
        else:
            self.driver = webdriver.PhantomJS(service_log_path=log_path)

    def get_soup(self):
        html = self.driver.page_source.encode('utf-8')
        soup = BeautifulSoup(html, 'lxml')
        return soup

    def reload(self):
        self.get(self.driver.current_url)

    def get(self, url):
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        self.soup = self.get_soup()

    def tags(self, name):
        return self.driver.find_elements_by_tag_name(name)

    def ids(self, name):
        return self.driver.find_elements_by_id(name)

    def names(self, name):
        return self.driver.find_elements_by_name(name)

    def classes(self, name):
        return self.driver.find_elements_by_class_name(name)

    def set_keys(self, obj, value):
        obj.send_keys(value)
        return value == obj.get_attribute('value')

    def quit(self):
        self.driver.quit()

def get_iphone_user():
    return 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML,like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5'

def get_android_user():
    return 'Mozilla/5.0 (Linux; U; Android 2.3.3; ja-jp; INFOBAR A01 Build/S7142) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'

def main():
    url = 'http://qiita.com'
    scraper = Scraper()
    scraper.get(url)

if __name__=='main':
    main()
