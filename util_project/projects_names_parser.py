from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from classes.Project import Project


def get_projects_as_objects(url):
    result_list = []
    driver = webdriver.Chrome(executable_path="/Users/eaxes/DA Projects/CMC/chromedriver/chromedriver")

    try:
        driver.get(url=url)
        time.sleep(20)
    #     # TODO time.sleep not a constant but wait until page is fully opened
    #
    #     button = driver.find_elements_by_xpath('//a[normalize-space()="Load More"]')
    #     while len(button) > 0:
    #         ActionChains(driver).move_to_element(button[0]).click(button[0]).perform()
    #         time.sleep(3)
    #         button = driver.find_elements_by_xpath('//a[normalize-space()="Load More"]')

        companies_list = driver.find_elements_by_class_name("company_single")

        for company in companies_list:

            name = company.find_element_by_class_name("comp_details_header") \
                .find_element(By.CSS_SELECTOR, "h4") \
                .get_attribute("innerHTML") \
                .replace("<span>", "") \
                .replace("</span>", "") \
                .strip()

            url = company.find_element_by_class_name("btn.wide.btn_square.see_details") \
                .get_attribute("href")

            result_list.append(Project(name=name, url=url))

        print(len(companies_list))



    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()



    return result_list


def get_url_list_of_projects(url):
    result_list = []

    driver = webdriver.Chrome(executable_path="/Users/eaxes/DA Projects/CMC/chromedriver/chromedriver")
    try:
        driver.get(url=url)
        time.sleep(20)
        # TODO time.sleep not a constant but wait until page is fully opened

        button = driver.find_elements_by_xpath('//a[normalize-space()="Load More"]')
        while len(button) > 0:
            ActionChains(driver).move_to_element(button[0]).click(button[0]).perform()
            time.sleep(3)
            button = driver.find_elements_by_xpath('//a[normalize-space()="Load More"]')

        some_data = driver.find_elements_by_class_name("btn.wide.btn_square.see_details")
        print(len(some_data))
        for item in some_data:
            result_list.append(item.get_attribute("href"))


    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()

    return result_list

def get_list_of_projects(url):
    result_list = []
    driver = webdriver.Chrome(executable_path="/Users/eaxes/DA Projects/CMC/chromedriver/chromedriver")
    try:
        driver.get(url=url)
        time.sleep(20)
        # TODO time.sleep not a constant but wait until page is fully opened

        button = driver.find_elements_by_xpath('//a[normalize-space()="Load More"]')
        while len(button) > 0:
            ActionChains(driver).move_to_element(button[0]).click(button[0]).perform()
            time.sleep(3)
            button = driver.find_elements_by_xpath('//a[normalize-space()="Load More"]')

        some_data = driver.find_elements_by_class_name("comp_details_header")
        for item in some_data:
            name = item.find_element(By.CSS_SELECTOR, "h4") \
                               .get_attribute("innerHTML") \
                               .replace("<span>", "") \
                               .replace("</span>", "") \
                               .strip()
            result_list.append(name)

    except Exception as ex:
        print(ex)

    finally:
        print(len(result_list))
        driver.close()
        driver.quit()

    return result_list
