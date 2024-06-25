from flet import *
from pages.dashboard import Dashboard
from pages.login import Login
from pages.signup import Signup
from pages.forgotpassword import ForgotPassword

class Main(UserControl):
    def __ini__(self, page: Page,):
        super().__init__()
        self.page = page

    def init_helper(self):
        self.page.on_route_change = self.on_route_change

    def on_route_change(self, route):
        self.page.views.clear()
        self.page.views.append(
            View()
        )

app(target=Main, assets_dir="assets", view=WEB_BROWSER)