from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path = 'C:\Selenium\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://advantageonlineshopping.com/#/category/Tablets/3')
driver.find_element_by_link_text('HOME').click()