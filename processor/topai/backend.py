import requests
import properties
import json

class Product_Data():
    def __init__(self) -> None:
        self.backend_url = properties.backend_url
        self.upload_product_data_url = properties.upload_product_data
        self.delete_product_data_url = properties.delete_product_data
        self.csfr_token_url = properties.get_csfr_token
        self.product_json_helper = Product_Json_Helper()
        pass
    def post_product_data(self,json_file_path,image_paths):
        product_json_data = self.product_json_helper.load_json_data(json_file_path)
        url = self.backend_url + self.upload_product_data_url
        csrf_url = self.backend_url + self.csfr_token_url
        session = requests.Session()
        session.get(csrf_url)
        csrf_token = session.cookies['csrftoken'] 
        headers = {
                'X-CSRFToken': csrf_token  # CSRF token for security
            }
        files = []
        for i, image_path in enumerate(image_paths):
            files.append(('form-{}-image'.format(i), (open(image_path, 'rb'))))
            files.append(('form-{}-caption'.format(i), (None, 'Caption for image {}'.format(i))))
        files += [
            ('form-TOTAL_FORMS', (None, len(image_paths))),
            ('form-INITIAL_FORMS', (None, '0')),
            ('form-MIN_NUM_FORMS', (None, '0')),
            ('form-MAX_NUM_FORMS', (None, '1000'))
        ]
        response = session.post(url, data=product_json_data, files=files,headers=headers)
        print ("Response for product data post",response.text)
        response_json = response.json()
        for _, file in files:
            if isinstance(file, tuple) and hasattr(file[1], 'close'):
                file[1].close()
        return False if response_json["status"] == "error" else True
    def delete_product_data(self):
        pass


class Product_Image_Data():
    def __init__(self) -> None:
        pass
    def post_product_image(self):
        pass
    def delete_product_image(self):
        pass

class Product_Json_Helper:
    def __init__(self) -> None:
        pass
    def load_json_data(self,json_file):
        import json
        product_json_data = None
        with open(json_file,"r") as f: 
            product_json_data = json.load(f)
        if not product_json_data : raise BaseException("Product Json Data cannot be read " , json_file)
        product_json_data = self.validate_json_data(product_json_data)
        return product_json_data
        return product_json_data
    def validate_json_data(self,product_json_data):
        product_fields = ["product_summary","product_categories","product_pros","product_cons","product_usecases","product_toolfor","product_pricing","product_rating","product_name","product_unique_id","product_pricing_available","product_affiliate_available","product_url"]
        for each_field in product_fields:
            if each_field not in product_json_data: raise BaseException("Product Json not in Format ", each_field )  
        if not isinstance(product_json_data["product_pricing"],dict) or not isinstance(product_json_data["product_pricing"],list) : product_json_data["product_pricing"] = [product_json_data["product_pricing"]]
        product_json_data["product_categories"] = json.dumps(product_json_data["product_categories"])
        product_json_data["product_pros"] = json.dumps(product_json_data["product_pros"])
        product_json_data["product_cons"] = json.dumps(product_json_data["product_cons"])
        product_json_data["product_usecases"] = json.dumps(product_json_data["product_usecases"])
        product_json_data["product_toolfor"] = json.dumps(product_json_data["product_toolfor"])
        product_json_data["product_pricing"] = json.dumps(product_json_data["product_pricing"])
        return product_json_data

# product_json_data
# json_file = "json/97b1d2ee-940d-4ef0-ab48-0abceb9170ef.json"
# image_paths = ["screenshots/97b1d2ee-940d-4ef0-ab48-0abceb9170ef_home.png","screenshots/97b1d2ee-940d-4ef0-ab48-0abceb9170ef_home copy.png"]
# Product_Data().post_product_data(json_file,image_paths)

# producut_json_data = load_json_data(json_file)
# product_post.post_product_data(producut_json_data)

# res = requests.get("http://127.0.0.1:8000/softwareguru")
# res = requests.get(properties.backend_url)
# properties.backend_url+properties.upload_product_data
# import uuid
# str(uuid.uuid4())