from selenium import webdriver
import unittest
import HtmlTestRunner


class OrangeHRMTest(unittest.TestCase):

    # Methods
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path='/home/flyboypk/PycharmProjects/SeleniumProject/Drivers/chromedriver')
        # cls.driver.maximize_window()

    # Verify HomePage Title
    def test_homePageTitle(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com')
        self.assertEqual("OrangeHRM123", self.driver.title, "Website Title Mismatch")

    # Verify Login
    def test_Login(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com')
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        self.assertEqual("OrangeHRM", self.driver.title, "Website Title Mismatch")

    # Close the browser
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='/home/flyboypk/Projects/Unittest+HTML_Reports+PageObjectModel/Reports'))
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\Reports'))
