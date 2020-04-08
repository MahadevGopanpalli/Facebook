from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def Details():
    username = input("Enter Email or Phone no. : ")
    password = input("Enter Password : ")

    login(username,password)

def login(username,password):
    url = 'https://www.facebook.com/'

    driver = webdriver.Chrome("/home/vaibhav18/Desktop/chromedriver")

    driver.get(url)

    driver.find_element_by_id('email').send_keys(username)
    driver.find_element_by_id('pass').send_keys(password)

    time.sleep(2)

    driver.find_element_by_id('loginbutton').click()

    
    

    try:
        b=driver.find_element(By.XPATH, "//*[@name='xhpc_message']").send_keys("Hello this post is using python...")
        print ("Succefully logged In...")
        time.sleep(5)

        button = driver.find_elements_by_tag_name('button')

        for b in button:
            if b.text == "Post":
                b.click()
        return
    except Exception as e:
        print("Email or Password Incorrect...")
        if (input("Do u Want try again...(Y/N)?").upper() == 'Y'):
            Details()
        else:
            return 

            
if __name__ == "__main__":
    Details()






