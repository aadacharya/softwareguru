import properties
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class ScrapUseCases:
    def __init__(self) -> None:
        self.usecase_url = properties.usecase_url
    def scrap(self):
        data = self.scrap_usecases()
        self.save_data(data,"usecase.json")
    def scrap_usecases(self):
        driver = webdriver.Chrome()
        driver.get(self.usecase_url)
        time.sleep(2)
        data = {"type":"usercases","data":[]}
        try : 
            gpt_cards = driver.find_elements(By.CSS_SELECTOR, 'div.gpt-card.my-1.col-md-4')
            # print("############# ",len(gpt_cards))
            for card in gpt_cards:
                anchor = card.find_element(By.TAG_NAME, 'a')
                text = anchor.text
                href = anchor.get_attribute('href')
                data['data'].append({"usecase":text,"href":href})
            return data
        except: 
            return False

    def save_data(self,data,filename):
        import json
        try : 
            with open(filename,'w') as f : 
                json.dump(data,f)
            return True
        except:
            return False

class ScrapCategories:
    def __init__(self) -> None:
        self.categories_url = properties.categories_url
    def scrap(self):
        data = self.scrap_categories()
        self.save_data(data,"categories.json")
    def scrap_categories(self):
        data = {"type":"categories","data":[]}
        driver = webdriver.Chrome()
        driver.get(self.categories_url)
        time.sleep(2)
        try : 
            gpt_cards = driver.find_elements(By.CSS_SELECTOR, 'div.gpt-card.my-1.col-md-4')
            for card in gpt_cards:
                anchor = card.find_element(By.TAG_NAME, 'a')
                text = anchor.text
                href = anchor.get_attribute('href')
                data['data'].append({"categorie":text,"href":href})
            return data
        except: 
            return False
    def save_data(self,data,filename):
        import json
        with open(filename,"w") as f:
            json.dump(data,f)

class ScrapProduct_Categories:
    def __init__(self,categories,categories_url) -> None:
        self.url = categories_url
        self.categories  = categories 
    def scrap(self): 
        status, data = True , {"type":"productmeta","data":[]}
        index = 1
        while status: 
            url = self.url + f"&p={index}"
            status, data = self.scrap_product_data(data,url)
            index += 1 
        self.save_data(data,f"categories_data/{self.categories }.json")
        print ( " ************ " , self.categories , len(data["data"]))
    def scrap_product_data(self,data,url):   
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(2)
        try:
            product_divs = driver.find_elements(By.CSS_SELECTOR, 'div.mt-1.d-flex.flex-wrap')
            if not product_divs : 
                # print ("### Returning as no prod_divs" , len(data["data"]))
                return False , data
            # print ("##### Found" , len(product_divs))
            for div in product_divs:
                h2_tag = div.find_element(By.TAG_NAME, 'h2')
                anchors = h2_tag.find_elements(By.TAG_NAME, 'a')
                try: topai_url = anchors[0].get_attribute('href')
                except: topai_url = None
                try: product_name = anchors[0].text
                except : product_name = None
                try: product_url = anchors[1].get_attribute('href')
                except: product_url = None
                if product_name: data["data"].append({"product_name":product_name,"topai_url":topai_url,"product_url":product_url})
            # print ("### Returning " , len(data["data"]))
            return True, data
        except Exception as e: 
            return False , data
    def save_data(self,data,filename):
        import json
        with open(filename,"w") as f : 
            json.dump(data,f)
        

class ScrapProduct_UseCases:
    def __init__(self,usecase,usecase_url) -> None:
        self.url = usecase_url
        self.usecase  = usecase 
    def scrap(self): 
        status, data = True , {"type":"productmeta","data":[]}
        index = 1
        while status: 
            # url = self.url + f"&p={index}"
            url = self.url 
            status, data = self.scrap_product_data(data,url)
            index += 1 
        self.save_data(data,f"use_case_data/{self.usecase }.json")
        print ( " ************ " , self.usecase , len(data["data"]))
    def scrap_product_data(self,data,url):   
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(2)
        try:
            product_divs = driver.find_elements(By.CSS_SELECTOR, 'div.mt-1.d-flex.flex-wrap')
            if not product_divs : 
                # print ("### Returning as no prod_divs" , len(data["data"]))
                return False , data
            # print ("##### Found" , len(product_divs))
            for div in product_divs:
                h2_tag = div.find_element(By.TAG_NAME, 'h2')
                anchors = h2_tag.find_elements(By.TAG_NAME, 'a')
                try: topai_url = anchors[0].get_attribute('href')
                except: topai_url = None
                try: product_name = anchors[0].text
                except : product_name = None
                try: product_url = anchors[1].get_attribute('href')
                except: product_url = None
                if product_name: data["data"].append({"product_name":product_name,"topai_url":topai_url,"product_url":product_url})
            # print ("### Returning " , len(data["data"]))
            return False, data
        except Exception as e: 
            return False , data
    def save_data(self,data,filename):
        import json
        with open(filename,"w") as f : 
            json.dump(data,f)
        
# scrapper = ScrapProduct_UseCases("test","https://topai.tools/usecases/human-resources").scrap()