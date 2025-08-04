from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait as WDW
import time
import csv
'''✅ Title

✅ Price

✅ Rating (1 to 5 stars)

✅ Availability (In stock / Out of stock)

✅ Product page URL (optional)'''

rating_map = {"One": 1, "Two": 2
              ,"Three": 3,  "Four": 4
              ,"Five": 5}

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/")
time.sleep(3)
# Open the CSV only once
#with open("books_to_scrape.csv", "w", newline="", encoding='utf-8') as file:
   # writer = csv.writer(file)
   # writer.writerow(["Title", "Price", "Rating", "Availability", "Url"])

while True:
        WDW(driver,10).until(Ec.presence_of_all_elements_located((By.CLASS_NAME, "product_pod")))
        books = driver.find_elements(By.CLASS_NAME, "product_pod")
        for bk in books :
            title = bk.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
            price = bk.find_element(By.CLASS_NAME, "price_color").text
            ratingcs = bk.find_element(By.CLASS_NAME, "star-rating").get_attribute("class")#star-rating one 
            rating_parts = ratingcs.split()
            rating = [part for part in rating_parts if part != "star-rating"][0]
            #means rating_parts is a list like ["star-rating, one"] rting mens return anything in list except "star-rating"
            numeric_ratings = rating_map.get(rating, 0)
            availability = bk.find_element(By.CSS_SELECTOR, "p.instock.availability").text.strip()
            url = bk.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("href")
            # Write each row
         #   writer.writerow([title, price, numeric_ratings, availability, url])

            # Debug print (optional)
            print(f"✅ {title} | ${price} | {numeric_ratings}★ | {availability}")

            print(f"Title: {title}")
            print(f"price {price}")
            print(f"Availability: {availability}")
            print(f"Rating: {numeric_ratings} stars")
            print(f"Link : {url} ")
        try:
            next_button = driver.find_element(By.CLASS_NAME, "next")
            next_link = next_button.find_element(By.TAG_NAME, "a").get_attribute("href")
            driver.get(next_link)
            time.sleep(5)
        except:
            print("no more pages")
            break
        
    