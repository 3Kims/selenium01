from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

PATH = "C:\\Users\\user\\김주혁\\tools\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# 웹페이지열기
driver.get("https://store.musinsa.com/app/")
