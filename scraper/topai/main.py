from scrap import ScrapProduct_Categories

import json

from selenium import webdriver

# categories_json = {}
# with open ("categories.json","r") as f : 
#     categories_json = json.load(f)
# categories_data = categories_json["data"]
# index = 5
# for i in range(index,len(categories_data)):
#     each = categories_data[i]
#     print (each , i)
#     scrapper = ScrapProduct_Categories(each["categorie"],each["href"]).scrap()

# from scrap import ScrapProduct_UseCases
# usecase_json = {}
# with open ("usecase.json","r") as f : 
#     usecase_json = json.load(f)
# usecase_data = usecase_json["data"]
# index = 154
# for i in range(index,len(usecase_data)):
#     each = usecase_data[i]
#     print (each , i)
#     scrapper = ScrapProduct_UseCases(each["usecase"],each["href"]).scrap()

# indexes = [310,311,312,232,115] # usecase to be extracted
# for i in indexes: 
#     each = usecase_data[i]
#     print (each , i)
#     scrapper = ScrapProduct_UseCases(each["usecase"],each["href"]).scrap()

