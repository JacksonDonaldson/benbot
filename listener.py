import requests as reqs
import sendNotif as notif
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import dataStorage
import sys

# email = "mopavet284@ddwfzp.com"
# password = "thisisatestpassword"

#url = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"
cookie = "dtSa=-"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "cookie": cookie}


def notify(message):
    notif.start(message)


def cookify(d):
    for cookie in dataStorage.cookies:
        d.add_cookie(cookie)

def key(d, m):
    for c in m:
        d.send_keys(c)
        time.sleep(.1)
        
def purchase(url):
    print("purchasing")
    driver = webdriver.Firefox()
    driver.get(url)

    cookify(driver)
    driver.get(url)
    # quit()
    
    elem = driver.find_element_by_class_name("fulfillment-add-to-cart-button")
    elem.click()
    time.sleep(4)
    elem = driver.find_element_by_class_name("fulfillment-add-to-cart-button")
    inner = elem.get_attribute("innerHTML")
    while elem.get_attribute("innerHTML") == inner:
        elem = driver.find_element_by_class_name("fulfillment-add-to-cart-button")
        time.sleep(.05)
        
    elem.click()
    # added to cart.
    try:
        elem = driver.find_element_by_class_name("cart-link")
        elem.click()
    except:
        pass
    time.sleep(1)
    try:
        elem = driver.find_elements_by_class_name("availability__fulfillment")[1].find_element_by_class_name("c-radio-brand")
        elem.click()
        time.sleep(1)
    except:
        pass
    try:
        elem = driver.find_element_by_class_name("checkout-buttons__checkout")
        elem.click()
    except:
        pass

    time.sleep(5)

    
    try:
        elem = driver.find_element_by_id("fld-e")
        elem.send_keys(dataStorage.email)
    except:
        pass
    try:
        elem = driver.find_element_by_class_name("button--continue")
        elem.click()
        time.sleep(4)
    except:
        pass
    try:
        elem = driver.find_element_by_id("fld-p1")
        elem.send_keys(dataStorage.password)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
    except:
        pass
    try:
        elem = driver.find_element_by_id("consolidatedAddresses.ui_address_2.firstName")
        time.sleep(.1)
        key(elem, dataStorage.firstName)
        print(dataStorage.firstName)
        elem = driver.find_element_by_id("consolidatedAddresses.ui_address_2.lastName")
        time.sleep(.1)
        key(elem, dataStorage.lastName)
        elem = driver.find_element_by_id("consolidatedAddresses.ui_address_2.street")
        time.sleep(.1)
        key(elem, dataStorage.street)
        print("sent street")
        elem = driver.find_element_by_id("consolidatedAddresses.ui_address_2.city")
        time.sleep(.1)
        key(elem, dataStorage.city)
        elem = driver.find_element_by_id("consolidatedAddresses.ui_address_2.state")
        elem.find_elements_by_tag_name("option")[27].click()
        elem = driver.find_element_by_id("consolidatedAddresses.ui_address_2.zipcode")
        time.sleep(.1)
        key(elem, dataStorage.zipcode)
    except:
        pass
    try:
        elem = driver.find_element_by_id("user.phone")
        elem.send_keys(dataStorage.phoneNumber)
        time.sleep(3)
    except:
        pass
    try:
        elem = driver.find_element_by_class_name("button--continue")
        elem.click()
        time.sleep(4)
    except:
        pass
    time.sleep(2)
    try:
        elem = driver.find_element_by_id("credit-card-cvv")
        elem.send_keys(dataStorage.cvv)
        time.sleep(3.2)
    except:
        pass
    try:
        elem = driver.find_element_by_id("payment.billingAddress.firstName")
        elem.clear()
        elem.send_keys(dataStorage.firstName)
        elem = driver.find_element_by_id("payment.billingAddress.lastName")
        elem.clear()
        elem.send_keys(dataStorage.lastName)
        elem = driver.find_element_by_id("payment.billingAddress.street")
        elem.clear()
        elem.send_keys(dataStorage.street)
        elem = driver.find_element_by_id("payment.billingAddress.city")
        elem.clear()
        elem.send_keys(dataStorage.city)
        elem = driver.find_element_by_id("payment.billingAddress.state")
        elem.clear()
        elem.send_keys(dataStorage.state)
        elem = driver.find_element_by_id("payment.billingAddress.zipcode")
        elem.clear()
        elem.send_keys(dataStorage.zipcode)
    except:
        pass
    time.sleep(1)
    try:
        
        #pain
        elem = driver.find_element_by_class_name("button--place-order-fast-track")
        elem.find_elements_by_tag_name("button")[2].click()
    except:
        print("order placement failed for fast track")
    try:
        elem = driver.find_element_by_class_name("button--place-order")
        try:
            elem.find_elements_by_tag_name("button")[2].click()
        except:
            elem.find_element_by_tag_name("button").click()
    except:
        print("order placement failed for regular. If it also failed for fast track, there are problems")
    
    print("attempted order and login")



print("bot started. Awaiting stock.")

while True:
    for url in dataStorage.urls:
        try:
            t = reqs.get(url, headers=headers)
        except:
            print("error w/ reqs. If this happens once in a while, it's okay")
        if t.status_code != 200:
            notif.start("An error has occurred with the bot, and it has quit. Most likely, bestbuy blocked it from requesting the webpage. If you see this, contact Jackson")
            break
        if ">Sold Out</button>" not in t.text:
            # executes if the webpage doesn't have a sold out button
            notif.start("A " + url + " is available. Attempting purchase.")
            purchase(url)
            quit()
        #else:
        #    print(t.text[t.text.index(">Sold Out</button>")- 100 : t.text.index(">Sold Out</button>") + 100])
    
