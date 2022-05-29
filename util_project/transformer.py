

def get_url_from_project_name(name, base_url):
    #TODO write in RegEx
    result = name.replace(" ", "-").replace(".", "-")
    return base_url + f"{result}"