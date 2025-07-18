import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def add(a, b):
    return a + b

def scrollIntoViewLocator(driver, locator):
    driver.execute_script("document.querySelector(\""+locator+"\").scrollIntoView()")

def scrollIntoViewElement(driver, element):
    driver.execute_script("arguments[0].scrollIntoView();", element)

def demoQATextBox() :
    driver = webdriver.Chrome()

    driver.get("https://demoqa.com/")
    time.sleep(2)
    ele1 = driver.find_element(By.XPATH, "//h5[.='Elements']")
    scrollIntoViewElement(driver, ele1)
    ele1.click()

    ele2 = driver.find_element(By.XPATH, "//span[.='Text Box']")
    # scrollIntoViewElement(ele2)
    ele2.click()

    # scrollIntoViewElement(driver.find_element(By.XPATH,"//input[@placeholder='Full Name']"))
    driver.find_element(By.XPATH, "//input[@placeholder='Full Name']").send_keys("Welcome to python")

    # scrollView("input[@placeholder='name@example.com']")
    driver.find_element(By.XPATH, "//input[@placeholder='name@example.com']").send_keys("ayyappa@gmail.com")

    # scrollIntoViewElement(driver.find_element(By.XPATH,"//*[@placeholder='Current Address']"))
    driver.find_element(By.XPATH, "//*[@placeholder='Current Address']").send_keys("chennai")

    scrollIntoViewLocator(driver, "#permanentAddress")
    driver.find_element(By.ID, "permanentAddress").send_keys("Tirupati")
    driver.find_element(By.ID, "submit").click()

    name = driver.find_element(By.ID, "name").text
    print(name)

    email = driver.find_element(By.ID, "email").text
    print(email)

    currentAddress = driver.find_element(By.XPATH, "//p[@id='currentAddress']").text
    print(currentAddress)

    # scrollIntoViewElement(driver.find_element(By.XPATH,"//p[@id='permanentAddress']")
    permanentAddress = driver.find_element(By.XPATH, "//p[@id='permanentAddress']").text
    print(permanentAddress)

    time.sleep(4)

    driver.quit()


