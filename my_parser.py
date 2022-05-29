import util_project.projects_names_parser

url = "https://daomaker.com/"
list_of_projects = util_project.projects_names_parser.get_list_of_projects(url)
for item in list_of_projects:
    print(item)



