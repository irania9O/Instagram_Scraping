from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.instagram.com/?hl=en")
assert "Instagram" in driver.title.strip()
driver.find_element(by=By.NAME, value='username').click()

input_username_Element = driver.find_element(by=By.NAME, value='username')
input_username_Element.send_keys('insta_for_sel_ap@hi2.in')

input_password_Element = driver.find_element(by=By.NAME, value='password')
input_password_Element.send_keys('AP_1401@sel')

driver.find_element(by=By.CSS_SELECTOR, value='.sqdOP > .qF0y9').click()


try:
    element = WebDriverWait(driver, 10)
    element.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".yWX7d")))
except Exception as e: print(e)
finally:
    driver.find_element(by=By.CSS_SELECTOR, value='yWX7d').click()
print("ok")
#driver.quit()

