from selenium import webdriver

path = './chromedriver'
driver = webdriver.Chrome(path)
driver.get('http://localhost:8000')

#assert "Django" in driver.title
assert "install" in driver.title
