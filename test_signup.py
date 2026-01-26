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

# ===== DESKTOP SIGNUP TEST =====
print("Starting DESKTOP signup test...")
service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

try:
    # Navigate to landing page
    driver.get("https://qa-app.ourpact.com")
    driver.maximize_window()
    time.sleep(2)
    
    # Take screenshot of login page
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_01_desktop_login_page.png"))
    
    # Click signup link
    signup_link = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/section/section/div[2]/div/div/form/div[5]/a")
    signup_link.click()
    
    time.sleep(2)
    
    # Take screenshot of signup page
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_02_desktop_signup_form.png"))
    
    # Fill in signup form
    # Name field
    name_field = driver.find_element(By.XPATH, '//*[@id="firstName"]')
    name_field.send_keys(f"Automated Test {timestamp}")
    
    # Email field
    email_field = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/section/section/div[2]/div/div/form/div[2]/input")
    email_field.send_keys(f"automated_test_{timestamp}@mailinator.com")
    
    # Password field
    password_field = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/section/section/div[2]/div/div/form/div[3]/div[1]/input")
    password_field.send_keys("qqqqqqqq")
    
    # Confirm Password field
    confirm_password_field = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/section/section/div[2]/div/div/form/div[4]/input")
    confirm_password_field.send_keys("qqqqqqqq")
    
    time.sleep(1)
    
    # Take screenshot after filling form
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_03_desktop_form_filled.png"))
    
    # Click signup button
    signup_button = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/section/section/div[2]/div/div/form/div[6]/button")
    signup_button.click()
    
    time.sleep(2)
    
    # Take screenshot after signup (before consent modal)
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_04_desktop_after_signup.png"))
    
    # Handle Data and Privacy consent modal
    time.sleep(1)
    consent_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div/div[3]/div[2]/button")
    consent_button.click()
    
    time.sleep(2)
    
    # Take screenshot after consent
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_05_desktop_after_consent.png"))

    print("Desktop signup test completed!")

finally:
    driver.quit()

time.sleep(1)

# ===== MOBILE SIGNUP TEST =====
print("Starting MOBILE signup test...")
mobile_user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1"
chrome_options = Options()
chrome_options.add_argument(f"user-agent={mobile_user_agent}")
chrome_options.add_argument("--window-size=375,812")

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Navigate to landing page
    driver.get("https://qa-app.ourpact.com")
    time.sleep(2)
    
    # Take screenshot of login page on mobile
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_06_mobile_login_page.png"))
    
    # Click signup link
    signup_link = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/section/section/div[2]/div/div/form/div[5]/a")
    signup_link.click()
    
    time.sleep(2)
    
    # Take screenshot of signup page on mobile
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_07_mobile_signup_form.png"))
    
    # Fill in signup form
    # Name field
    name_field = driver.find_element(By.XPATH, '//*[@id="firstName"]')
    name_field.send_keys(f"Automated Test {timestamp}")
    
    # Email field
    email_field = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/section/section/div[2]/div/div/form/div[2]/input")
    email_field.send_keys(f"automated_test_{timestamp}@mailinator.com")
    
    # Password field
    password_field = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/section/section/div[2]/div/div/form/div[3]/div[1]/input")
    password_field.send_keys("qqqqqqqq")
    
    # Confirm Password field
    confirm_password_field = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/section/section/div[2]/div/div/form/div[4]/input")
    confirm_password_field.send_keys("qqqqqqqq")
    
    time.sleep(1)
    
    # Take screenshot after filling form
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_08_mobile_form_filled.png"))
    
    # Click signup button
    signup_button = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/section/section/div[2]/div/div/form/div[6]/button")
    signup_button.click()
    
    time.sleep(2)
    
    # Take screenshot after signup (before consent modal)
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_09_mobile_after_signup.png"))
    
    # Handle Data and Privacy consent modal
    time.sleep(1)
    consent_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div/div[3]/div[2]/button")
    consent_button.click()
    
    time.sleep(2)
    
    # Take screenshot after consent
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_10_mobile_after_consent.png"))

    print("Mobile signup test completed!")
    print(f"\nAll screenshots saved to: {screenshot_folder}")

finally:
    driver.quit()
