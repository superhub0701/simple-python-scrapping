import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#url of the page we want to scrape
url = "https://69b0-188-43-136-33.ngrok.io/1.html"
#setting chrome_options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome('./chromedriver', options=chrome_options)
driver.get(url)

# this is just to ensure that the page is loaded
time.sleep(2)

html = driver.page_source

# this renders the JS code and stores all
# of the information in static HTML code.

# Now, we could simply apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
data = soup.find(id="abcde").span
print(data.text)

driver.close() # closing the webdriver