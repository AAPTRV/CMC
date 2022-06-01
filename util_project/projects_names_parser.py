from selenium import webdriver
import time
import util_project.json_parser_bs4
import util_project.json_parser
from selenium.webdriver import ActionChains
import util_project.ticker_parser
from classes.Project import Project


def get_projects_as_objects(url):
    result_list = []
    driver = webdriver.Chrome(executable_path="/Users/eaxes/DA Projects/CMC/chromedriver/chromedriver")

    try:
        driver.get(url=url)
        time.sleep(20)

        button = driver.find_elements_by_xpath('//a[normalize-space()="Load More"]')

        while len(button) > 0:
            ActionChains(driver).move_to_element(button[0]).click(button[0]).perform()
            time.sleep(3)
            button = driver.find_elements_by_xpath('//a[normalize-space()="Load More"]')

        companies_list = driver.find_elements_by_class_name("company_single")
        print("companies list length: ")
        print(len(companies_list))
        print("\n")

        for company in companies_list:

            print("Parsing info:")

            name = "Test name"
            print(name)

            ticket_url = company.find_element_by_class_name("btn.wide.btn_square.see_details") \
                .get_attribute("href")
            print(ticket_url)

            json = util_project.json_parser_bs4.get_json(ticket_url)
            print("Json OK!")
            ticket = util_project.json_parser.get_first_ticket(json)
            print("Ticket OK!")
            print(ticket + "\n")

            result_list.append(Project(name=name, url=url, ticket=ticket))
            print("Result list length is: " + str(len(result_list)))

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()

    return result_list
