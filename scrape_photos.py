import os

import wget as wget
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


# this code scrapes photos of a  searched hashtag


# specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")

# target username and password
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
username.clear()
password.clear()

# enter username and password
username.send_keys("username")
password.send_keys("password")

# target login button and click it
log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

# not_now and not_now2 are alerts to handle-pay attention,cause you might have only one
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not Now')]"))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not Now')]"))).click()

# target the search input field
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

# search for hashtag cat
keyword = "#cat"
searchbox.send_keys(keyword)
# searchbox.send_keys(Keys.ENTER)

# its our enter function code
my_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + keyword[1:] + "/')]")))
my_link.click()

# scroll down 2 times,to increase - scroll more
scrolls = 1
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(5)

# follow each image link and extract only image at index=1
imgs = driver.find_elements_by_tag_name('img')
imgs = [img.get_attribute('src') for img in imgs]

#-----------------save--------------------------------------------------------
# # save images to computer
# path = os.getcwd()
# path = os.path.join(path, keyword[1:] + "s")
#
# # create directory
# os.mkdir(path)
#
# # download images
# counter = 0
# for image in imgs:
#     save_as = os.path.join(path, keyword[1:] +str(counter)+'.jpg')
#     wget.download(image, save_as)
#     counter += 1