from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time_sleep = 2

driver.get("https://accounts.spotify.com/pt-BR/login")
sleep(time_sleep)
input_login = driver.find_element(By.ID, "login-username")
input_login.send_keys("************@outlook.com")
sleep(time_sleep)
input_password = driver.find_element(By.ID, "login-password")
input_password.send_keys("**********")
sleep(time_sleep)
bt_login = driver.find_element(By.ID, "login-button")
bt_login.click()
sleep(time_sleep)
bt_web_player = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="web-player-link"]')
bt_web_player.click()
sleep(time_sleep)
driver.get("https://open.spotify.com/track/0J6mQxEZnlRt9ymzFntA6z")
