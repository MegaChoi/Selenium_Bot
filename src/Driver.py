from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
class Driver():
    def __init__(self) -> None:
        #Configurations
        self.option = Options()
        self.option.add_argument("--disable-infobars")
        self.option.add_argument("start-maximized")
        self.option.add_argument("--disable-extensions")
        self.option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
        self.PATH = ("C:/Users/Duc/OneDrive/Desktop/Testing/chromedriver.exe")
        self.driver = webdriver.Chrome(chrome_options=self.option, executable_path="path-of-driver\chromedriver.exe")
    def CreatDriver(self):
        return self.driver