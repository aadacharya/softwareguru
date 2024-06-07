from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import re
index = 0
driver = webdriver.Chrome()
url = "https://www.g2.com/products/lucid-software-inc-lucid-visual-collaboration-suite/reviews#reviews"
driver.get(url)
import time
for _ in range(5000):
    try:
        index = 0
        map = {}
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = driver.find_element(By.CSS_SELECTOR, "li.pagination__component.pagination__page-number.pagination__page-number--current")
        page_number = element.text
        map[page_number] = {}
        reviews_elements = driver.find_elements(By.CSS_SELECTOR, 'div[itemprop="review"]')
        # len(reviews_elements)
        if len(reviews_elements) == 0 :
            driver.refresh()
            continue
        # each_reviews = reviews_elements[0]
        last_review = None
        for each_reviews in reviews_elements:
            last_review = each_reviews
            element = each_reviews.find_element(By.CSS_SELECTOR, "div.stars")
            class_attribute = element.get_attribute("class")
            rating = int(re.search(r'stars-(\d+)', class_attribute).group(1))/2
            user_review=""
            div_elements = each_reviews.find_elements(By.CSS_SELECTOR, "div.d-f")
            for div_element in div_elements:
                user_review += div_element.text
            map[page_number][index] = [ rating,user_review]
            index+=1
        import json
        with open(f"extracted_reviews{page_number}.json", "w") as json_file:
            json.dump(map, json_file, indent=4)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        next_link = driver.find_element(By.LINK_TEXT, "Next ›")
        driver.execute_script("arguments[0].scrollIntoView();", last_review)
        next_link.click()
        time.sleep(2)
    except:
        print("Failed")
        continue
