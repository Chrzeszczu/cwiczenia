import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

#pause the test for few seconds using Time class
service_obj = Service(r"..\ChromeDriver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 8)

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")

# Wait until 3 or fewer objects are visible after search
wait.until(lambda browser: len(driver.find_elements(By.XPATH, "//div[@class='products']/div")) <= int(3))

count = len(driver.find_elements(By.XPATH, "//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)

driver.close()


