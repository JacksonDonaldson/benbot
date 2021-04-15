from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

f = open("dataStorage.py", "w")
print("Enter the urls from bestbuy to search, for example https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440 for the 3080 founder's edition\nhit enter after each url, ensuring there is no white space before or after\nOnly the first entered url will be purchased if multiple become available simultanously \nenter \"done\" after the last url")
urls = []
i = ""
i = input()
while i!= "done":
    urls.append(i)
    i = input()
f.write("urls = " + str(urls) + "\n") 
f.write("email = \"" + input("bestbuy email: ") + "\"\npassword = '" + input("bestbuy password: ") + "'\ndiscordId = " + input("discord id: (go into settings->advanced->enable developer mode, then right click your profile in a server on the right bar and copy id):") + "\n")

f.write("cvv = \"" + input("Credit card 3 digit security code: ") + "\"\n")
f.write("phoneNumber = \"" + input("phone number: ") + "\"\n")
f.write("firstName = \"" + input("Billing Address First Name: ") + "\"\n")
f.write("lastName = \"" + input("Billing Address Last Name: ") + "\"\n")
f.write("street = \"" + input("Billing Address Street Address: ") + "\"\n")
f.write("city = \"" + input("Billing Address City: ") + "\"\n")
f.write("state = \"" + input("Billing Address State (postal code, ex: mi: ") + "\"\n")
f.write("zipcode = \"" + input("Billing Address Zipcode: ") + "\"\n")

f.close()
import sendNotif as notif
import dataStorage
def testPurchase():
    print("purchasing")
    driver = webdriver.Firefox()
    while True:
        try:
            driver.get("https://www.bestbuy.com")
            
            elem = driver.find_element_by_class_name("utility-navigation-list-item")
            elem.click()
            elem = driver.find_element_by_class_name("abt-2465-menu-header")
            elem.find_element_by_tag_name("a").click()
            time.sleep(5)
            break
        except:
            pass
    elem = driver.find_element_by_id("fld-e")
    elem.send_keys(dataStorage.email)

    elem = driver.find_element_by_id("fld-p1")
    elem.send_keys(dataStorage.password)
    elem.send_keys(Keys.RETURN)

    print("attempted login, saving current cookies to auto-login next time")
    time.sleep(2)
    cookies = driver.get_cookies()
    f = open("dataStorage.py", "a")
    f.write("\ncookies = " + str(cookies))
    f.close()

    print("Cookies saved. reloading webpage and attempting cookie-based signin")
    driver.quit()
    driver = webdriver.Firefox()
    driver.get("https://www.bestbuy.com")
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://www.bestbuy.com")
    print("should have loaded bestbuy, and logged in.")
    print("assuming it did, test was successful. Check dataStorage.py if you want to make sure your entered information is correct.")
    time.sleep(10)
    driver.quit()
    
    

print("executing test.")
print("sending discord notification")
notif.start("This is a test notification")
print("logging in to save cookies")
testPurchase()
print("Test complete")
##print(toSave)
##f.write("\ncookies= " + str(toSave))

print("setup complete. run \"run.cmd\" to start the program")
