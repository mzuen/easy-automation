import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestOnlineLogin:
    
    web_url = "https://practicetestautomation.com/practice-test-login/"
    
    @property
    def expected_result(self):
        return {"login_success_page": "https://practicetestautomation.com/logged-in-successfully/"}
    
    def set_up(self):
        self._service = Service('./chromedriver')
        self.driver = webdriver.Chrome(service=self._service)

    
    def test_login_with_correct_username(self):
        self.set_up()
        self.driver.get(self.web_url)
        username_elem = self.driver.find_element(by=By.NAME, value="username")
        username_elem.send_keys("student")
        
        password_elem = self.driver.find_element(by=By.NAME, value="password")
        password_elem.send_keys("Password123")
        time.sleep(3)
        
        submit_btn = self.driver.find_element(by=By.ID, value="submit")
        submit_btn.click()
        
        time.sleep(1)
        
        assert self.driver.current_url == self.expected_result["login_success_page"]
        
        title_elem =  self.driver.find_element(by=By.CLASS_NAME, value="post-title")
        assert title_elem.text == "Logged In Successfully"
        
        logout_btn_xpath = "/html/body[@id='modern-store-modified']/div[@id='overflow-container']/div[@id='max-width']/section[@id='main-container']/div[@id='loop-container']/div[@class='post-257 page type-page status-publish hentry entry']/article/div[@class='post-content']/div[@class='is-layout-flow wp-block-group']/div[@class='wp-block-group__inner-container']/div[@class='wp-block-button aligncenter is-style-fill']/a[@class='wp-block-button__link has-text-color has-background has-very-dark-gray-background-color']"
        logout_btn = self.driver.find_element(by=By.XPATH, value=logout_btn_xpath)
        
        assert logout_btn.text == "Log out"
        
        time.sleep(1)
        
        self.driver.close()
        
    
    