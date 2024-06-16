import requests
import properties
import json

class Product_Data():
    def __init__(self) -> None:
        self.backend_url = properties.backend_url
        self.upload_product_data_url = properties.upload_product_data
        self.delete_product_data_url = properties.delete_product_data
        self.csfr_token_url = properties.get_csfr_token
        pass
    def post_product_data(self,product_json_data):
        url = self.backend_url + self.upload_product_data_url
        csrf_url = self.backend_url + self.csfr_token_url
        session = requests.Session()
        session.get(csrf_url)
        csfr_token = session.cookies['csrftoken'] 
        headers = {
                'Content-Type': 'application/json',
                'X-CSRFToken': csfr_token
            }
        response = session.post(url,json=product_json_data,headers=headers)
        print ("Response for product data post",response.text)
        pass
    def delete_product_data(self):
        pass


class Product_Image_Data():
    def __init__(self) -> None:
        pass
    def post_product_image(self):
        pass
    def delete_product_image(self):
        pass

def load_json_data(json_file):
    import json
    product_json_data = None
    with open(json_file,"r") as f: 
        product_json_data = json.load(f)
    if not product_json_data : raise BaseException("Product Json Data cannot be read " , json_file)
    return product_json_data
def validate_json_data(product_json_data):
    product_fields = ["product_summary","product_categories","product_pros","product_cons","product_usecases","product_toolfor","product_pricing","product_rating","product_name","product_unique_id","product_pricing_available","product_affiliate_available","product_url"]
    for each_field in product_fields:
        if each_field not in product_json_data: raise BaseException("Product Json not in Format ", each_field )  
    if not isinstance(product_json_data["product_pricing"],dict) or not isinstance(product_json_data["product_pricing"],list) : product_json_data["product_pricing"] = [product_json_data["product_pricing"]]
    return True

# product_json_data
json_file = "json/ad1e3b00-63eb-4415-b702-96a87adf6489.json"
producut_json_data = load_json_data(json_file)
validate_json_data(producut_json_data)

product_post = Product_Data()
product_post.post_product_data(producut_json_data)

# res = requests.get("http://127.0.0.1:8000/softwareguru")
# res = requests.get(properties.backend_url)
# properties.backend_url+properties.upload_product_data
# import uuid
# str(uuid.uuid4())