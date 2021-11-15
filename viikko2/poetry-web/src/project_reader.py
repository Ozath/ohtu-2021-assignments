import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        # content = request.urlopen(self._url).read().decode("utf-8")
        content = toml.load("pyproject.toml")
        # print(content)
        a = list(content['tool']['poetry']['dependencies'].keys())
        b = list(content['tool']['poetry']['dev-dependencies'].keys())
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(content['tool']['poetry']['name'], content['tool']['poetry']['description'], a, b)
