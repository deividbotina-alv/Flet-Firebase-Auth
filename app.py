from flet import *
from pages.dashboard import Dashboard
from pages.login import Login
from pages.signup import Signup
from pages.forgotpassword import ForgotPassword

class Main(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.init_helper()

    def init_helper(self):
        self.page.on_route_change = self.on_route_change
        self.page.go("/signup")

    def on_route_change(self, route):
        new_page = {
            "/login": Login,
            "/signup": Signup,
            "/me": Dashboard,
            "/forgotpassword": ForgotPassword,
        }[self.page.route](self.page)

        self.page.views.clear()
        self.page.views.append(
            View(
                route,
                controls=[new_page]
            )
        )
        self.page.update()

app(target=Main, assets_dir="assets", view=WEB_BROWSER)