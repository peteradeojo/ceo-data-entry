import csv
from functions import get_company_from_email, parse_entry
from soup4 import soup4_find

data = csv.reader(open("results.csv"))

with open(r"_formatted.txt", "w") as output:
  for row in data:
    # print(row)
    name = row[0]
    kini = "".join(row[1:])
    if name == '' or name == 'Not found' or name == "None":
      name = soup4_find(get_company_from_email(parse_entry(kini)))
    
    output.write(f"{name}\n{kini}\n\n")
