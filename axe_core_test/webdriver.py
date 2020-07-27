from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

__all__ = ['Webdriver']


class Webdriver(Firefox:
    def __init__(self, headless=True):
        options=Options()
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        if headless:
            options.headless=True
        super().__init__(options=options)
