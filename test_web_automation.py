from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://qa-app.ourpact.com")

print("Page title is:", driver.title)

driver.quit()



