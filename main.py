from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def handlePage1(driver):
    consent = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.ID, "QID11-1-label"))
    #consent = driver.find_element(By.ID, "QR~QID11~1")
    consent.click()

    nextButton = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.ID, "NextButton"))
    nextButton.click()

def handlePage2(driver):
    WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, "QR~QID84"))

    nextButton = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.ID, "NextButton"))
    nextButton.click()

def handlePage3(driver):
    none = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.ID, "QID47-7-label"))
    none.click()

    nextButton = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.ID, "NextButton"))
    nextButton.click()

def handlePage4(driver):
    none = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.ID, "QID46-14-label"))
    none.click()

    nextButton = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.ID, "NextButton"))
    nextButton.click()

def fillOutCheckAtURLWithDriver(url, driver):
    driver.get(url)
    handlePage1(driver)
    handlePage2(driver)
    handlePage3(driver)
    handlePage4(driver)

def fillOutCheckAtURL(url):
    driver = webdriver.Firefox()
    fillOutCheckAtURLWithDriver(url, driver)
    driver.quit()

u = input()
print(u)
input()
fillOutCheckAtURL(u)
