from pageObjects.RegisterNewUserPage import RegisterNewUserPage
from utilities.readProperties import ReadConfig


class Test_002_Registration:
    baseURL = ReadConfig.getApplicationURL()
    random_email = ReadConfig.random_email
    password2 = ReadConfig.generate_random_password()

    def test_Login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # Create Class Object
        self.register_Obj = RegisterNewUserPage(self.driver)
        # Send Values to fields and click login
        self.register_Obj.clickRegisterLinkText()
        self.register_Obj.selectGender()
        self.register_Obj.enterFirstName()
        self.register_Obj.enterLastName()
        self.register_Obj.enterUserEmail(self.random_email)
        self.register_Obj.enterUserPassword(self.password2)
        self.register_Obj.enterUserConfirmPassword(self.password2)
        self.register_Obj.clickRegisterButton()
        message = self.register_Obj.getRegistrationMessage()

        assert "Your registration" in message
