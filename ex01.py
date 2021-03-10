from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("C:/GitClone/chromedriver.exe")

browser.get('https://www.naver.com')
webtoon = browser.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[9]/a')
webtoon.get_attribute('href')

#webtoon.click()
input_sear = browser.find_element_by_id('query')
input_sear.send_keys('python')

input_sear.send_keys(Keys.ENTER)

elems = browser.find_elements_by_tag_name('a')
for e in elems :
    print(e.get_attribute('href'))

brower.save_screenshot("naver_python.png")

time.sleep(5)
browser.close()
browser.quit()