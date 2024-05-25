from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os, sys

from functions import get_companies, remove_dot_com

filename = sys.argv[1]

chrome_app_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_options = Options()
chrome_options.binary_location = chrome_app_path
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")

chrome_service = Service(os.path.join(os.getcwd(), "chromedriver/chromedriver"))


driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

results = []

for company in get_companies(filename):
  driver.get(f"https://google.com/search?q=who+is+the+ceo+of+{remove_dot_com(company)}")

  # resultXPath = "/html/body/div[5]/div/div[13]/div/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div[2]/div/span/span/b"
  resultXPath = """[data-attrid="wa:/description"]"""

  result = WebDriverWait(driver, 20, 1).until(lambda x: x.find_element(By.CSS_SELECTOR, resultXPath))
  print(result)

  results.append(f"{company} {result.text}")

driver.close()

results = "\n".join(results)
print(results)