import os
from bardapi import Bard
import requests

class AskBard:
    def __init__(self, api_key):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers = {
                    "Host": "bard.google.com",
                    "X-Same-Domain": "1",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
                    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                    "Origin": "https://bard.google.com",
                    "Referer": "https://bard.google.com/",
                }
        self.timeout = 300
        self.session.cookies.set("__Secure-1PSID", self.api_key) 
        self.bard =  Bard(token = self.api_key, session = self.session, timeout = self.timeout)
    def ask(self, prompt):
        response = self.bard.get_answer(prompt)["content"]
        return response