from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path = 'C:\Selenium\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://advantageonlineshopping.com/#/orderPayment')
print(driver.find_element_by_xpath("/html/body/div[3]/section/article/div[2]/div/h2/span/text()"))