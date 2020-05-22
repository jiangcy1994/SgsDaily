from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from config import *

__all__ = ['OpenGame', 'QuitGame']

def OpenGame(url, username, password):
    driver = webdriver.Chrome()
    driver.get(url)
    title = driver.title
    username_input, password_input = driver.find_elements(By.CLASS_NAME, 'dobest_input')
    username_input.send_keys(username)
    password_input.send_keys(password)
    driver.find_element(By.CLASS_NAME, 'mycheckbox').click()
    driver.find_element(By.CLASS_NAME, 'dobest_de_btn').click()
    time.sleep(operation_interval)

    driver.find_element(By.CSS_SELECTOR, '.new_ser1:nth-child(2)').click()
    driver.find_element(By.ID, "newGoInGame").click()
    time.sleep(page_load_interval)
    return driver, title

def QuitGame(driver):
    driver.quit()
