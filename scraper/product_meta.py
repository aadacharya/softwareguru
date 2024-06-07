from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import re
import json
product_meta_map = None
with open("data/product_meta_data.json" , "r") as f :
    product_meta_map = json.load(f)
# product_meta_map

driver = webdriver.Chrome()
url = "https://www.g2.com/search?utf8=%E2%9C%93&query=a&filters%5Bstar_rating%5D%5B%5D=5&order=popular"
driver.get(url)
import time
for _ in range(5000):
    element = driver.find_element(By.CSS_SELECTOR, "li.pagination__component.pagination__page-number.pagination__page-number--current")
    page_number = element.text
    product_meta_map[page_number] = {}
    product_elements = driver.find_elements(By.CSS_SELECTOR, 'div[class="paper mb-1"]')
    if len(product_elements) == 0 :
        driver.refresh()
        continue
    for index,product_element in enumerate(product_elements):
        try:
            product_review_parent = product_element.find_element(By.CSS_SELECTOR, "a.product-listing__img.js-log-click")
            product_review_link = product_review_parent.get_attribute("href")
            product_name_div = product_element.find_element(By.CSS_SELECTOR, 'div[itemprop="name"]')
            product_name = product_name_div.text.strip()
            star_element = product_element.find_element(By.CSS_SELECTOR, "div.stars")
            class_attribute = star_element.get_attribute("class")
            rating = int(re.search(r'stars-(\d+)', class_attribute).group(1))/2
            product_paragraph_span = product_element.find_element(By.CSS_SELECTOR, "span.product-listing__paragraph")
            product_paragraph = product_paragraph_span.text.strip()
            if product_paragraph_span.get_attribute("data-truncate-revealer-overflow-text"):  
                product_paragraph = product_paragraph[:-12] + product_paragraph_span.get_attribute("data-truncate-revealer-overflow-text")
            product_image = product_element.find_element(By.CSS_SELECTOR, 'img[itemprop="image"]')  
            image_source = product_image.get_attribute("src") if product_image.get_attribute("src").startswith("http") else product_image.get_attribute("data-deferred-image-src")
            categories_parent = product_element.find_element(By.CSS_SELECTOR, "div.product-listing__search-footer > div.cell.xlarge-8")
            categories = []
            category_links = categories_parent.find_elements(By.CSS_SELECTOR, "a.link.js-log-click")
            for link in category_links:
                categories.append(link.text)
            print(page_number,index)
            product_meta_map[page_number][index] = {"PRODUCT_REVIEW_LINK":product_review_link,"PRODUCT_NAME":product_name,"RATING":rating,"ABOUT":product_paragraph,"LOGO":image_source,"CATEGORIES":categories}
        except :
            print(f"error in page {page_number} and index {index}" )
    import json
    with open(f"data/product_meta_data{page_number}.json", "w") as json_file:
        json.dump(product_meta_map, json_file, indent=4)
    next_link = driver.find_element(By.LINK_TEXT, "Next ›")
    next_link.click()
    time.sleep(2)
