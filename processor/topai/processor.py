import pandas as pd 
from selenium import webdriver
import properties
import json
import os
class Processor:
    def __init__(self) -> None:
        self.json_file_path = [properties.categories_data_filepath,properties.usecase_data_filepath]
        self.data_frame = self.get_dataframe(self.json_file_path)
        text , urls = self.extract_website_text()
        gemini_response = self.get_gemini_reponse(text)
        # self.extract_website()
        # self.check_product_url()
    def get_dataframe(self,json_filepaths):
        data = []
        for eachpath in json_filepaths:
            filelist = os.listdir(eachpath)
            for eachfile in filelist:
                if eachfile.endswith(".json"): 
                    with open(f"{eachpath}/{eachfile}","r") as f : data+=json.load(f)["data"]
        dataframe = pd.DataFrame(list({frozenset(item.items()): item for item in data}.values()))
        dataframe.to_csv("Unique_Product_Meta.csv")
        print(dataframe.shape,dataframe.columns)
        print(dataframe.head)
        return dataframe
    def check_product_url(self):
        count = 0 
        for index, row in self.data_frame.iterrows():
            import requests
            res = requests.get(row["product_url"])
            print(index,count)
            if str(res.status_code).startswith("2"): count +=1 
        print (count)
        return count
    def extract_website_text(self):
        from bs4 import BeautifulSoup
        import requests
        for i in range(3):
            url = self.data_frame.iloc[i]["product_url"]
            url = url.split("?")[0]
            res = requests.get(url)
            text, urls = None , None
            if str(res.status_code).startswith("2"):
                soup = BeautifulSoup(res.content, 'html.parser')
                text = soup.get_text()
                links = soup.find_all('a', href=True)
                urls = [link['href'] for link in links]
            return text , urls
                # print(url , len(urls), len(text))
    def get_gemini_reponse(self):
        import google.generativeai as genai 
        genai.configure(api_key=properties.gemini_api)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("https://topai.tools/")
        return response.text
    def get_screenshot(self,url,path):
        try: 
            from selenium import webdriver
            from selenium.webdriver.chrome.service import Service
            from selenium.webdriver.common.by import By
            options = webdriver.ChromeOptions()
            options.add_argument('--headless') 
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(options=options)
            driver.set_window_size(1920, 1080)
            driver.get(url)
            driver.implicitly_wait(10)
            driver.save_screenshot(path)
            driver.quit()
            return True
        except Exception as e : 
            raise SystemError(f"Unable to take Screen shot for {url} \n Exception found {e}")

        pass
pro = Processor()
# res = pro.get_gemini_reponse()
# print(res)