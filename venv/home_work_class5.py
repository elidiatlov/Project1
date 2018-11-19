from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#1
 #a
driver = webdriver.Chrome(executable_path="C:\Selenium\chromedriver_win32\chromedriver.exe")
driver.get("https://www.walla.co.il")
 #b
driver = webdriver.Chrome(executable_path="C:\Selenium\chromedriver_win32\chromedriver.exe")
driver.get("https://www.ynet.co.il")

#2

title = driver.title
driver.refresh()
if title==driver.title:
    print("equel")

#3
#yes indeed, the elements remain the same no matter the browser.

#4

driver.get("https://translate.google.com")
driver.find_element_by_id("source").send_keys("שבת שלום")
driver.find_element_by_id("gt-submit").click()

#5

driver.get("https://www.youtube.com")
driver.find_element_by_id("search").send_keys("syava - workout")
driver.find_element_by_id("search-icon-legacy").click()

#6

driver.get("https://translate.google.com")
driver.find_element_by_xpath("//*[@id='gt-submit']") ### what is to delete???
driver.find_element_by_id("gt-submit")
driver.find_element_by_class_name("jfk-button.jfk-button-action")
print(b)

#7

driver.get("https://www.facebook.com")
driver.find_element_by_id("email").send_keys("test@gmail.com")
driver.find_element_by_name("pass").send_keys("12345")
driver.find_element_by_id("loginbutton").click()

#8
#?????????????????????????????????????????????????????????????????????????????????????????

#9

driver.find_element_by_name("q")