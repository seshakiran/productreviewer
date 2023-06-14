from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# specify the url of the business page on Google
url = 'https://www.google.com/maps/place/ISKCON+temple+Bangalore/@13.0098328,77.5510964,15z/data=!4m7!3m6!1s0x0:0x7a7fb24a41a6b2b3!8m2!3d13.0098328!4d77.5510964!9m1!1b1'

# create an instance of the Chrome driver
driver = webdriver.Chrome()

# navigate to the specified url
driver.get(url)

# Wait for the reviews to load
wait = WebDriverWait(driver, 20) # increased the waiting time
review_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'wiI7pd')))


totalRev = "div div.fontBodySmall"
username = ".d4r55"
reviews = "wiI7pd"

wait = WebDriverWait(driver, 20)

totalRevCount = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, totalRev))).get_attribute("textContent").split(' ')[0].replace(',','').replace('.','')
print("totalRevCount - ", totalRevCount)

# get the top 10 reviews for argument sake
totalRevCount = 10

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, totalRev))).click()

mydict = {}
found = 0

while found < int(totalRevCount):

    review_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, reviews)))
    reviewer_names = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, username)))

    found = len(mydict)
    for rev, name in zip(review_elements, reviewer_names):
        mydict[name.text] = rev.text
        if len(rev.text) == 0:
            found = int(totalRevCount) + 1
            break

    for i in range(8):
        ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()

    print("found - ", found)

    print(mydict)

    time.sleep(2)





# extract the text of each review
reviews = [element.text for element in review_elements]

# print the reviews
print(reviews)

# close the browser
driver.quit()