from selenium import webdriver
from selenium.webdriver.common.by import By
import time

username=input("Enter mail...?")
password=input("ENter Password..")

url = 'https://www.facebook.com/'

driver = webdriver.Chrome("/home/vaibhav18/Desktop/chromedriver")

driver.get(url)

driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)

time.sleep(2)

driver.find_element_by_id('loginbutton').click()


driver.find_element(By.XPATH, "//*[@name='xhpc_message']").send_keys("Hello this is Mahadev...")

time.sleep(5)

button = driver.find_elements_by_tag_name('button')

for b in button:
    if b.text == "Post":
        b.click()
        




