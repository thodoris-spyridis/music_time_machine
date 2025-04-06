from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

search_date = "1988-04-25"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(f"https://www.billboard.com/charts/hot-100/{search_date}")

artist = driver.find_element(By.XPATH, value='//*[@id="post-1479786"]/div[3]/div/div/div/div[2]/div[2]/ul/li[4]/ul/li[1]/span').text
song_title = driver.find_element(By.CLASS_NAME, value="c-title").text

print(artist)

driver.quit()