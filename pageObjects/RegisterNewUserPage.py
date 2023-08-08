
from selenium.webdriver.common.by import By


class RegisterNewUserPage:
    link_register_class = "ico-register"
    radioButton_gender_id = "gender-male"
    textbox_firstName_id = "FirstName"
    textbox_lastName_id = "LastName"
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    textbox_confirmPassword_id = "ConfirmPassword"
    button_register_id = "register-button"
    element_registration_message_class = "result"

    def __init__(self, driver):
        self.driver = driver

    # Action Methods
    def clickRegisterLinkText(self):
        self.driver.find_element(By.CLASS_NAME, self.link_register_class).click()

    def selectGender(self):
        self.driver.find_element(By.ID, self.radioButton_gender_id).click()

    def enterFirstName(self):
        self.driver.find_element(By.ID, self.textbox_firstName_id).send_keys("Amina")

    def enterLastName(self):
        self.driver.find_element(By.ID, self.textbox_lastName_id).send_keys("Bella")

    def enterUserEmail(self, random_email):
        self. driver.find_element(By.ID, self.textbox_email_id).send_keys(random_email)

    def enterUserPassword(self, password2):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password2)

    def enterUserConfirmPassword(self, password2):
        self.driver.find_element(By.ID, self.textbox_confirmPassword_id).send_keys(password2)

    def clickRegisterButton(self):
        self.driver.find_element(By.ID, self.button_register_id).click()

    def getRegistrationMessage(self):
        message_element = self.driver.find_element(By.CLASS_NAME, self.element_registration_message_class)
        return message_element.text
