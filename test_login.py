from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Setup ChromeDriver
driver = webdriver.Chrome()

try:
    #step 1: navigate to the landing page
    driver.get("https://qa-app.ourpact.com")
    driver.maximize_window()
    time.sleep(2) #optional, waits for page to load.

    email_field = driver.find_element(By.XPATH, '//*[@data-testid="input_email"]')
    password_field = driver.find_element(By.XPATH, '//*[@data-testid="input_pw"]')

    email_field.send_keys("tylerj@mailinator.com")
    password_field.send_keys("qqqqqqqq")

    login_button = driver.find_element(By.XPATH, '//*[@data-testid="btn_login"]')
    login_button.click()

    time.sleep(2)

    logout_button = driver.find_element(By.XPATH, '//*[@title="Log Out"]')
    logout_button.click()

    time.sleep(2)



finally:
    driver.quit()


