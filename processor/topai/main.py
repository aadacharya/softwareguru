import requests
from bs4 import BeautifulSoup
url = 'https://photes.io/'
response = requests.get(url)
text,urls = None,None
response.status_code
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    links = soup.find_all('a', href=True)
    urls = [link['href'] for link in links]
import properties
import google.generativeai as genai 
genai.configure(api_key=properties.gemini_api)
model = genai.GenerativeModel('gemini-pro')
prompt = f''' This is the text extracted from a website {text}  
\n Give following response in valid json format with keys as summary,categories,pro,cons,usecase,toolfor
\n 1. 100 words summary 
\n 2. what categoires does the tool falls under give me 5 categories
\n 3. 5 pros and 5 cons of this tool in list format
\n 4. 5 use cases with explanation for each , the json keys should be case and details
\n 5. who is this tool fit for give me 5 with explanation for each , json keys should be target and details'''
response = model.generate_content(prompt)
answer = response.text
answer = answer[answer.find("{"):-answer[::-1].find("}")]
import json 
value = json.loads(answer)
with open("test1.json","w") as f : json.dump(value,f)
