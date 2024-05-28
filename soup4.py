from functions import *
from bs4 import BeautifulSoup
import requests
import sys

results = []

not_found = []

filename = sys.argv[1]

addresses = get_addresses(filename)
for address in addresses:
  _, company = get_company_from_email(parse_entry(address))
  html = requests.get(f"https://www.google.com/search?q=who is the ceo of {remove_dot_com(company)}")
  soup = BeautifulSoup(html.text, features="html.parser")

  el = soup.css.select_one("#main > div:nth-of-type(3) span")
  if el and test_valid_name(el.text):
    results.append(f"{el.text}\n{address}\n")
  else:
    not_found.append(address)


print(f"Found {len(results)} out of {len(addresses)} companies")

filedate = get_datetime()
if len(results) > 0:
  with open(f"results-{filedate}.txt", "w") as f:
    f.write("\n".join(results))

if len(not_found) > 0:
  with open(f"not-found.txt", "w") as f:
    f.write("\n".join(not_found))