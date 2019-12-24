import lxml.html
import requests
import MySQLdb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#conn = MySQLdb.connect(db='Crawler', user='cloud', passwd='1111', charset='utf8mb4')

#c=conn.cursor()

#select_sql = 'SELECT company FROM re_info'

#c.execute(select_sql)

driver = webdriver.PhantomJS()

driver.get('https://www.catch.co.kr/')

#for row in c.fetchall():
#    for i in range(len(row)):

print(driver.title)

input_element = driver.find_element_by_name('SearchList')
input_element.send_keys('삼성생명보험(주)')
input_element.send_keys(Keys.RETURN)

link = driver.find_elements_by_css_selector('.bx-viewport > ul > li > a')
if not link:
    print('해당 결과 없음')
if link:
    detail_link = link[0].get_attribute('href')
    detail_link = 'https://www.catch.co.kr' + detail_link
    print(detail_link)
            
            #detail_page = request.get(detail_link)
            #page = lxml.html.fromstring(detail_page.content)

    print()
    print()
