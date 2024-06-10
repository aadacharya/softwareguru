import requests
from bs4 import BeautifulSoup

class Extractor: 
    def __init__(self,website_url) -> None:
        self.website_url = website_url
        self.pricing = None 
        self.affiliate = None
        pass
    def check_website(self):
        res = requests.get(self.website_url)
        if str(res.status_code).startswith("2") : return res 
        return False
    def get_valid_urls(self,soup):
        valid_urls = None
        links = soup.find_all('a', href=True)
        urls = [link['href'] for link in links]
        for each_url in urls : 
            if "pricing" in each_url or "plans" in each_url: self.pricing = each_url
            if "affiliate" in each_url: self.affiliate = each_url
        return valid_urls
    def get_website_information(self):
        soup,extracted_text = None, None
        response = self.check_website()
        if response: 
            soup = BeautifulSoup(response.content,'html.parser')
        if soup : extracted_text = soup.get_text()
        valid_urls = self.get_valid_urls()

        summary,categories,pricing,usecase,procon,toolfor,affiliation = [None]*6    

        information = [summary,categories,pricing,usecase,procon,toolfor]
        
        affiliation = True if self.affiliate else False
        return information , affiliation


        