from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time_sleep = 2

driver.get("https://www.netflix.com/br/login")
input_login = driver.find_element(By.NAME, "userLoginId")
input_login.send_keys("**************@hotmail.com")
sleep(time_sleep)
input_senha = driver.find_element(By.NAME, "password")
sleep(time_sleep)
input_senha.send_keys("*******" + Keys.ENTER)
sleep(time_sleep)

driver.get("https://www.netflix.com/SwitchProfile?tkn=V65C3MHMJRBOHFVAEBGL7FR6TE")
sleep(time_sleep)

driver.get("https://www.netflix.com/watch/70195800?tctx=1%2C0%2C%2C%2C%2C%2C%2C%2C")
