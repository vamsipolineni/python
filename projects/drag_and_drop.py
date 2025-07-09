import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    url = "https://formy-project.herokuapp.com/dragdrop
    print("navigating to webpage...")
    driver.get(url)
    print("maximizing window....")
    driver.maximize_window()
    print("switching to frame....")
    frame = driver.find_element(By.XPATH, frame_ele)
    driver.switch_to.frame(frame)
    source_ele = driver.find_element(By.XPATH, source_path)
    target_ele = driver.find_element(By.XPATH, target_path)
    time.sleep(2)
    print("performing drag and drop....")
    action = ActionChains(driver)
    action.drag_and_drop(source_ele, target_ele).perform()
    print("dragged and dropped successfully....")
except Exception as e:
    print(e)
    time.sleep(4)
except Exception as es:
    print(es)
finally:
    driver.quit()
