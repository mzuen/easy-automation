from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestPythonOrgSearch:
    url = "https://www.python.org/"

    def set_up(self):
        self._service = Service('./chromedriver')
        self.driver = webdriver.Chrome(service=self._service)

    def test_search_button(self):
        self.set_up()
        self.driver.get(self.url)
        title = self.driver.title
        assert "Python" in title
        assert self.driver.current_url == self.url

        elem = self.driver.find_element(by=By.NAME, value="q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert self.driver.current_url == "https://www.python.org/search/?q=pycon&submit="

        self.driver.close()
