import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.tutorialspoint.com/selenium/practice/webtables.php"
driver.get(url)
driver.maximize_window()
print("Page Title: ", driver.execute_script('return document.title;'))
print("Site URL: ", driver.execute_script('return document.URL;'))

time.sleep(2)

cell_xpath = "//table[@class='table table-striped mt-3']"
col_xpath = "//table[@class='table table-striped mt-3']/thead/tr/th"
row_xpath = "//table[@class='table table-striped mt-3']/tbody/tr"

row_ele = driver.find_elements(By.XPATH, row_xpath)
print('Row Len: ', len(row_ele))

col_ele = driver.find_elements(By.XPATH, col_xpath)
print('Column Len: ', len(col_ele))

for col in col_ele:
    driver.execute_script("arguments[0].style.background='black'; arguments[0].style.color='white';", col)
time.sleep(2)

for row in row_ele:
    driver.execute_script("arguments[0].style.background='orange'; arguments[0].style.color='black';", row)
    cell_path = row.find_elements(By.TAG_NAME, 'td')
    data = [cell.text for cell in cell_path]
    print(data)
    time.sleep(2)