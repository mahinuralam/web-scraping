from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the path to the chromedriver executable
chromedriver_path = '/Users/prismerp/Documents/personal/chromedriver_mac64/chromedriver'
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


async def callscript(product_name):
    # Create Chrome options object
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    # options.add_argument('--headless')
    options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' # If chrome is not installed in default location

    # Set chromedriver executable path in options object
    options.add_argument(f'--chromedriver-executable={chromedriver_path}')

    # Create a Chrome webdriver instance with options
    driver = webdriver.Chrome(options=options)

    # Navigate to the Amazon website
    driver.get('https://www.amazon.com')

    # Wait for the page to load
    driver.implicitly_wait(10)

    # print(driver.page_source)

    # Do something on the website (e.g., search for a product)
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys(str(product_name))
    search_box.submit()
    driver.implicitly_wait(10)

    # Get a list of all the search result items
    search_results = driver.find_elements(By.CLASS_NAME, "sg-col-16-of-20")
    # print(search_results)
    # Loop through the list of search result items and extract information
    c = 0
    product_map = {}
    start = 4
    # find the parent element of all search results
    for result in search_results:
        try:
            elementsss = result.find_elements(By.CLASS_NAME,'s-widget-container-height-small')
            for element in elementsss:
                try:
                    product_details = element.find_element(By.CLASS_NAME,'a-size-medium').text
                    # print("A -> ",product_details)
                    product_price = element.find_element(By.CLASS_NAME, 'a-price').text
                    # print("S -> ", product_price)
                    nested_span = element.find_element(By.CLASS_NAME, 'a-size-base')
                    span_value = nested_span.text
                    # print("D -> ", span_value)
                    product_link = result.find_element(By.CSS_SELECTOR, 'h2 a').get_attribute('href')
                    # print("F -> ", product_link)
                    temp = {}
                    temp = {
                        'details': product_details,
                        'price': product_price,
                        'span_value': span_value,
                        'url': product_link
                    }
                    # print("TEMP --> ", temp)
                    product_map.update(temp)
                except:
                    print("NOT FOUND")
                    pass

        except Exception as e:
            print("No rating found",e)

    print(" BEFORE ----")
    
    driver.quit()
    
    print("AFTER ---- ")
    
    return product_map