
import util_project.projects_names_parser
import util_project.json_parser


url = "https://daomaker.com/"
# list_of_projects = util_project.projects_names_parser.get_list_of_projects(url)
# for item in list_of_projects:
#     print(util_project.transformer.get_url_from_project_name(item, url))

list_of_url_projects = util_project.projects_names_parser.get_projects_as_objects(url)
print("End of parsing ...")

# test_url = "https://daomaker.com/company/spellfire"
# json = util_project.json_parser.get_json(test_url)
# print(json)
# result = util_project.json_parser.get_list_tickets(json)
# print(result)

# json = util_project.json_parser.get_json(url)
# ticket = util_project.json_parser.get_first_ticket(json)
# print(f"Ticket: {ticket}")


