from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/eaxes/DA Projects/CMC/chromedriver/chromedriver")

url = "https://daomaker.com/company/gamium"

try:
    driver.get(url=url)
    time.sleep(15)
    #TODO time.sleep not a constant but wait until page is fully opened

    button = driver.find_element_by_xpath('//button[normalize-space()="Key Metrics"]')
    ActionChains(driver).move_to_element(button).click(button).perform()

    time.sleep(5)
    some_data = driver.find_elements_by_class_name("metrics__block")

    ticker = some_data[0].find_element(By.CSS_SELECTOR, "h3").get_attribute("innerHTML")

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
