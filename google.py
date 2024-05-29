from driver import initialize_driver, find_element, install_captcha_solver
from functions import *
from time import sleep
import sys

def parse_name_out_of_text(text: str):
  return text.split("-")[0].strip()

def confirm_name(name):
  pass

driver = initialize_driver()

if len(sys.argv) == 1:
  query = "who+is+the+ceo+of+"
else:
  query = sys.argv[1]

# selector = "#rso > div:nth-child(1) > div > div > div > div.kb0PBd.cvP2Ce.A9Y9g.jGGQ5e > div > div > span > a > h3"
selector = "#rso span > a > h3"

install_captcha_solver(driver)

addresses = get_addresses("emails1.txt")

filename = f"results.csv"
file = open(filename, "w")

selectors = get_selectors()

n = len(addresses)
for i in range(n):
  address = addresses[i]
  _, company = get_company_from_email(parse_entry(address))
  print(f"{i+1}/{n} querying for:", company)
  driver.get(f"https://www.google.com/search?q={query}{remove_dot_com(company)}")
  
  for s in selectors:
    el = find_element(driver, s, 2)
    if el is not None:
      break

  if el is not None:
    file.write(f"{inspect_result(el.text)},{address}\n")
  else:
    file.write(f"Not found,{address}\n")
  
  sleep(1)

file.close()
driver.quit()