from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com")

laptop_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Laptops')]")
laptop_button.click()


time.sleep(3)

laptops = driver.find_elements(By.CLASS_NAME, "card-title")
descpritions = driver.find_elements(By.CLASS_NAME, "card-text")
prices = driver.find_elements(By.TAG_NAME, "h5")

products = []

for laptop, price, descprition in zip(laptops, prices, descpritions):
    products.append({
        "laptop": laptop.text,
        "price": price.text,
        "description": descprition.text
    })
    
for product in products:
    print(f"Name: {product['laptop']}")
    print(f"Description: {product['price']}")
    print(f"Price: {product['description']}")
    print("-" * 30) 
    
with open("lesson-12\homework\products.json", mode="w") as file:
    json.dump(products, file, indent=4)
    
driver.quit()
