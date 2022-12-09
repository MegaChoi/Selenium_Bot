from selenium.webdriver.common.by import By
import time
class Comment:
    def __init__(self):
        #Username and password
        self.username = "sonvuvu2020@gmail.com"
        self.password = "19001009Gbc%"
    def lauch(self,driver, targetURL, count = 5):
        #Get facebook mobile
        driver.get("https://m.facebook.com")
        time.sleep(3)
        #Login
        userIdField = driver.find_element(By.ID,"m_login_email")
        passwordField = driver.find_element(By.ID,"m_login_password")   
        loginButton = driver.find_elements(By.TAG_NAME,"button")[0]
        userIdField.send_keys(self.username )
        passwordField.send_keys(self.password)
        loginButton.click()
        time.sleep(4)
        #Get target
        targetURL = targetURL.strip().replace("www","m")
        driver.get(targetURL)
        time.sleep(3)
        # Find comment box and comment
        comment = driver.find_element(By.ID, value= "composerInput")
        send = driver.find_element(By.TAG_NAME,"button")
        # Extract comment
        with open("src\\supply\\Message.txt", "r", encoding= "UTF-8") as f:
            lines = f.readlines()
            try:
                for i in range(len(lines)):
                    time.sleep(3)
                    comment.send_keys(lines[i].strip())
                    send.submit()
            except:
                pass
        time.sleep(5000)





