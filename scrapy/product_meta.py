from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
index = 0
driver = webdriver.Chrome()
url = "https://www.g2.com/search?utf8=%E2%9C%93&query=a&filters%5Bstar_rating%5D%5B%5D=5&order=popular"
driver.get(url)
import time
for _ in range(5000):
    map = {}
    element = driver.find_element(By.CSS_SELECTOR, "li.pagination__component.pagination__page-number.pagination__page-number--current")
    page_number = element.text
    map[page_number] = {}
    elements = driver.find_elements(By.CLASS_NAME, "paper.mb-1")
    len(elements)
    if len(elements) == 0 :
        driver.refresh()
        continue
    for element in elements:
        try:
            product_name_div = element.find_element(By.CSS_SELECTOR, 'div[itemprop="name"]')
            product_name = product_name_div.text.strip()
            title_to_find = f"Read {product_name} Reviews"
            print(title_to_find)
            parent_element = element.find_element(By.XPATH, "//a[@title='" + title_to_find + "']")
            print(parent_element)
            reviews_link = parent_element.get_attribute("href")
            reviews_span = parent_element.find_element(By.CSS_SELECTOR, "span.pl-4th")
            reviews_text = reviews_span.text
            print("Reviews:", reviews_text)
            product_paragraph_span = element.find_element(By.CLASS_NAME, 'product-listing__paragraph')
            product_paragraph = product_paragraph_span.text.strip()
            product_image = element.find_element(By.CSS_SELECTOR, 'img[itemprop="image"]')
            image_src_1 = product_image.get_attribute("data-deferred-image-src")
            image_src = product_image.get_attribute("src")
            parent_div = driver.find_element(By.CSS_SELECTOR, "div.product-listing__search-footer > div.cell.xlarge-8")
            categories = []
            category_links = parent_div.find_elements(By.CSS_SELECTOR, "a.link.js-log-click")
            for link in category_links:
                categories.append(link.text)
            if index not in map[page_number]: map[page_number][index] = [ product_name,product_paragraph,[image_src,image_src_1],categories,[reviews_text,reviews_link]]
            index+=1
        except :
            print("error")
    import json
    with open(f"extracted_meta{page_number}.json", "w") as json_file:
        json.dump(map, json_file, indent=4)
    next_link = driver.find_element(By.LINK_TEXT, "Next ›")
    next_link.click()
    time.sleep(2)
