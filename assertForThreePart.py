from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()
driver.get('https://oto.repair/')

bodyText = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/div/div/div[2]/ul/li/h4')
bodyTextTobeAsserted="CHÍNH HIỆU"

try:
    print("\n")
    print("######################################################")
    print("\n")
    assert bodyTextTobeAsserted in bodyText.text
    print("{} exists on the home page of the 'WHY CHOOSE US?' list".format(bodyTextTobeAsserted))
except AssertionError:
    if len(bodyText.text.strip()) >0:
        print("{} doesn't exist on the home page of the 'WHY CHOOSE US?' list".format(bodyTextTobeAsserted))
    else:
        print("doesn't have any text on the home page of the 'WHY CHOOSE US?' list")





        
footerText=driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[2]/h6')
footerTextTobeAsserted="DỊCH VỤ"

try:
    print("\n")
    print("######################################################")
    print("\n")
    
    assert footerTextTobeAsserted in footerText.text
    print("{} exists on the footer of the home page ".format(footerTextTobeAsserted))
except AssertionError:
    if len(footerText.text.strip()) >0:
        print("{} doesn't exist on the footer of the home page".format(footerTextTobeAsserted))
    else:
        print("doesn't have any text on the footer of the home page")

navbarText=""
navbarTextTobeAsserted="Danh sách tiệm"

try:
    navbarText = WebDriverWait(driver,5).until( EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/nav/ul/li[2]/a')))
   
except:
    print("\n")
    print("######################################################")
    
    print('timeout')


try:
    print("\n")
    print("######################################################")
    print("\n")
    if navbarText=="" :
        print("navbar button text doesn't exist")
    else:        
        assert navbarTextTobeAsserted in navbarText.text
        print("{} exists on the home page navbar button".format(navbarTextTobeAsserted))
except AssertionError:
    if len(navbarText.text.strip()) >0:
        print("{} doesn't exist on the home page navbar button".format(navbarTextTobeAsserted))
        print("it contain this text: {}".format(navbarText.text.strip()))
    else:
        print("doesn't have any text on navbar button text")     
print("\n")
driver.close()
    