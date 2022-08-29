from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
driver = webdriver.Chrome(executable_path=r"C:\Users\2080897\Documents\test\chromedriver_win32\chromedriver.exe")

fileCsv = "./DatosPruebaPy.csv"
with open(fileCsv, 'r') as file:  
    reader = csv.reader(file,delimiter=";")
    next(reader, None)
    for fila in reader:
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSd8pYrym78Am_OtC7TeJ7igtixsW7eZPbRCAM6vbii3nS-0cA/viewform")
        time.sleep(2)
        elements = driver.find_elements(By.XPATH, "//input[@class='whsOnd zHQkBf']")
        for e in range(0,8):
            elements[e].send_keys(fila[e])
        btnSubmit = driver.find_element(By.XPATH, "//span[@class='NPEfkd RveJvd snByac']")
        time.sleep(2)
        btnSubmit.click()
    driver.close() 
