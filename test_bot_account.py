from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os
from datetime import datetime

# Create timestamped folder for screenshots on Desktop
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
screenshot_folder = os.path.join(os.path.expanduser("~"), "Desktop", timestamp)
os.makedirs(screenshot_folder, exist_ok=True)

# ===== BOT ACCOUNT DESKTOP TEST =====
print("Starting BOT account DESKTOP test with dropdown and blocking operations...")
service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

try:
    # Step 1: Navigate to the landing page
    driver.get("https://qa-app.ourpact.com")
    driver.maximize_window()
    time.sleep(2)
    
    # Take screenshot of login page
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_01_login_page.png"))

    # Step 2: Login with bot account
    email_field = driver.find_element(By.XPATH, '//*[@data-testid="input_email"]')
    password_field = driver.find_element(By.XPATH, '//*[@data-testid="input_pw"]')

    email_field.send_keys("tyler+bot1@eturi.com")
    password_field.send_keys("qqqqqqqq")

    login_button = driver.find_element(By.XPATH, '//*[@data-testid="btn_login"]')
    login_button.click()

    time.sleep(3)
    
    # Take screenshot after login
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_02_after_login.png"))
    print("Bot account logged in successfully!")

    # Step 3: Click the Block Button
    block_button_xpath = '/html/body/div[1]/main/div/section/div/div/div/div[1]/div[1]/button[1]'
    block_button = driver.find_element(By.XPATH, block_button_xpath)
    block_button.click()
    time.sleep(2)
    
    # Take screenshot after clicking block button
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_03_after_block_button_click.png"))
    print("Block button clicked successfully!")

    # Step 4: Select dropdown option
    dropdown_xpath = '/html/body/div[1]/main/div[1]/section/div/div/div/div[1]/div[2]/form/select'
    try:
        dropdown_element = driver.find_element(By.XPATH, dropdown_xpath)
        select = Select(dropdown_element)
        
        # List all available options for debugging
        options = select.options
        print(f"Available dropdown options: {[opt.text for opt in options]}")
        
        # Try to select by visible text
        try:
            select.select_by_visible_text("Until I Say So")
        except:
            # If exact match fails, try partial match or value attribute
            print("Exact text match failed, trying alternative methods...")
            found = False
            for option in options:
                if "Until I Say So" in option.text or "until i say so" in option.text.lower():
                    select.select_by_value(option.get_attribute("value"))
                    found = True
                    break
            if not found:
                # Print all option texts for debugging
                print(f"Could not find 'Until I Say So' in options: {[opt.text for opt in options]}")
                # Select first non-empty option as fallback
                if len(options) > 1:
                    select.select_by_index(1)
        
        time.sleep(2)
        
        # Take screenshot after selecting dropdown option
        driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_04_after_dropdown_select.png"))
        print("Dropdown option selected successfully!")
    except Exception as e:
        print(f"Error selecting dropdown: {e}")
        # Take screenshot for debugging
        driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_04_ERROR_dropdown.png"))

    # Step 5: Wait for element presence and click button
    wait_element_xpath = '/html/body/div[1]/main/div/section/div/div/div/div[1]/div[2]/figure/span/span'
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, wait_element_xpath)))
    print("Waited element is now present!")
    
    # Take screenshot after waiting for element
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_05_after_wait_element.png"))
    
    # Click the button
    click_button_xpath = '/html/body/div[1]/main/div/section/div/div/div/div[1]/div[1]/button'
    click_button = driver.find_element(By.XPATH, click_button_xpath)
    click_button.click()
    time.sleep(2)
    
    # Take screenshot after clicking final button
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_06_after_final_button_click.png"))
    print("Final button clicked successfully!")

    # Step 6: Logout
    logout_button = driver.find_element(By.XPATH, '//*[@title="Log Out"]')
    logout_button.click()

    time.sleep(2)
    
    # Take screenshot after logout
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_07_after_logout.png"))

    print("Bot account DESKTOP test completed successfully!")
    print(f"All screenshots saved to: {screenshot_folder}")

except Exception as e:
    print(f"Error during DESKTOP test execution: {e}")
    # Take screenshot on error
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_DESKTOP_ERROR.png"))

finally:
    driver.quit()

time.sleep(1)

