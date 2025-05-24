from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_books():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # без окна браузера
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)

    driver.get("http://books.toscrape.com/catalogue/page-1.html")
    time.sleep(2)

    books = []
    items = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")

    for item in items:
        title = item.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
        price = item.find_element(By.CSS_SELECTOR, "p.price_color").text.strip("£")
        rating_class = item.find_element(By.CSS_SELECTOR, "p.star-rating").get_attribute("class")
        # rating_class: "star-rating Three" например
        rating_str = rating_class.split()[-1]
        rating_map = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}
        rating = rating_map.get(rating_str, 0)

        books.append({
            "title": title,
            "price": float(price),
            "rating": rating
        })

    driver.quit()
    return books

