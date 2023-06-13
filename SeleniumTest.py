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
lk = '/html/body/div[2]/div[2]/nav[1]/ul/li[1]/a'

for i in usr_text:
    elem_usr.send_keys(i)
    time.sleep(0.3)

for n in pas_text:
    elem_pas.send_keys(n)
    time.sleep(0.3)

elem_lgnbtn.click()

#--------------------

st_mail = '/html/body/div[2]/div[2]/nav[2]/ul/li[9]/a/div/div/span'
st_mail_text = usr_text + '@online.muiv.ru'

student_mail = webdriver.Edge()
student_mail.get("https://gmail.com")

elem_st_mail = student_mail.find_element(By.ID, 'identifierId')
next_btn = browser.find_element(By.ID, 'identifierNext')
print(next_btn)

for i in st_mail_text:
    elem_st_mail.send_keys(i)
    time.sleep(0.3)

time.sleep(120)