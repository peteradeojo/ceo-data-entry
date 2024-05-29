import csv
from functions import get_company_from_email, parse_entry

data = csv.reader(open("results.csv"))

with open(r"_formatted.txt", "w") as output:
  for row in data:
    # print(row)
    name = row[0]
    kini = "".join(row[1:])
    if name == '' or name == 'Not found' or name == "None":
      name = input(f"who is the ceo of {get_company_from_email(parse_entry(kini))[1]}: ")
    
    output.write(f"{name}\n{kini}\n\n")
