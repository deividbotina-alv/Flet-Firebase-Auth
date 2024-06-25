from flet import *

class Main(UserControl):
    def __ini__(self, page: Page,):
        super().__init__()
        self.page = page

app(target=Main, assets_dir="assets", view=WEB_BROWSER)