from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Selenium\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(10)

driver.get("https://translate.google.co.il")
print(driver.current_url)

driver.find_element_by_id("gt-submit").click()

my_list = driver.find_elements_by_id("123")
my_list[0].click()

driver.find_element_by_xpath("//*[@id='gt-submit']")

driver.find_element_by_id("source").send_keys("Hello Word")

x = driver.find_element_by_id("gt-submit")
print(x.get_attribute("value"))




#prints URL title
print(driver.title)

#prints the DOM source
print(driver.page_source)

#closes current web page tab
driver.close()

#quits the whole session(srvices, etc)
driver.quit()

#browser goes back/forward/refresh
driver.back()/forward()/refresh()

##Locators
#ID
#Name
#Link Text
#Partial LinkText
#Class Name
#Xpath