from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

def get_ticket(url):
    driver = webdriver.Chrome(executable_path="/Users/eaxes/DA Projects/CMC/chromedriver/chromedriver")
    try:

        driver.get(url=url)
        time.sleep(25)
        # TODO time.sleep not a constant but wait until page is fully opened

        button = driver.find_element_by_xpath('//button[normalize-space()="Key Metrics"]')
        ActionChains(driver).move_to_element(button).click(button).perform()

        time.sleep(5)
        ticket = driver.find_elements_by_class_name("metrics__block")[0] \
            .find_element(By.CSS_SELECTOR, "h3") \
            .get_attribute("innerHTML")
        print(f"Ticker: {ticket}")

        return ticket

    except Exception as ex:
        print(ex)
        return "Failed to load ticket"

    finally:
        driver.close()
        driver.quit()
        time.sleep(5)
