from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import pickle

__all__ = ['Webdriver']


class Webdriver(Firefox):
    def __init__(self, headless=True):
        options=Options()
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        if headless:
            options.headless=True
        super().__init__(options=options)
		
	def save_cookies(self, paht):
		with open(paht, mode='wb') as f:
			pickle.dump(self.get_cookies(), f)
			
	def load_cookies(self, path):
		with open(path, mode='rb') as f:
			cookies = pickle.load(cookiesfile)
		for cookie in cookies:
			self.add_cookie(cookie)
