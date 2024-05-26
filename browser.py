from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from functions import *
import sys

filename = sys.argv[1]
addresses = get_companies(filename)

results = []
not_found= []

wait_time = 1.5

# Set up selectors
selectors = []
selectors_tally = {}
with open("selectors.txt") as s:
  selectors = [x.strip() for x in s.readlines()]
  for i in range(len(selectors)):
    selectors_tally[i] = 0

chrome_app_path = "./chromedriver/chromedriver"
# user_data_dir = ""
options = webdriver.ChromeOptions()
options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
# options.add_argument(f"--user-data-dir={user_data_dir}")

service = webdriver.ChromeService(executable_path=chrome_app_path, service_args=["--user-profile=Default", "--profile-directory=Default"])

driver = webdriver.Chrome(options=options, service=service, keep_alive=True)

def test_did_you_mean():
  did_you_mean = driver.find_elements(By.PARTIAL_LINK_TEXT, "who is the ceo of")
  return len(did_you_mean) > 0

def test_selectors(driver):
  found = None
  for i in range(len(selectors)):
    selector = selectors[i]
    try:
      el = WebDriverWait(driver, wait_time).until(lambda x: x.find_element(By.CSS_SELECTOR, selector))
      found = el.text

      # Score selector
      if i in selectors_tally:
        selectors_tally[i] +=1
      else:
        selectors_tally[i] = 1

      break
    except:
      pass

  return found

def get_selector_report():
  with open("selector-report.txt", "w") as sw:
    for i in selectors_tally:
      sw.write(f"{selectors[i]}\nScore: {selectors_tally[i]}\n\n")

for address in addresses:
  try:
    driver.get(f"https://www.google.com/search?q=who+is+the+ceo+of+{remove_dot_com(address)}")

    name = test_selectors(driver)
    if name is not None:
      results.append(f"{address} {name}")
    else:
      not_found.append(address)
  except:
    continue

tt = get_datetime()

print(f"Found {len(results)} out of {len(addresses)} companies")

if len(results) > 0:
  with open(f"results-{tt}.txt", "w") as f:
    f.write("\n".join(results))

if len(not_found) > 0:
  with open(f"not-found.txt", "w") as f:
    f.write("\n".join(not_found))

get_selector_report()