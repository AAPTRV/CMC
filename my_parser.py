import util_project.projects_names_parser
import util_project.transformer

url = "https://daomaker.com/"
# list_of_projects = util_project.projects_names_parser.get_list_of_projects(url)
# for item in list_of_projects:
#     print(util_project.transformer.get_url_from_project_name(item, url))

list_of_url_projects = util_project.projects_names_parser.get_projects_as_objects(url)

for project in list_of_url_projects:
    print(project.get_name())
    print(project.get_url())
    print("\n")


