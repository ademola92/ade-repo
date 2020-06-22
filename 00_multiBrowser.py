from selenium import webdriver

from selenium.webdriver.common.keys import Keys
#Createdriver object and then the method chrome
# then pass a method called executable path to put driver location
driver = webdriver.Chrome(executable_path="/Users/ademolaadejuyigbe/driver/chromedriver")

#firefox
driver = webdriver.Firefox(executable_path="")
#internet explorer
driver = webdriver.Ie(executable_path="")

#navigate to the url
driver.get("http://youtube.com")

#get title of page
print(driver.title)

#get current url
print(driver.current_url)

#get you html code for the page
print(driver.page_source)

#close the browser
driver.close()