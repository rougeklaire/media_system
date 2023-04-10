from selenium import webdriver
from selenium.webdriver.common.by import By

# Credentials
username = ""
password = ""


driver = webdriver.Firefox()
driver.get("https://accounts.spotify.com/de/login?continue=https%3A%2F%2Fopen.spotify.com%2F")
driver.find_element(By.ID, "login-username").send_keys(username)
driver.find_element(By.ID, "login-password").send_keys(password)
driver.find_element(By.ID, "login-button").click()

#driver.close()
