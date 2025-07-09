import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

source_path = "//img[@alt='The peaks of High Tatras']"
target_path = "//div[@id='trash']"
frame_ele = "//iframe[@class='demo-frame lazyloaded']"

driver = webdriver.Chrome()
try:
    url = "https://www.globalsqa.com/demo-site/draganddrop/"
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
    time.sleep(4)
    # url = "https://formy-project.herokuapp.com/dragdrop"
    # print("navigating to webpage...")
    # driver.get(url)
    # print("maximizing window....")
    # driver.maximize_window()
    # source_ele = driver.find_element(By.ID, 'image')
    # target_ele = driver.find_element(By.ID, 'box')
    # time.sleep(2)
    # action = ActionChains(driver)
    # print("performing drag and drop....")
    # action.drag_and_drop(source_ele, target_ele).perform()
    # time.sleep(5)
    # print("dragged and dropped successfully....")
except Exception as e:
    print(e)
finally:
    driver.quit()