import urllib.request
from PIL import Image
from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'C:\Users\haime\Downloads\geckodriver-v0.27.0-win64\geckodriver.exe')
  
def craw(driver, url):
    driver.get(url)
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    images = driver.find_elements_by_tag_name('img')
    i = 0
    for image in images:
        print(image.get_attribute('src'))
        urllib.request.urlretrieve(image.get_attribute('src'), f"{i}.png", )
        i = i + 1
    driver.quit()

craw(driver, 'https://www.facebook.com/photo?fbid=176561697507431&set=g.1961375810770323')