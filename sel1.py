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

# 타겟 엘레멘트검색. ideal 검색순서 (id -> name -> class)
# search박스 찾기 >> search박스 기본 value 지우기 >> search박스에 입력할 내용 >> RETURN == 엔터
search = driver.find_element_by_id('search_query')
search.clear()
search.send_keys("vans")
search.send_keys(Keys.RETURN)

# 조건이 맞을때까지 기다리게하기
# EC.prsenece of element located : By.[NAME/ID/CLASS_NAME/TAG_NAME]
try:
    searchList = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "searchList"))
    )
    itemList = searchList.find_elements_by_name("goods_link")

    for item in itemList:
        print(item.text)

finally:
    print("done")
    driver.quit()
