from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os
from datetime import datetime

# Create timestamped folder for screenshots on Desktop
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
screenshot_folder = os.path.join(os.path.expanduser("~"), "Desktop", timestamp)
os.makedirs(screenshot_folder, exist_ok=True)

# ===== DESKTOP TEST =====
print("Starting DESKTOP login test...")
service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

try:
    #step 1: navigate to the landing page
    driver.get("https://qa-app.ourpact.com")
    driver.maximize_window()
    time.sleep(2) #optional, waits for page to load.
    
    # Take screenshot of login page
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_01_desktop_login_page.png"))

    email_field = driver.find_element(By.XPATH, '//*[@data-testid="input_email"]')
    password_field = driver.find_element(By.XPATH, '//*[@data-testid="input_pw"]')

    email_field.send_keys("tylerj@mailinator.com")
    password_field.send_keys("qqqqqqqq")

    login_button = driver.find_element(By.XPATH, '//*[@data-testid="btn_login"]')
    login_button.click()

    time.sleep(2)
    
    # Take screenshot after login
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_02_desktop_after_login.png"))

    logout_button = driver.find_element(By.XPATH, '//*[@title="Log Out"]')
    logout_button.click()

    time.sleep(2)
    
    # Take screenshot after logout
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_03_desktop_after_logout.png"))

    print("Desktop test completed!")

finally:
    driver.quit()

time.sleep(1)

# ===== MOBILE TEST =====
print("Starting MOBILE login test...")
mobile_user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1"
chrome_options = Options()
chrome_options.add_argument(f"user-agent={mobile_user_agent}")
chrome_options.add_argument("--window-size=375,812")

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    #step 1: navigate to the landing page
    driver.get("https://qa-app.ourpact.com")
    time.sleep(2)
    
    # Take screenshot of login page on mobile
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_04_mobile_login_page.png"))

    email_field = driver.find_element(By.XPATH, '//*[@data-testid="input_email"]')
    password_field = driver.find_element(By.XPATH, '//*[@data-testid="input_pw"]')

    email_field.send_keys("tylerj@mailinator.com")
    password_field.send_keys("qqqqqqqq")

    login_button = driver.find_element(By.XPATH, '//*[@data-testid="btn_login"]')
    login_button.click()

    time.sleep(2)
    
    # Take screenshot after login on mobile
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_05_mobile_after_login.png"))

    logout_button = driver.find_element(By.XPATH, '//*[@title="Log Out"]')
    logout_button.click()

    time.sleep(2)
    
    # Take screenshot after logout on mobile
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_06_mobile_after_logout.png"))

    print("Mobile test completed!")
    print(f"\nAll screenshots saved to: {screenshot_folder}")

finally:
    driver.quit()


