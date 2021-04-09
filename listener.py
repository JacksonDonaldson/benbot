import requests as reqs
import benBotSendNotif as notif
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import dataStorage
email = "mopavet284@ddwfzp.com"
password = "thisisatestpassword"

url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440'
cookie = "dtSa=-"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36", "cookie":cookie}

def notify(message):
    notif.start(message)

def cookify(d):
    for cookie in dataStorage.cookies:
        d.add_cookie(cookie)
    
def purchase():
    print("purchasing")
    driver = webdriver.Firefox()
    driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")
    cookify(driver)
    driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")
    quit()
    elem = driver.find_element_by_class_name("fulfillment-add-to-cart-button")
    elem.click()
    time.sleep(30)
    while("art" not in elem.text):
        elem = driver.find_element_by_class_name("fulfillment-add-to-cart-button")
        time.sleep(.05)
    elem.click()
    #added to cart.

    elem = driver.find_element_by_class_name("cart-link")
    elem.click()

    time.sleep(.5)
    
    elem = driver.find_element_by_class_name("checkout-buttons__checkout")
    elem.click()

    time.sleep(5)

    elem = driver.find_element_by_id("fld-e")
    elem.send_keys(email)

    elem = driver.find_element_by_id("fld-p1")
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)

    time.sleep(20)
    
    driver.quit()
    print("successfully clicked element")

while True:
    t = reqs.get(url, headers = headers)
    if ">Sold Out</button>" in t.text:
        #executes if the webpage doesn't have a sold out button
        notif.start("A 3080 is available. Attempting purchase.")
        purchase()
        quit()
