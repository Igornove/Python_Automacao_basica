from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="c:/Users/usuario/Downloads/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('https://www.google.com')

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("you tube")
search_box.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 10)
first_result = wait.until(EC.element_to_be_clickable((By.XPATH, "(//h3)[1]")))
actions = ActionChains(driver)
actions.move_to_element(first_result).click().perform()

time.sleep(3)

search_box = driver.find_element(By.NAME,"search_query")
search_box.send_keys("gameplay rj")
search_box.send_keys(Keys.RETURN) 


wait.until(EC.presence_of_element_located((By.XPATH, "(//ytd-video-renderer)[1]")))

first_video = driver.find_element(By.XPATH, "(//ytd-video-renderer)[1]") 
actions.move_to_element(first_video).click().perform()
time.sleep(10)
driver.quit()
