import requests
import properties

url = properties.backend_url + properties.get_csfr_token
session = requests.session()
session.get(url)
csrf_token = session.cookies['csrftoken'] 
csrf_token