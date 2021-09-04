import pytest
#import pytest_html
import constants as const
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time 
 
#Fixture for Firefox
@pytest.fixture(params=["firefox"],scope="class")
def driver_init(request):
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()
 
#Main Test 
@pytest.mark.usefixtures("driver_init")
class Test_GMAIL():
    def test_open_url(self):
        self.driver.get(const.BASE_URL)
        print(self.driver.title)
        assert self.driver.title == "Gmail"
        time.sleep(5)
    
    def test_email_field_type(self):
        email = self.driver.find_element_by_css_selector('input[type="email"]')
        assert email.tag_name == "input"
        time.sleep(5)
        return 

    def test_email_feild_text(self):
        email = self.driver.find_element_by_class_name('snByac')
        assert email.text == "Email or phone"
        time.sleep(5)
        return

    def test_email_field_with_valid_input(self):
        email = self.driver.find_element_by_css_selector('input[type="email"]')
        email.send_keys(const.EMAIL)
        time.sleep(5)
        return 

    def test_next_button_text(self):
        button = self.driver.find_element_by_css_selector('span[jsname="V67aGc"]')
        assert button.text == "Next"
        return

    def test_next_button_type(self):
        button = self.driver.find_element_by_css_selector('button[jsname="LgbsSe"]')
        assert button.tag_name == "button" 
        return
           
    def test_next_button_click(self):
        button = self.driver.find_element_by_css_selector('button[jsname="LgbsSe"]')
        button.click()
        time.sleep(3)
        return

    