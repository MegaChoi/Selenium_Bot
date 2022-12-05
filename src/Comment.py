from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options


class Comment:
    def __init__(self,username, password, targetURL):
        #Configurations
        self.option = Options()
        self.option.add_argument("--disable-infobars")
        self.option.add_argument("start-maximized")
        self.option.add_argument("--disable-extensions")
        self.option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
        self.PATH = ("C:/Users/Duc/OneDrive/Desktop/Testing/chromedriver.exe")
        self.driver = webdriver.Chrome(chrome_options=self.option, executable_path="path-of-driver\chromedriver.exe")
        #Username and password
        self.username = username
        self.password = password
        self.targetURL = targetURL
    def lauch(self, count = 3):
        #Get facebook mobile
        self.driver.get("https://m.facebook.com")
        time.sleep(1)
        #Login
        userIdField = self.driver.find_element(By.ID,"m_login_email")
        passwordField = self.driver.find_element(By.ID,"m_login_password")   
        loginButton = self.driver.find_elements(By.TAG_NAME,"button")[0]
        userIdField.send_keys(self.username )
        passwordField.send_keys(self.password)
        loginButton.click()
        time.sleep(3)
        #Get target
        self.driver.get(self.targetURL)
        time.sleep(2)
        #Find comment box and comment
        comment = self.driver.find_element(By.ID, value= "composerInput")
        send = self.driver.find_element(By.TAG_NAME,"button")
        test = ["hay", "wow", "ghke", "231"]
        try:
            for i in range(count):
                time.sleep(2)
                comment.send_keys(test[i])
                send.submit()
                print(i)
        except:
            print(Exception)
        time.sleep(5000)






