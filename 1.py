import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "http://192.168.20.51/raintime_Expo_Sing_V4/web/web/pages/m9_page9.html"
#setting chrome_options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome('./chromedriver', options=chrome_options)
driver.get("http://192.168.20.51")

request_cookies_browser = driver.get_cookies()

#making a persistent connection using the requests library
s = requests.Session()
params = {'username': 'admin', 'password': 'admin'}

c = [s.cookies.set(c['name'], c['value']) for c in request_cookies_browser]

resp = s.post("http://192.168.20.51/cgi/login", params) #I get a 200 status_code

#passing the cookie of the response to the browser
dict_resp_cookies = resp.cookies.get_dict()
response_cookies_browser = [{'name':name, 'value':value} for name, value in dict_resp_cookies.items()]
c = [driver.add_cookie(c) for c in response_cookies_browser]

#the browser now contains the cookies generated from the authentication
driver.get(url)

# this is just to ensure that the page is loaded
time.sleep(3)

html = driver.page_source

# this renders the JS code and stores all
# of the information in static HTML code.

# Now, we could simply apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
temperature01 = soup.find(id="m9_wgt794").span
humidity01 = soup.find(id="m9_wgt797").span
temperature02 = soup.find(id="m9_wgt772").span
humidity02 = soup.find(id="m9_wgt776").span
temperature03 = soup.find(id="m9_wgt779").span
humidity03 = soup.find(id="m9_wgt782").span
windSpeed = soup.find(id="m9_wgt787").span
solar = soup.find(id="m9_wgt789").span
UTCI01 = soup.find(id="m9_wgt800").span
UTCI02 = soup.find(id="m9_wgt803").span
UTCI03 = soup.find(id="m9_wgt806").span
print(temperature01.text, humidity01.text, temperature02.text, humidity02.text, temperature03.text, humidity03.text, windSpeed.text, solar.text, UTCI01.text, UTCI02.text, UTCI03.text)

# driver.close()  # closing the webdriver.  It closes the the browser window on which the focus is set.

# quit() basically calls driver.dispose method which in turn closes all the browser windows and
# ends the WebDriver session gracefully.
driver.quit()
