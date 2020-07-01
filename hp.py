from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

#CZC02962G7,CZC02962GZ,CZC02962FG
service_tag=raw_input("Enter HP Serial Number: ")
options = Options()
options.headless = True
options.add_argument("window-size=1280x1696")
driver = webdriver.Chrome(executable_path= r'/Users/swimmchan/Downloads/chromedriver', chrome_options=options)
url = 'https://support.hp.com/us-en/checkwarranty'
# browser = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)
driver.implicitly_wait(10)
warrantylookup = driver.find_element_by_id('wFormSerialNumber')

warrantylookup.send_keys(service_tag)

driver.implicitly_wait(30)

wait = WebDriverWait(driver, 20)
button = wait.until(EC.element_to_be_clickable((By.ID, 'btnWFormSubmit'))).click()
# driver.find_element_by_id('btnWFormSubmit').click()
driver.implicitly_wait(30)
try:
    end_date = driver.find_element_by_xpath("//div[@class='col-lg-18']/div[5]/div[2]").text
    print('Warranty End Date: ' + end_date)
except:
    print('Sorry, no products were found that match that query.')
driver.quit()
