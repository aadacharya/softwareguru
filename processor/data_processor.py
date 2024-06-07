import pandas as pd 
import properties
raw_data_df = pd.read_csv("directoryjson.csv")
# raw_data_df.columns

import google.generativeai as genai 
genai.configure(api_key=properties.gemini_api)
model = genai.GenerativeModel('gemini-pro')

prompt = ''' I will give you a json input where the key is the product name and the value is product about \n
your task is to \n 
1. Completely rewrite each of the product about for avoiding palgarism check. Please rephrase and add remove \n
or additional details to make it distinct from the original text. \n
2. Each of the rewriten product about should be exactly 300 words \n
Finally, return the response in the given json format. \n
Json Format: {"product_name": "About the Product"} \n 
'''
# 3. If the original product about is null then write your own product about of 100 words \n 
content_json ={}
for each in range(25):
    product = raw_data_df.iloc[each]
    content_json[product["PRODUCT_NAME"]] = product["ABOUT"]
import json
response = model.generate_content(prompt + json.dumps(content_json))
response.text
response_json = json.loads(response.text)
for each in response_json: 
  if each not in content_json: print (each)
len(response_json.keys())
content_json

import uuid 
uuid.uuid4()

import requests
image_url = "https://example.com/image.jpg"
response = requests.get(image_url)
if response.status_code == 200:
    with open("image.jpg", "wb") as f:
        f.write(response.content)
    print("Image downloaded successfully")
else:
    print("Failed to download image:", response.status_code)