from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()
browser.get("https://e.muiv.ru/login/index.php")

elem_usr = browser.find_element(By.ID, 'username')
elem_pas = browser.find_element(By.ID, 'password')
elem_lgnbtn = browser.find_element(By.ID, 'loginbtn')

usr_text = '70178540'
pas_text = 'VuketTecy7387'
left_btn_name = '/html/body/div[2]/nav/div/button'
timetable = '/html/body/div[2]/div[2]/nav[2]/ul/li[5]/a'
for i in usr_text:
    elem_usr.send_keys(i)
    time.sleep(0.3)

for n in pas_text:
    elem_pas.send_keys(n)
    time.sleep(0.3)

elem_lgnbtn.click()
elem_left_btn = browser.find_element(By.XPATH, left_btn_name)
elem_left_btn.click()
timetable_btn = browser.find_element(By.XPATH, timetable)
timetable_btn.click()

ttdate = browser.find_element(By.ID, 'region-main')
print(ttdate.text)

time.sleep(60)