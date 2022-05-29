from selenium import webdriver
import re


def get_json(url):
    driver = webdriver.Chrome(executable_path="/Users/eaxes/DA Projects/CMC/chromedriver/chromedriver")

    try:
        driver.get(url=url)
        json = driver.find_element_by_id("com.daomaker.daopad-state")
        return json.get_attribute("innerHTML")

    except Exception as ex:
        print(ex)
        return("error")

    finally:
        driver.close()
        driver.quit()


def get_first_ticket(json):
    if json == "error":
        return "no ticket (missing dao pad state)"
    return re.search(r'\w*(?=&q;,&q;price_per_token)', string=json) \
        .group(0)

def get_list_tickets(json):
    if json == "error":
        return "no ticket (missing dao pad state)"
    return re.findall(r'\w*(?=&q;,&q;price_per_token)', string=json)