# ===== BOT ACCOUNT MOBILE TEST =====
print("\nStarting BOT account MOBILE test with dropdown and blocking operations...")
mobile_user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1"
chrome_options = Options()
chrome_options.add_argument(f"user-agent={mobile_user_agent}")
chrome_options.add_argument("--window-size=375,812")

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Navigate to the landing page
    driver.get("https://qa-app.ourpact.com")
    time.sleep(2)
    
    # Take screenshot of login page on mobile
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_m01_login_page.png"))

    # Step 2: Login with bot account
    email_field = driver.find_element(By.XPATH, '//*[@data-testid="input_email"]')
    password_field = driver.find_element(By.XPATH, '//*[@data-testid="input_pw"]')

    email_field.send_keys("tyler+bot1@eturi.com")
    password_field.send_keys("qqqqqqqq")

    login_button = driver.find_element(By.XPATH, '//*[@data-testid="btn_login"]')
    login_button.click()

    time.sleep(3)
    
    # Take screenshot after login
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_m02_after_login.png"))
    print("Bot account logged in successfully on mobile!")

    # Step 3: Click the Block Button
    block_button_xpath = '/html/body/div[1]/main/div/section/div/div/div/div[1]/div[1]/button[1]'
    block_button = driver.find_element(By.XPATH, block_button_xpath)
    block_button.click()
    time.sleep(2)
    
    # Take screenshot after clicking block button
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_m03_after_block_button_click.png"))
    print("Block button clicked successfully on mobile!")

    # Step 4: Select dropdown option
    dropdown_xpath = '/html/body/div[1]/main/div[1]/section/div/div/div/div[1]/div[2]/form/select'
    try:
        dropdown_element = driver.find_element(By.XPATH, dropdown_xpath)
        select = Select(dropdown_element)
        
        # List all available options for debugging
        options = select.options
        print(f"Available dropdown options on mobile: {[opt.text for opt in options]}")
        
        # Try to select by visible text
        try:
            select.select_by_visible_text("Until I Say So")
        except:
            # If exact match fails, try partial match or value attribute
            print("Exact text match failed on mobile, trying alternative methods...")
            found = False
            for option in options:
                if "Until I Say So" in option.text or "until i say so" in option.text.lower():
                    select.select_by_value(option.get_attribute("value"))
                    found = True
                    break
            if not found:
                # Print all option texts for debugging
                print(f"Could not find 'Until I Say So' in options: {[opt.text for opt in options]}")
                # Select first non-empty option as fallback
                if len(options) > 1:
                    select.select_by_index(1)
        
        time.sleep(2)
        
        # Take screenshot after selecting dropdown option
        driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_m04_after_dropdown_select.png"))
        print("Dropdown option selected successfully on mobile!")
    except Exception as e:
        print(f"Error selecting dropdown on mobile: {e}")
        # Take screenshot for debugging
        driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_m04_ERROR_dropdown.png"))

    # Step 5: Wait for element presence and click button
    wait_element_xpath = '/html/body/div[1]/main/div/section/div/div/div/div[1]/div[2]/figure/span/span'
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, wait_element_xpath)))
    print("Waited element is now present on mobile!")
    
    # Take screenshot after waiting for element
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_m05_after_wait_element.png"))
    
    # Click the button
    click_button_xpath = '/html/body/div[1]/main/div/section/div/div/div/div[1]/div[1]/button'
    click_button = driver.find_element(By.XPATH, click_button_xpath)
    click_button.click()
    time.sleep(2)
    
    # Take screenshot after clicking final button
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_m06_after_final_button_click.png"))
    print("Final button clicked successfully on mobile!")

    # Step 6: Logout
    logout_button = driver.find_element(By.XPATH, '//*[@title="Log Out"]')
    logout_button.click()

    time.sleep(2)
    
    # Take screenshot after logout
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_m07_after_logout.png"))

    print("Bot account MOBILE test completed successfully!")
    print(f"All screenshots saved to: {screenshot_folder}")

except Exception as e:
    print(f"Error during MOBILE test execution: {e}")
    # Take screenshot on error
    driver.save_screenshot(os.path.join(screenshot_folder, f"{timestamp}_MOBILE_ERROR.png"))

finally:
    driver.quit()

time.sleep(1)

