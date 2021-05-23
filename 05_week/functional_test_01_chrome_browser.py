from selenium import webdriver

path = './chromedriver'
driver = webdriver.Chrome(path)
driver.get('http://www.facebook.org')

