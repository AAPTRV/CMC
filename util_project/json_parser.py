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
        return ("error")

    finally:
        driver.close()
        driver.quit()


def get_first_ticket(json):
    if json == "error":
        return "no ticket (missing dao pad state)"
    result = re.findall(r'(?<={&q;key&q;:&q;Ticker:&q;,&q;value&q;:&q;)\w*', string=json)
    if len(result) == 0 or result[0] == "0" or result[0] == "":
        result = re.findall(r'\w*(?=&q;,&q;price_per_token)', string=json)
    if len(result) == 0 or result[0] == "0" or result[0] == "":
        result = re.findall(r'(?<=coin_ticker&q;:&q;)\w*', string=json)
    if len(result) == 0 or result[0] == "0" or result[0] == "":
        result = re.findall(r'(?<=total_hardcap&q;:123,&q;coin_ticker&q;:&q;)\w*', string=json)

    if len(result) == 0:
        return "No ticket found (after 2 tries)"
    return result[0]

