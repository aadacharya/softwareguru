
import pandas as pd 
from selenium import webdriver
import properties
import json
import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import uuid
import glob
from backend import Product_Data
class Product_Meta_Processor: 
    def __init__(self) -> None:
        self.product_topai_metadata_file = "Unique_Product_Meta.csv"
        product_metadata = self.process_topai_metadata(self.product_topai_metadata_file)
        self.runner(product_metadata)
    def runner(self,product_metadata):
        index = 463
        for counter in range(index,index+500): 
            product_name = product_metadata["product_name"][counter]
            product_website_url = product_metadata["product_url"][counter]
            image_paths = []
            try : 
                product_unique_id = uuid.uuid4()
                response = self.website_request_validator(product_website_url)
                website_extracted_text = None
                list_urls , pricing_page ,affiliate_page = [None] * 3 
                if response : 
                    list_urls, pricing_page , affiliate_page = self.website_home_page_extractor(response)
                    website_extracted_text = self.website_text_extractor(response)
                else: 
                    print ("response not found for " , product_website_url,index)
                    assert False
                if self.get_website_screenshot(product_website_url,f"screenshots/{product_unique_id}_home.png"):
                    image_paths.append(f"screenshots/{product_unique_id}_home.png")
                website_extracted_text_pricing = "" 
                if pricing_page:
                    product_website_pricing_url = product_website_url + pricing_page if "http" not in pricing_page else pricing_page
                    price_response = self.website_request_validator(product_website_pricing_url)
                    if price_response: website_extracted_text_pricing = self.website_text_extractor(price_response)
                    if self.get_website_screenshot(product_website_pricing_url,f"screenshots/{product_unique_id}_pricing.png"):
                        image_paths.append(f"screenshots/{product_unique_id}_pricing.png")
                product_content_json = json.loads(self.generate_product_content(website_extracted_text+website_extracted_text_pricing))
                product_content_json = {key.lower(): value for key, value in product_content_json.items()}
                product_content_json["product_name"] = product_name
                product_content_json["product_unique_id"] = str(product_unique_id)
                product_content_json["product_pricing_available"] = True if pricing_page else None
                product_content_json["product_affiliate_available"] = True if affiliate_page else None
                product_content_json["product_url"] = product_website_url
                self.save_product_content(product_content_json,f"json/{product_unique_id}.json")
                # print(index , product_website_url , len(website_extracted_text) , pricing_page, product_unique_id)
                print("Retrival Success For Index " , counter)
                status = Product_Data().post_product_data(f"json/{product_unique_id}.json",image_paths)
                if not status: assert False
            except Exception as e :  
                print(" >>>>>>>>> Retrival Failed For Index " , counter , e )
                # import json
                failed_data = {}
                with open('failed.json','r') as f : 
                    failed_data = json.load(f)
                failed_data[product_website_url] = counter
                with open('failed.json' , 'w') as f:
                    failed_data = json.dump(failed_data,f)

    def save_product_content(self,product_content_json,filename):
        with open(filename,"w") as f: json.dump(product_content_json,f)
    def process_topai_metadata(self,filename):
        processed_metadata = {}
        return pd.read_csv(filename).to_dict()
    def website_request_validator(self,website_url):
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}   
            response = requests.get(website_url,headers=headers)
            if str(response.status_code).startswith("2") : return response
            else: return None
        except Exception as e : 
            print("Error Logged in website_request_validator " , e )
            return None
    def website_text_extractor(self,response):
        try: 
            soup = BeautifulSoup(response.content,'html.parser')
            return soup.text
        except Exception as e : 
            print("Error Logged in website_text_extractor " , e )
            return None
    def website_home_page_extractor(self,response):
        list_urls , pricing_page , affiliate_page = [None]*3
        soup = BeautifulSoup(response.content,'html.parser')
        list_links = soup.find_all('a', href=True)
        list_urls = [link['href'] for link in list_links]
        for url in list_urls: 
            if "pricing" in url or "price" in url or "plan" in url : pricing_page = url
            if "affiliate" in url : affiliate_page = url
        return list_urls , pricing_page , affiliate_page
    def get_website_screenshot(self,website_url,filename):
        try: 
            options = webdriver.ChromeOptions()
            options.add_argument('--headless') 
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(options=options)
            driver.set_window_size(1920, 1080)
            driver.get(website_url)
            driver.implicitly_wait(20)
            import time 
            time.sleep(5)
            try:
                alert = Alert(driver)
                alert.accept()
                alert.dismiss()
            except: pass 
            time.sleep(5)
            driver.save_screenshot(filename)
            driver.quit()
            return True
        except Exception as e :
            print(f"Unable to take Screen shot for {website_url} \n Exception found {e}")
            return False 
    def generate_product_content(self,extracted_text):
        import properties
        import google.generativeai as genai 
        genai.configure(api_key=properties.gemini_api)
        model = genai.GenerativeModel('gemini-pro')
        prompt = f''' This is the text extracted from a website {extracted_text}  
        \n Give following response in valid json format with keys as product_summary,product_categories,product_pros,product_cons,product_usecases,product_toolfor,product_pricing,product_rating
        \n 1. 100 words summary 
        \n 2. what categoires does the tool falls under give me 5 categories
        \n 3. 5 pros and 5 cons of this tool in list format
        \n 4. 5 use cases with explanation for each, the json keys should be case and details
        \n 5. who is this tool fit for give me 5 with explanation for each , json keys should be target and details
        \n 6. Pricing Information
        \n 7. Rating out of 10 for this product for the information given'''
        response = model.generate_content(prompt)
        answer = response.text
        answer = answer[answer.find("{"):-answer[::-1].find("}")]
        # import json 
        return answer


class Product_Content_Processor:
    def __init__(self) -> None:
        json_files_path =  "json/"
        categorie_json_file = "catergories_json/categories.json"
        toolfor_json_file = "toolfor_json/toolfor.json"
        json_files = self.list_json_files(json_files_path)
        for each_json in json_files: 
            self.gather_categories(each_json,categorie_json_file)
            self.gather_toolfor(each_json,toolfor_json_file)
    def list_json_files(self,json_file_path):
        json_files = None 
        json_files = glob.glob(os.path.join(json_file_path, '*.json'))
        return json_files
    def gather_categories(self,json_file,categorie_json_file):
        with open(categorie_json_file,"r") as f : 
            categorie_json = json.load(f)
        with open(json_file,"r") as f : 
            product_content_json = json.load(f)
        for each_categories in product_content_json["categories"]: 
            if each_categories not in categorie_json : categorie_json[each_categories] = [product_content_json["product_id"]]
            else: categorie_json[each_categories].append(product_content_json["product_id"])
        with open(categorie_json_file,"w") as f : 
            json.dump(categorie_json,f)
    def gather_toolfor(self,json_file,toolfor_json_file):
        with open(toolfor_json_file,"r") as f :
            toolfor_json = json.load(f)
        with open(json_file,"r") as f :
            product_content_json = json.load(f)
        for each_toolfor in product_content_json["toolfor"]: 
            if each_toolfor["target"] not in toolfor_json : toolfor_json[each_toolfor["target"]] = [product_content_json["product_id"]]
            else: toolfor_json[each_toolfor["target"]].append(product_content_json["product_id"])
        with open(toolfor_json_file,"w") as f : 
            json.dump(toolfor_json,f)
        # pass

# Product_Content_Processor()

# import pandas as pd
# df = pd.read_csv("Unique_Product_Meta.csv")
# df["product_url"] = df["product_url"].str.replace('/?via=topaitools','')
# df.to_csv("Unique_Product_Meta.csv")