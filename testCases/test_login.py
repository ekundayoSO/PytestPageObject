
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Demo Web Shop":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            assert False

    def test_Login(self, setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        # Create Class Object
        self.login_Obj = LoginPage(self.driver)
        # Send Values to fields and click login
        self.login_Obj.clickLoginBtn()
        self.login_Obj.setUserEmail(self.email)
        self.login_Obj.setUserPassword(self.password)
        self.login_Obj.clickLogin()
        actual_login_title = self.driver.title
        self.driver.close()
        if actual_login_title == "Demo Web Shop":
            assert True
        else:
            assert False
