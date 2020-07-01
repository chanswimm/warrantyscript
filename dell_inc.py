# from bs4 import BeautifulSoup
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
# from selenium.webdriver.common.keys import Keys

#70JYWC2, HX315F2
service_tag=raw_input("Enter a Dell Service Tag: ")
driver = webdriver.PhantomJS()
url = 'https://www.dell.com/support/home/en-ca/product-support/servicetag/'+service_tag
# browser = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)
driver.implicitly_wait(10)
# //*[@id="warrantyExpiringLabel"]
try:
    warranty = driver.find_element_by_id('warrantyExpiringLabel').text
    print('Warranty End Date: ' + warranty)
except:
    print('There is no match for that Service Tag or product ID. Please try again, auto-detect or choose from all products')
driver.quit()
