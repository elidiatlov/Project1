import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

### Opens the website, pressing on login button and "not sign yet" button

driver = webdriver.Chrome(executable_path="C:\Selenium\chromedriver_win32\chromedriver.exe")
driver.get("https://buyme.co.il/")
driver.find_element_by_xpath("//*[@id='ember577']/div/ul[1]/li[3]/a/span[1]").click()
driver.find_element_by_id("ember959").send_keys("Aa12345678@gmail.com")
driver.find_element_by_id("ember961").send_keys("Aa12345678")
driver.find_element_by_xpath("//*[@id='ember951']/button").click()

### By using the elements, we fill up the necessary details for siging up to the website

driver.find_element_by_id("ember901").send_keys("eli")
driver.find_element_by_id("ember902").send_keys("Aa12345678@gmail.com")
driver.find_element_by_id("valPass").send_keys("Aa12345678")
driver.find_element_by_id("ember904").send_keys("Aa12345678")
driver.find_element_by_xpath("//*[@id='ember900']/div[5]/div/label").click()
driver.find_element_by_xpath("//*[@id='ember900']/button").click()
print(123)
print(456)

time.sleep(3)

###adding information about price point, area and catagory, after that pressing search
driver.find_element_by_xpath("//*[@id='ember650_chosen']/a").click()
driver.find_element_by_xpath("//*[@id='ember650_chosen']/div/ul/li[5]").click()
driver.find_element_by_xpath("//*[@id='ember665_chosen']/a/span").click()
driver.find_element_by_xpath("//*[@id='ember665_chosen']/div/ul/li[3]").click()
driver.find_element_by_xpath("//*[@id='ember674_chosen']/a/span").click()
driver.find_element_by_xpath("//*[@id='ember674_chosen']/div/ul/li[3]").click()
driver.find_element_by_id("ember709").click()

### picking a businuss place and typing a price

time.sleep(3)
a = driver.find_elements_by_css_selector('a[href*="/supplier/"]')[2].click()
print(a)
time.sleep(3)
driver.find_element_by_id("ember1154").send_keys("1000")
driver.find_element_by_xpath("//*[@id='ember1153']/div[2]/div/button").click()

### adding sender & receiver information

time.sleep(3)

driver.find_element_by_xpath("//*[@id='ember1214']/label[1]").click()
driver.find_element_by_xpath("//*[@id='ember1241']").send_keys("eli")
driver.find_element_by_id("ember1243").send_keys("liro")
driver.find_element_by_xpath("//*[@id='ember1251_chosen']/a/span").click()
driver.find_element_by_xpath("//*[@id='ember1251_chosen']/div/ul/li[2]").click()
driver.find_element_by_xpath("//*[@id='ember1265']/textarea").send_keys("Enjoy the gift")

### chosing handly a photo we want to add

driver.find_element_by_id("ember1274").click()

### adding last details and sending

driver.find_element_by_xpath("//*[@id='ember1207']/div[3]/div/div[1]/label[1]").click()
driver.find_element_by_xpath("//*[@id='ember1207']/div[4]/div/div[1]/div[2]/div/button").click()
driver.find_element_by_xpath("//*[@id='ember1707']").send_keys("friend@gmail.com")
driver.find_element_by_xpath("//*[@id='ember1207']/div[4]/div/div[3]/div/div[2]/button[2]").click()
driver.find_element_by_xpath("//*[@id='ember1207']/div[5]/button").click()