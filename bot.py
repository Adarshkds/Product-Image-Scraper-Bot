from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from lxml import html #We can also use BeautifulSoup for parsing the page source

chrome_options = Options()
chrome_options.add_argument('--headless')  
selenium_service = Service('chromedriver.exe')  
driver = webdriver.Chrome(service=selenium_service, options=chrome_options)

product_links = ["link1", "link2", ...]  # Replace with your actual product links
count = 0
for product_link in product_links:
    try:
        driver.get(product_link)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'className'))) #className is the class name of the image element and has to be replaced with the actual class name
        page_source = driver.page_source
        tree = html.fromstring(page_source)
        zoom_img_element = tree.xpath('//img[contains(@class, "className")]') #className to be replaced

        if zoom_img_element:
            image_src = zoom_img_element[0].get('src')
            print("Product Image Source:", image_src)
            count+=1
            print(count)
        else:
            print("Image source not found on", product_link)

    except TimeoutException:
        print("Timed out while waiting for 'className' element on", product_link) #className to be replaced

driver.quit()
