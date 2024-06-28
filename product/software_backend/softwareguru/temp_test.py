import requests
import properties

base_url = "http://127.0.0.1:8000/softwareguru/"

print("here", base_url + properties.update_category_data)


session = requests.Session()
session.get(base_url + properties.get_csfr_token)
csrf_token = session.cookies["csrftoken"]
headers = {"X-CSRFToken": csrf_token}  # CSRF token for security

# print("here", base_url + properties.update_category_data)

response = session.post(
    base_url + properties.update_category_data,
    data={},
    files={},
    headers=headers,
)

print(response.text, response.status_code)
