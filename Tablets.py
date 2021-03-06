from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Class for tablets page
class Tablets:

    def __init__(self, driver):
        self.driver = driver
# Show me my location on the site
    def home(self):
        return self.driver.find_element_by_link_text('HOME')

# General wait for tablets page by general element in the page
    def wait_tablets(self):
        return WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"img[id='16']")))

# Go into hp elite pad page
    def hp_elitepad(self):
        return self.driver.find_element_by_id("16").click()

# Go into hp elite page
    def hp_elite(self):
        return self.driver.find_element_by_id('17').click()

# Go into hp pro  page
    def hp_pro(self):
        return self.driver.find_element_by_id('18').click()