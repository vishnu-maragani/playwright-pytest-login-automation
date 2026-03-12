

import json

from playwright.sync_api import Page


class URL:
    def __init__(self,page:Page):
        self.page = page
        self.url = "https://rahulshettyacademy.com/client/#/auth/login"
    def page_url(self):
        self.page.goto(self.url,timeout=60000)
        
def get_credentials():
    filePath = "test_data/login_credentials.json"
    with open(filePath,'r') as file:
        return json.load(file)