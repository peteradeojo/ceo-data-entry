import re
from datetime import datetime

noDigitPattern = re.compile(r"\D", re.IGNORECASE)
namePattern = re.compile(r"\w{1,3}", re.IGNORECASE)

def get_addresses(filename):
  f = open(filename)
  data = f.readlines()
  f.close()
  return [x.strip() for x in data]
  
def get_company_from_email(email: str):
  return email.split("@")

def parse_entry(entry: str):
  data = entry.strip().split(" ")
  return data[-1]

def remove_dot_com(address):
  return address.split(".")[0]

def get_companies(filename):
  return [get_company_from_email(parse_entry(x))[-1] for x in get_addresses(filename)]

def test_valid_name(name: str):
  l = len(name.split(" "))
  return l > 1 and l <= 3 and noDigitPattern.match(name) is not None

def get_datetime():
  return datetime.now().strftime("%d-%m-%Y-%H:%M:%S")

def get_selectors():
  with open("selectors.txt") as s:
    return [x.strip() for x in s.readlines()]
  

def inspect_result(result: str):
  print(result)
  options = result.replace(" - ", " ").split(" ")
  n = len(options)
  for i in range(n):
    print(f"{i}. {options[i]}")

  move = input("A to make selection, B to overwrite: ")
  if move.lower() == "a":
    selected = input("Enter numbers to select: ").strip().split(",")
    name = " ".join([options[int(s)] for s in selected])
    print(name)
    return name
  else:
    return input("Enter name: ").strip()


if __name__ == '__main__':
  with open("names.txt") as file:
    names = [n.strip() for n in file.readlines()]
    for n in names:
      inspect_result(n)