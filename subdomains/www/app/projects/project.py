from fastapi.templating import Jinja2Templates


class Project:
    # A Project Describes an HTMX & Tailwind powered webpage that contains a project I have created

    def __init__(self, name, description, icon_path, route_base):
        self.name = name
        self.description = description
        self.icon_path = icon_path
        self.templates = Jinja2Templates(directory="templates")
        self.route_base = route_base

    def parse_template(self):
        pass
