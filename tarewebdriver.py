from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def Ingresar():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.facebook.com")

    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys("blsblblsz.0804@il.com")
    
   
    password_input = driver.find_element(By.NAME, "pass")
    password_input.send_keys("51649rtyui")
    
    login_button = driver.find_element(By.NAME, "login")
    login_button.click()

    time.sleep(5)

    driver.quit()
Ingresar()

def RecuperarCuenta():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.facebook.com")

    olvide_const=driver.find_element(By.PARTIAL_LINK_TEXT, "¿Olvidaste")
    olvide_const.click()

    email_new = driver.find_element(By.ID, "identify_email")
    email_new.send_keys("hksjdsajd@gmail.com")

    btn_buscar=driver.find_element(By.CLASS_NAME, "_42ft")
    btn_buscar.click()

    time.sleep(5)

    driver.quit()
RecuperarCuenta()

def ChroPath():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.facebook.com")

    email_input = driver.find_element(By.XPATH, "//input[@id='email']")
    email_input.send_keys("blsblblsz.0804@il.com")
    
   
    password_input = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]")
    password_input.send_keys("51649rtyui")
    
    login_button = driver.find_element(By.CSS_SELECTOR, "#email")
    login_button.click()

    time.sleep(5)

    driver.quit()
ChroPath()

    


