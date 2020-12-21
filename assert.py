from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://oto.repair/')

myMenuText = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/nav/ul/li[2]/a')
textTobeAsserted="Danh sách tiệm"
try:
    assert textTobeAsserted in myMenuText.text
    print("{} exists on the main menu".format(textTobeAsserted))
except AssertionError:
    if len(myMenuText.text) >0:
        print("{} doesn't exist".format(textTobeAsserted))
    else:
        print("the main menu doesn't have any text")
         

driver.close()
    