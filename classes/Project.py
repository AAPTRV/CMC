import pandas as pd


class Project(object):

    def __init__(self, name, url, ticket):
        self.name = name
        self.url = url
        self.ticket = ticket

    def get_name(self):
        return self.name

    def get_url(self):
        return self.url

    def get_ticket(self):
        return self.ticket

    def get_series(self):
        return pd.Series({"name":   self.get_name(),
                          "ticket": self.get_ticket(),
                          "url":    self.get_url()})


