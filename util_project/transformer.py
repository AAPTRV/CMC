

def get_url_from_project_name(name, base_url):
    #TODO write in RegEx
    result = name.replace(" ", "-").replace(".", "-")
    return base_url + f"{result}"

def transform_slug_json_into_dict(json):

    name_default = "No name found through transform function"
    ticker_default = "No ticket found through transform function"
    personal_allocation_default = "No personal allocation found through transform function"

    name = name_default
    ticker = ticker_default
    personal_allocation = personal_allocation_default

    if "title" in json:
        name = json["title"]

    for table in json:
        if personal_allocation == personal_allocation_default:
            if "Personal Allocation:" in table:
                personal_allocation = table["Personal Allocation"]
            elif "Individual Allocation:" in table:
                personal_allocation = table["Individual Allocation"]
            elif "Individual Allocation: " in table:
                personal_allocation = table["Individual Allocation "]
            elif "DAO SHO Individual Allocation:" in table:
                personal_allocation = table["DAO SHO Individual Allocation:"]
            elif "DAO SHO Personal Allocation: " in table:
                personal_allocation = table["DAO SHO Personal Allocation: "]
            elif "Allocation:" in table:
                personal_allocation = table["Individual Allocation"]
            elif "Personal Allocation (Round 2):" in table:
                personal_allocation = table["Personal Allocation (Round 2):"]
            elif "Hardcap (SHO):" in table:
                personal_allocation = table["Hardcap (SHO):"]
            elif "'Personal Cap (SHO)'" in table:
                personal_allocation = table["Personal Cap (SHO)"]

        if ticker == ticker_default:
            if "Ticker:" in table:
                ticker = table["Ticket"]
            elif "Ticker" in table:
                ticker = table["Ticker"]
            elif "Key MetricsTicker" in table:
                ticker = table["Key MetricsTicker"]

    return {'ticker': ticker,
            'name': name,
            'personal_allocation': personal_allocation}
