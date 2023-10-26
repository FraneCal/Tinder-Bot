from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = r"C:\Users\Zemmente\Desktop\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

driver.get("https://tinder.com/")

sing_in = driver.find_element(By.XPATH,'//*[@id="s-1432688076"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
time.sleep(1)
sing_in.click()

time.sleep(1)
facebook = driver.find_element(By.XPATH, '//*[@id="s-1211347640"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div/div')
facebook.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

time.sleep(5)

driver.switch_to.window(fb_login_window)

time.sleep(3)

email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.click()
email.send_keys('stststst1231@outlook.com')

password = driver.find_element(By.XPATH, '//*[@id="pass"]')
password.click()
password.send_keys('In71948N')

log_in = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
log_in.click()

driver.switch_to.window(base_window)

time.sleep(8)

allow_location = driver.find_element(By.XPATH, '//*[@id="s-1211347640"]/main/div/div/div/div[3]/button[1]')
allow_location.click()
time.sleep(2)
not_interested = driver.find_element(By.XPATH, '//*[@id="s-1211347640"]/main/div/div/div/div[3]/button[2]')
not_interested.click()
accept_cookies = driver.find_element(By.XPATH, '//*[@id="s-1432688076"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_cookies.click()
time.sleep(5)

driver.switch_to.window(base_window)

dislike_button = driver.find_element(By.XPATH, '//*[@id="s-1432688076"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button')
dislike_button.click()
time.sleep(1)
