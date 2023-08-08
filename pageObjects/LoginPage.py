
from selenium.webdriver.common.by import By


class LoginPage:
    homepage_login_class = "ico-login"
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    button_login_class = "login-button"
    link_logout_link_text = "Log out"

    def __init__(self, driver):
        self.driver = driver

    # Action Methods
    def clickLoginBtn(self):
        self.driver.find_element(By.CLASS_NAME, self.homepage_login_class).click()

    def setUserEmail(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self. driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def setUserPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.CLASS_NAME, self.button_login_class).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_link_text).click()
