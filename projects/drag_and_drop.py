import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    url = "https://formy-project.herokuapp.com/dragdrop"
    print("navigating to webpage...")
    driver.get(url)
    print("maximizing window....")
    driver.maximize_window()
    source_ele = driver.find_element(By.ID, 'image')
    target_ele = driver.find_element(By.ID, 'box')
    time.sleep(2)
    action = ActionChains(driver)
    print("performing drag and drop....")
    action.drag_and_drop(source_ele, target_ele).perform()
    time.sleep(5)
    print("dragged and dropped successfully....")
except Exception as e:
    print(e)
finally:
    driver.quit()