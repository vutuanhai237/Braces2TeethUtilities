import urllib.request
from PIL import Image
from selenium import webdriver
for i in range(0, 2000):
    driver = webdriver.Firefox(executable_path=r'C:\Users\haoquach\Desktop\crawler\geckodriver-v0.27.0-win64\geckodriver.exe')
    url = 'https://thispersondoesnotexist.com/'
    driver.get(url)
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    images = driver.find_elements_by_tag_name('img')
    for image in images:
        print(image.get_attribute('src'))
        urllib.request.urlretrieve(image.get_attribute('src'), f"download5\{i}.png", )
    driver.quit()
