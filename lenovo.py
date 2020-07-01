from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#MG003KES,YB00598102
service_tag=raw_input("Enter Lenovo Serial Number: ")
options = Options()
options.headless = True
options.add_argument("window-size=1200x600")
driver = webdriver.Chrome(executable_path= r'/Users/swimmchan/Downloads/chromedriver', chrome_options=options)
url = 'https://pcsupport.lenovo.com/ca/en/warrantylookup#/'
driver.implicitly_wait(10)
driver.get(url)

warrantylookup = driver.find_element_by_xpath("//div[@id='app-standalone-warrantylookup']//input")

warrantylookup.send_keys(service_tag)

driver.implicitly_wait(10)

driver.find_element_by_xpath("//button[contains(.,'Submit')]").click()
try:
    end_date = driver.find_element_by_xpath("/html/body/div[2]/section[2]/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div[5]/span[2]").text
    print('Warranty End Date: ' + end_date)
except:
    print('Sorry, no products were found that match that query.')
driver.quit()
